#!/usr/bin/env bash
set -u
printf '\033[95m◆ ROSIERIOT STACK VERIFICATION\033[0m\n'
for tool in python3 unzip go subfinder dnsx httpx naabu nuclei aquatone; do
  if command -v "$tool" >/dev/null 2>&1; then printf '\033[92m  ✓ %-12s %s\033[0m\n' "$tool" "$(command -v "$tool")"; else printf '\033[93m  ◇ %-12s missing (optional except python3)\033[0m\n' "$tool"; fi
done
printf 'Hint: run python3 rosieriot_overdrive.py --target example.com --demo --color always\n'
