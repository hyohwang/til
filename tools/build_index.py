"""README の目次（分野ごとの一覧）を作り直す。commit の前に自動で動く。

分野＝一番上のフォルダ（templates・tools などを除く）。題＝各ファイルの最初の見出し。
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP = {"templates", "tools"}
START, END = "<!-- index:start -->", "<!-- index:end -->"


def title_of(path):
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


def main():
    dirs = sorted(d for d in ROOT.iterdir()
                  if d.is_dir() and not d.name.startswith(".") and d.name not in SKIP)
    lines, total = [], 0
    for d in dirs:
        files = sorted(d.rglob("*.md"))
        if not files:
            continue
        total += len(files)
        lines.append(f"\n### {d.name}（{len(files)}）\n")
        lines += [f"- [{title_of(f)}]({f.relative_to(ROOT).as_posix()})" for f in files]
    body = f"{START}\n件数：{total}\n" + "\n".join(lines) + f"\n{END}"

    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    head, rest = text.split(START, 1)
    new = head + body + rest.split(END, 1)[1]
    if new != text:
        readme.write_text(new, encoding="utf-8")


if __name__ == "__main__":
    main()
