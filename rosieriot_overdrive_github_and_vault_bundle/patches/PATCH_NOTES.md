# RosieRiot Overdrive patches

- PATH: missing optional tools are skipped rather than crashing the launcher.
- Low bandwidth: default subprocess timeout 55 seconds (maximum 85 seconds).
- Nuclei: available only by explicit `--modules nuclei` selection and optional upstream install.
- Aquatone: browser screenshot stage is optional; verify an available browser and upstream aquatone binary.
- Safety: `--live` must be accompanied by `--authorized` and is scoped to the requested domain.
- Outputs: timestamped report folders avoid overwriting previous reports.
