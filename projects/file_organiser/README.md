# File Organiser

Moves files in a target folder into subfolders by extension. Helps tidy user Downloads before backups or migrations.

## Usage

Dry run first:

```bash
python organise_downloads.py --path "C:/Users/Name/Downloads" --dry-run
```

Then apply:

```bash
python organise_downloads.py --path "C:/Users/Name/Downloads"
```

## Notes
- Only moves files in the top level of the target folder.
- Creates subfolders like `Documents`, `Images`, `Archives`, etc.
- Safe to cancel and rerun.