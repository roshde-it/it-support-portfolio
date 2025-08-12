import argparse
import os
import shutil
from pathlib import Path

CATEGORIES = {
    "Images": {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff", ".webp"},
    "Documents": {".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".rtf"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "Audio": {".mp3", ".wav", ".aac", ".flac", ".ogg"},
    "Video": {".mp4", ".mov", ".avi", ".mkv"},
    "Code": {".py", ".js", ".json", ".html", ".css", ".ps1", ".bat", ".sh"},
    "Installers": {".exe", ".msi", ".pkg", ".dmg"}
}

def categorize(ext):
    for name, exts in CATEGORIES.items():
        if ext.lower() in exts:
            return name
    return "Other"

def organise(path: Path, dry_run: bool):
    moved = []
    for item in path.iterdir():
        if item.is_file():
            category = categorize(item.suffix)
            dest_dir = path / category
            dest_dir.mkdir(exist_ok=True)
            dest = dest_dir / item.name
            if dry_run:
                moved.append((str(item), str(dest)))
            else:
                shutil.move(str(item), str(dest))
                moved.append((str(item), str(dest)))
    return moved

def main():
    parser = argparse.ArgumentParser(description="Organise files in a folder by extension category")
    parser.add_argument("--path", required=True, help="Folder to organise")
    parser.add_argument("--dry-run", action="store_true", help="Show what would happen without moving files")
    args = parser.parse_args()

    target = Path(args.path).expanduser().resolve()
    if not target.exists() or not target.is_dir():
        print(f"Path not found or not a directory: {target}")
        return

    moves = organise(target, args.dry_run)
    if args.dry_run:
        print("Dry run - no files moved.")
    print(f"Items processed: {len(moves)}")
    for src, dst in moves[:30]:
        print(f"{src} -> {dst}")
    if len(moves) > 30:
        print("...")

if __name__ == "__main__":
    main()