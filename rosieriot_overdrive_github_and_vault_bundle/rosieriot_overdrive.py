#!/usr/bin/env python3
"""RosieRiot Overdrive: scoped, permission-gated reconnaissance launcher."""
import argparse, datetime, json, os, pathlib, re, shutil, subprocess, sys, time

TOOLS = [('subfinder','Subdomain discovery'),('dnsx','DNS resolution'),('httpx','HTTP probe'),('naabu','Port discovery'),('nuclei','Template checks'),('aquatone','Visual snapshot')]
PALETTE={'pink':'\033[95m','cyan':'\033[96m','yellow':'\033[93m','green':'\033[92m','red':'\033[91m','dim':'\033[2m','end':'\033[0m'}

def main():
    p=argparse.ArgumentParser(description='RosieRiot Overdrive | GlitchByte Phantom Labs')
    p.add_argument('--target',required=True,help='Domain you own or are explicitly authorized to assess')
    p.add_argument('--demo',action='store_true',help='Offline demo, never contacts target')
    p.add_argument('--live',action='store_true',help='Execute scoped live checks (requires --authorized)')
    p.add_argument('--authorized',action='store_true',help='Confirm explicit authorization for target')
    p.add_argument('--color',choices=['auto','always','never'],default='auto')
    p.add_argument('--out',default=str(pathlib.Path.home()/'RosieRiotReports'))
    p.add_argument('--timeout',type=int,default=55,help='Per-command timeout; default 55 seconds')
    p.add_argument('--modules',default='subfinder,dnsx,httpx',help='Comma-separated permitted modules; naabu/nuclei/aquatone opt-in')
    p.add_argument('--max-hosts',type=int,default=20)
    a=p.parse_args()
    if not re.fullmatch(r'(?=.{1,253}$)[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?)+',a.target): p.error('Use a valid domain such as example.com')
    if a.demo==a.live: p.error('Choose exactly one of --demo or --live')
    if a.live and not a.authorized: p.error('--live requires --authorized for a domain you own or are permitted to scan')
    modules=[x.strip() for x in a.modules.split(',') if x.strip()]
    allowed={x[0] for x in TOOLS}
    if set(modules)-allowed: p.error('Unknown modules: '+', '.join(sorted(set(modules)-allowed)))
    a.timeout=max(5,min(85,a.timeout)); a.max_hosts=max(1,min(100,a.max_hosts))
    colors=a.color=='always' or (a.color=='auto' and sys.stdout.isatty())
    def say(msg,key='cyan'):
        print((PALETTE[key]+msg+PALETTE['end']) if colors else msg,flush=True)
    say('╔══════════════════════════════════════════════════╗','pink')
    say('║  ROSIERIOT OVERDRIVE 2026 :: PHANTOM LABS        ║','pink')
    say('╚══════════════════════════════════════════════════╝','pink')
    say(f'◆ TARGET {a.target}    ◆ MODE {"OFFLINE DEMO" if a.demo else "AUTHORIZED LIVE"}','yellow')
    out=pathlib.Path(a.out).expanduser()/f'{a.target}_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}'
    out.mkdir(parents=True,exist_ok=True)
    report={'target':a.target,'mode':'demo' if a.demo else 'live','started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'modules':{},'notice':'Only assess domains and systems you are authorized to test.'}
    hosts=[a.target]
    def execute(label,argv,stdin=None):
        cmd=shutil.which(argv[0]);
        if not cmd:
            say(f'  ◇ {label}: SKIPPED (not installed)','yellow')
            return {'status':'missing','cmd':argv[0]}
        try:
            r=subprocess.run([cmd]+argv[1:],input=stdin,text=True,capture_output=True,timeout=a.timeout,check=False)
            output=(r.stdout or '').strip(); error=(r.stderr or '').strip()
            (out/f'{label}.txt').write_text(output+('\n[stderr]\n'+error if error else '')+'\n',encoding='utf8')
            say(f'  ◇ {label}: exit={r.returncode}, {len(output.splitlines())} output lines','green' if r.returncode==0 else 'yellow')
            if error: say('    NOTE: '+error[:250].replace('\n',' '),'yellow')
            return {'status':'ok' if r.returncode==0 else 'error','exit_code':r.returncode,'lines':len(output.splitlines()),'output_file':f'{label}.txt','stdout':output}
        except subprocess.TimeoutExpired:
            say(f'  ◇ {label}: TIMEOUT after {a.timeout}s (continuing)','yellow')
            return {'status':'timeout','seconds':a.timeout}
        except OSError as ex:
            say(f'  ◇ {label}: ERROR {ex}','red')
            return {'status':'error','message':str(ex)}
    if a.demo:
        for m in modules:
            say(f'◆ MODULE {m.upper()}','cyan'); report['modules'][m]={'status':'demo','description':dict(TOOLS)[m],'example':'No network requests made'}
            say('  ◇ DEMO: sample stage complete (no network calls)','green')
        (out/'demo_output.txt').write_text('Offline demonstration. No target scanned.\n',encoding='utf8')
    else:
        if 'subfinder' in modules:
            say('◆ MODULE SUBFINDER'); r=execute('subfinder',['subfinder','-d',a.target,'-silent','-timeout','15']); report['modules']['subfinder']={k:v for k,v in r.items() if k!='stdout'}
            if r.get('status')=='ok':
                hosts=sorted({h.strip() for h in r['stdout'].splitlines() if h.strip()==a.target or h.strip().endswith('.'+a.target)})[:a.max_hosts] or [a.target]
        (out/'scoped_hosts.txt').write_text('\n'.join(hosts)+'\n',encoding='utf8')
        # default stage sequence uses bounded input, bounded execution time, and low request concurrency
        if 'dnsx' in modules:
            say('◆ MODULE DNSX'); r=execute('dnsx',['dnsx','-silent','-retry','1','-t','2'], '\n'.join(hosts)+'\n'); report['modules']['dnsx']={k:v for k,v in r.items() if k!='stdout'}
        if 'httpx' in modules:
            say('◆ MODULE HTTPX'); r=execute('httpx',['-silent','-status-code','-title','-threads','2','-rl','2'], '\n'.join(hosts)+'\n'); report['modules']['httpx']={k:v for k,v in r.items() if k!='stdout'}
        if 'naabu' in modules:
            say('◆ MODULE NAABU (opt-in active scan)'); r=execute('naabu',['naabu','-host',a.target,'-top-ports','100','-rate','10','-silent']);report['modules']['naabu']={k:v for k,v in r.items() if k!='stdout'}
        if 'nuclei' in modules:
            say('◆ MODULE NUCLEI (opt-in template scanning)'); r=execute('nuclei',['nuclei','-u','https://'+a.target,'-severity','info,low','-rl','2','-c','2','-silent']);report['modules']['nuclei']={k:v for k,v in r.items() if k!='stdout'}
        if 'aquatone' in modules:
            say('◆ MODULE AQUATONE (opt-in browser snapshots)');r=execute('aquatone',['aquatone','-out',str(out/'aquatone')], 'https://'+a.target+'\n');report['modules']['aquatone']={k:v for k,v in r.items() if k!='stdout'}
    report['completed_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
    (out/'report.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
    say(f'◆ SAVED REPORT {out}','pink')
    say('◆ COMPLETE','green')
if __name__=='__main__': main()
