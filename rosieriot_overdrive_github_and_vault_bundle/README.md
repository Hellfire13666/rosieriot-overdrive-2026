<!-- GLITCHBYTE-UPLOAD-DOOR:START -->
<div align="right"><a href="https://github.com/Hellfire13666/rosieriot-overdrive-2026/upload/main"><img alt="UPLOAD FILES" src="https://img.shields.io/badge/UPLOAD-FILES-00D9FF?style=flat-square&logo=github&logoColor=white"></a></div>
<!-- GLITCHBYTE-UPLOAD-DOOR:END -->

<div align="center">

![RosieRiot Overdrive](assets/rosieriot-overdrive-banner.png)

# ROSIERIOT OVERDRIVE 2026

**GlitchByte Phantom Labs • Python 3 • Ubuntu/Linux**

*“Recon loud. Archive clean.”*

An authorized, modular reconnaissance launcher with colorful terminal feedback, an offline demonstration, and JSON/text reports.

</div>

## Tool stack

| Module | Function | Requirement |
|---|---|---|
| Subfinder | Subdomain enumeration | External binary |
| DNSX | DNS resolution | External binary |
| HTTPX (ProjectDiscovery) | Web probing | External binary |
| Naabu | Port discovery | Opt-in, authorized targets only |
| Nuclei | Low/informational template checks | Opt-in, authorized targets only |
| Aquatone | Website screenshots | Optional, may not be installed |

The artwork shows all six components, not their verified availability. A missing external binary is reported as unavailable, not installed automatically.

## Download and install

Download `rosieriot_overdrive_2026.zip` from this repository, place it in `~/Downloads`, then run:

```bash
mkdir -p "$HOME/PhantomLabsLaunchers"
unzip -n "$HOME/Downloads/rosieriot_overdrive_2026.zip" -d "$HOME/PhantomLabsLaunchers"
bash "$HOME/PhantomLabsLaunchers/rosieriot_overdrive_2026/install_missing_stack.sh"
bash "$HOME/PhantomLabsLaunchers/rosieriot_overdrive_2026/verify_stack.sh"
```

For a cloned repository, the launcher can also be run directly from the clone after checking dependencies.

## Offline demo

```bash
python3 rosieriot_overdrive.py --target example.com --demo --color always
```

## Authorized live assessment

```bash
python3 rosieriot_overdrive.py --target YOUR_OWN_DOMAIN.com --live --authorized \
  --modules subfinder,dnsx,httpx --timeout 25 --max-hosts 15 --color always
```

Only test domains you own or have explicit permission to assess. No exploitation capability is bundled. The tool is a reconstructed distribution; live operation has not been independently end-to-end verified.

## Reports

By default results save to `~/RosieRiotReports/<domain>_<timestamp>/` including `report.json` and per-module output files. Never commit reports containing private target data.

## Artwork and Vault

- `assets/rosieriot-overdrive-banner.png`: project hero artwork
- `assets/rosieriot-overdrive-icon.png`: square repository art
- `rosieriot_overdrive_2026.zip`: standalone Linux distribution
- `VAULT_MANIFEST.json`: SHA-256 backup inventory

**Vault doctrine:** Build it. Test it. Archive it. Protect the original.

## Releases and patches

See `patches/PATCH_NOTES.md` and `installers/OPTIONAL_TOOLS.md`. New releases should be versioned and checksummed rather than replacing previous backups.
