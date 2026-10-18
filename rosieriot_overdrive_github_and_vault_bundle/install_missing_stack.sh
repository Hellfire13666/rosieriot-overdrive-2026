#!/usr/bin/env bash
set -u
printf '\033[95m◆ ROSIERIOT OVERDRIVE INSTALLATION CHECK\033[0m\n'
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if ! command -v python3 >/dev/null 2>&1; then echo 'Python 3 is required: sudo apt install python3'; exit 1; fi
python3 -m py_compile "$ROOT/rosieriot_overdrive.py" || exit 1
printf '\033[92m✓ Python launcher verified. No third-party Python dependencies.\033[0m\n'
bash "$ROOT/verify_stack.sh"
cat <<'EOF'

Optional external tools are NOT automatically installed or modified.
For Go-based recon tools, see installers/OPTIONAL_TOOLS.md.
IMPORTANT: Some commands share names with other system utilities (notably httpx).
Try the offline demo before attempting authorized live assessments.
EOF
