# Optional stack setup (Ubuntu)

The Python launcher uses only the standard library and runs offline immediately.

The optional reconnaissance binaries are separate upstream tools. Install only what you need, after reviewing their official repositories and permissions. Typical Go installations:

```bash
sudo apt update
sudo apt install -y golang-go
mkdir -p "$HOME/go/bin"
# Review upstream projects before installing:
go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install github.com/projectdiscovery/dnsx/cmd/dnsx@latest
go install github.com/projectdiscovery/httpx/cmd/httpx@latest
go install github.com/projectdiscovery/naabu/v2/cmd/naabu@latest
go install github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
export PATH="$HOME/go/bin:$PATH"
```

Aquatone uses a browser and is optional; review the release at https://github.com/michenriksen/aquatone.

To retain Go tools on PATH for future shells, add `export PATH="$HOME/go/bin:$PATH"` to ~/.bashrc (only once).

On low bandwidth connections install one tool at a time. Per-module timeouts in RosieRiot prevent long hangs during a run.
