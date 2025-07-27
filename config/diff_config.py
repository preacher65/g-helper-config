import json
import sys
from pathlib import Path
from rich import print
from rich.console import Console
from rich.table import Table
import csv
import os

def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def compare_dicts(base, compare):
    diffs = []
    all_keys = sorted(set(base.keys()).union(set(compare.keys())))
    for key in all_keys:
        val1 = base.get(key, '<missing>')
        val2 = compare.get(key, '<missing>')
        if val1 != val2:
            diffs.append((key, val1, val2))
    return diffs

def save_markdown(diffs, file1, file2, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"# 🔍 G-Helper Config Diff Report\n\n")
        f.write(f"Comparing: `{file1}` vs `{file2}`\n\n")
        f.write("| Key | File 1 | File 2 |\n")
        f.write("|-----|--------|--------|\n")
        for key, v1, v2 in diffs:
            f.write(f"| `{key}` | `{v1}` | `{v2}` |\n")

def save_csv(diffs, output_path):
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Key", "File 1", "File 2"])
        for row in diffs:
            writer.writerow(row)

def main():
    if len(sys.argv) != 3:
        print("[red]Usage: python diff_config.py file1.json file2.json[/red]")
        sys.exit(1)

    file1, file2 = sys.argv[1], sys.argv[2]
    name1, name2 = Path(file1).stem, Path(file2).stem

    if not Path(file1).is_file() or not Path(file2).is_file():
        print(f"[red]One or both files not found: {file1}, {file2}[/red]")
        sys.exit(1)

    config1 = load_json(file1)
    config2 = load_json(file2)

    diffs = compare_dicts(config1, config2)

    if not diffs:
        print("[green]✅ No differences found[/green]")
        return

    # Display diff table in console
    table = Table(title="G-Helper config.json Differences")
    table.add_column("Key", style="bold cyan")
    table.add_column("File 1", style="dim")
    table.add_column("File 2", style="dim")
    for key, v1, v2 in diffs:
        table.add_row(key, str(v1), str(v2))
    console = Console()
    console.print(table)

    # Resolve project root relative to script location
    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent
    output_dir = project_root / "docs" / "diffs"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Save to markdown and CSV in output directory
    md_path = output_dir / f"{name1}_vs_{name2}.md"
    csv_path = output_dir / f"{name1}_vs_{name2}.csv"
    save_markdown(diffs, file1, file2, md_path)
    save_csv(diffs, csv_path)

    print(f"📄 Markdown saved to: [cyan]{md_path}[/cyan]")
    print(f"📊 CSV saved to: [cyan]{csv_path}[/cyan]")

if __name__ == "__main__":
    main()
