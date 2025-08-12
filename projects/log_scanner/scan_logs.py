import argparse
import os
from pathlib import Path

DEFAULT_KEYWORDS = ["ERROR", "WARNING", "FAIL", "EXCEPTION"]

def scan_file(path: Path, keywords):
    hits = {k: 0 for k in keywords}
    size_limit = 5 * 1024 * 1024  # 5 MB
    try:
        if path.stat().st_size > size_limit:
            return {"skipped": True, "reason": "too large", "hits": hits}

        with path.open("r", errors="ignore", encoding="utf-8") as f:
            for line in f:
                upper = line.upper()
                for k in keywords:
                    if k in upper:
                        hits[k] += 1
        return {"skipped": False, "hits": hits}
    except Exception as e:
        return {"skipped": True, "reason": str(e), "hits": hits}

def main():
    parser = argparse.ArgumentParser(description="Scan .log and .txt files for error markers")
    parser.add_argument("--path", required=True, help="Folder to scan")
    parser.add_argument("--keywords", nargs="*", default=DEFAULT_KEYWORDS, help="Keywords to search for")
    args = parser.parse_args()

    root = Path(args.path).expanduser().resolve()
    if not root.exists() or not root.is_dir():
        print(f"Path not found or not a directory: {root}")
        return

    files = [p for p in root.rglob("*") if p.suffix.lower() in {".log", ".txt"}]
    print(f"Found {len(files)} files")
    total = {k: 0 for k in args.keywords}

    for f in files:
        result = scan_file(f, args.keywords)
        if result["skipped"]:
            print(f"- {f.name}: skipped ({result.get('reason', 'n/a')})")
        else:
            counts = ", ".join([f"{k}:{v}" for k, v in result["hits"].items() if v > 0]) or "no hits"
            print(f"- {f.name}: {counts}")
            for k, v in result["hits"].items():
                total[k] += v

    print("
=== Summary ===")
    for k, v in total.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    main()