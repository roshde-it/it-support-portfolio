# Network Quick Check

A minimal script to help triage common connectivity problems.
- Checks DNS resolution for a few hosts
- Executes a system ping to test reachability
- Shows basic platform info

## Usage

```bash
python netcheck.py
```

You can also supply hosts to test:

```bash
python netcheck.py --hosts google.com cloudflare.com 8.8.8.8
```

## Sample Output PING SWEEP

```lua
ip,status
192.168.1.1,up
192.168.1.2,down
192.168.1.3,up
192.168.1.4,down
```


## Notes
- Uses the system `ping` command so it works without extra permissions.
- Output is plain text and safe to paste into tickets.
