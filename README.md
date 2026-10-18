<div align="center">

![RosieRiot Overdrive banner](rosieriot_overdrive_github_and_vault_bundle/assets/rosieriot-overdrive-banner.png)

# ⚡ ROSIERIOT OVERDRIVE 2026
**GlitchByte Phantom Labs • Ubuntu/Linux • Python 3**

### *“Recon loud. Archive clean.”*

**Recon • Intel • Visualize • Archive**

</div>

## 🚀 About
RosieRiot Overdrive is a modular launcher for offline demonstrations and authorized reconnaissance with colorful terminal feedback and organized reports. Its external tools are optional; they are not installed automatically.

| Module | Purpose | Status |
|---|---|---|
| Subfinder | Subdomain discovery | External binary |
| DNSX | DNS resolution | External binary |
| HTTPX (ProjectDiscovery) | Web service probing | External binary |
| Naabu | Port discovery | Opt-in for authorized targets |
| Nuclei | Template-based checks | Opt-in for authorized targets |
| Aquatone | Website screenshots | Optional |

The banner is artwork, not a live status dashboard. Check the actual environment using the verification script.

## 📦 Download
**[Download RosieRiot Overdrive ZIP](rosieriot_overdrive_github_and_vault_bundle/rosieriot_overdrive_2026.zip)** · [View the Python launcher](rosieriot_overdrive_github_and_vault_bundle/rosieriot_overdrive.py) · [View the square artwork](rosieriot_overdrive_github_and_vault_bundle/assets/rosieriot-overdrive-icon.png)

On GitHub, open the ZIP link above and use **Download raw file**, then save it to `~/Downloads/rosieriot_overdrive_2026.zip`.

## 🛠️ Ubuntu install

```bash
mkdir -p "$HOME/PhantomLabsLaunchers"
unzip -n "$HOME/Downloads/rosieriot_overdrive_2026.zip" -d "$HOME/PhantomLabsLaunchers"
bash "$HOME/PhantomLabsLaunchers/rosieriot_overdrive_2026/install_missing_stack.sh"
bash "$HOME/PhantomLabsLaunchers/rosieriot_overdrive_2026/verify_stack.sh"
```

### Offline demo
```bash
python3 "$HOME/PhantomLabsLaunchers/rosieriot_overdrive_2026/rosieriot_overdrive.py" \
  --target example.com --demo --color always
```

### Authorized operations
Check supported options before using live modules:
```bash
python3 "$HOME/PhantomLabsLaunchers/rosieriot_overdrive_2026/rosieriot_overdrive.py" --help
```

Only assess domains or systems you own or are explicitly authorized to test. Live operation has not been independently verified end to end.

## 📂 Tool files and backup index
The upload currently lives inside [`rosieriot_overdrive_github_and_vault_bundle/`](rosieriot_overdrive_github_and_vault_bundle/). Links below point to the **actual uploaded paths**:

- [Installer](rosieriot_overdrive_github_and_vault_bundle/install_missing_stack.sh) · [Verification](rosieriot_overdrive_github_and_vault_bundle/verify_stack.sh)
- [Optional tools instructions](rosieriot_overdrive_github_and_vault_bundle/installers/OPTIONAL_TOOLS.md)
- [Demo output](rosieriot_overdrive_github_and_vault_bundle/examples/demo_output.txt)
- [Patch notes](rosieriot_overdrive_github_and_vault_bundle/patches/PATCH_NOTES.md)
- [Backup checksum manifest](rosieriot_overdrive_github_and_vault_bundle/VAULT_MANIFEST.json)
- [Repository banner](rosieriot_overdrive_github_and_vault_bundle/assets/rosieriot-overdrive-banner.png) · [Square logo](rosieriot_overdrive_github_and_vault_bundle/assets/rosieriot-overdrive-icon.png)

## 🔐 Vault protocol
Every release gets a versioned backup package, an inventory with SHA-256 checksums, and a recovery path. This repository contains a backup manifest; **the separate Vault archive must be uploaded and verified independently**. Do not publish secrets or private target results.

[Phantom Labs headquarters](https://github.com/Hellfire13666/glitchbyte-phantom-labs) · [Release Vault](https://github.com/Hellfire13666/glitchbyte-phantom-labs-releases)

**Build it. Test it. Archive it. Protect the original.**
