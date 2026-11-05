"""ひな形から、学んだことの要点を1つ作る。

python tools/new.py <分野> <題>
例：python tools/new.py git branch の使い方
"""
import datetime
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def slug(text):
    return re.sub(r"[\/:*?\"<>|\s]+", "-", text.strip()).strip("-").lower()


def main(args):
    if len(args) < 2:
        sys.exit(__doc__)
    title = " ".join(args[1:])
    path = ROOT / slug(args[0]) / f"{slug(title)}.md"
    if path.exists():
        print(f"もうあります：{path.relative_to(ROOT)}")
        return
    text = (ROOT / "templates" / "til.md").read_text(encoding="utf-8")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.format(title=title, date=datetime.date.today().isoformat()), encoding="utf-8")
    print(f"作りました：{path.relative_to(ROOT)}")


if __name__ == "__main__":
    main(sys.argv[1:])
