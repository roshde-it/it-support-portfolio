# Log Scanner

Scan .log and .txt files in a folder for common error markers and produce a quick summary.

## Usage

```bash
python scan_logs.py --path "C:/Temp/logs"
```

Optional filters:

```bash
python scan_logs.py --path "C:/Temp/logs" --keywords ERROR WARNING FAIL
```

## Notes
- Reads files up to 5 MB to keep things snappy.
- Output is a simple summary you can paste into a ticket.