<!-- GLITCHBYTE-UPLOAD-DOOR:START -->
<div align="right"><a href="https://github.com/Hellfire13666/rosieriot-overdrive-2026/upload/main"><img alt="UPLOAD FILES" src="https://img.shields.io/badge/UPLOAD-FILES-00D9FF?style=flat-square&logo=github&logoColor=white"></a></div>
<!-- GLITCHBYTE-UPLOAD-DOOR:END -->

# RosieRiot Overdrive patches

- PATH: missing optional tools are skipped rather than crashing the launcher.
- Low bandwidth: default subprocess timeout 55 seconds (maximum 85 seconds).
- Nuclei: available only by explicit `--modules nuclei` selection and optional upstream install.
- Aquatone: browser screenshot stage is optional; verify an available browser and upstream aquatone binary.
- Safety: `--live` must be accompanied by `--authorized` and is scoped to the requested domain.
- Outputs: timestamped report folders avoid overwriting previous reports.
