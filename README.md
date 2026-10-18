# ⚡ RosieRiot Overdrive 2026

> **Recon loud. Archive clean.**  
> A GlitchByte Phantom Labs tool for authorized reconnaissance, colorful terminal feedback, and organized intelligence reports.

![RosieRiot Overdrive repository banner](assets/rosieriot-overdrive-banner.png)

## About

**RosieRiot Overdrive** is an Ubuntu/Linux Python 3 launcher for demonstrations and explicitly authorized assessments. It works alongside optional external tools rather than installing or changing them automatically.

**Tool stack:** Subfinder · DNSX · HTTPX · Naabu · Nuclei · Aquatone (optional)

## Quick start

Download and extract the project's release ZIP, then run:

```bash
mkdir -p "$HOME/PhantomLabsLaunchers"
unzip -n "$HOME/Downloads/rosieriot_overdrive_2026.zip" -d "$HOME/PhantomLabsLaunchers"
bash "$HOME/PhantomLabsLaunchers/rosieriot_overdrive_2026/install_missing_stack.sh"
```

Try the **offline demo** before any network operations:

```bash
python3 "$HOME/PhantomLabsLaunchers/rosieriot_overdrive_2026/rosieriot_overdrive.py" \
  --target example.com --demo --color always
```

Check installed dependencies:

```bash
bash "$HOME/PhantomLabsLaunchers/rosieriot_overdrive_2026/verify_stack.sh"
```

The release archive and banner must be uploaded to this repository before the links here will work. For the authoritative command flags, run `python3 rosieriot_overdrive.py --help` from the extracted tool directory.

## Project map

- `assets/`: original RosieRiot identity artwork
- `rosieriot_overdrive_2026/`: Python launcher and install/verification scripts
- `examples/`: demonstration output and sample reports
- `patches/`: maintenance and version notes
- `vault/`: safe backup manifests and checksums

## Lab network

- [GlitchByte Phantom Labs headquarters](https://github.com/Hellfire13666/glitchbyte-phantom-labs)
- [GlitchByte Phantom Labs release vault](https://github.com/Hellfire13666/glitchbyte-phantom-labs-releases)

## Safety and publication

Use active probing only against systems you own or have explicit permission to assess. Do not publish private target reports, credentials, tokens, or personal data. Keep timestamped backup copies and verify checksums before restoring.

**Built in Cultivation Room. Powered through RosieRiot Overdrive. Archived in the Vault.**
