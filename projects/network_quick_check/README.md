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

## Notes
- Uses the system `ping` command so it works without extra permissions.
- Output is plain text and safe to paste into tickets.