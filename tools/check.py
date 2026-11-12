"""commit の前に、会社・顧客の情報やキーが入っていないかを確かめる。

- 止める語の一覧（1行に1語。どのリポジトリにも入れない）。次の順に探す：
  1. 環境変数 BLOCKED_WORDS_FILE
  2. 会社の OneDrive の hr/05_career/github_blocked-words.txt
     （環境変数 OneDriveCommercial、または %USERPROFILE% の「OneDrive - 」で始まるフォルダ）
  見つからない（私用の PC）ときは、下の一般的な確認だけを行い、警告を出して止めない
- 決まった形：社内のIP、キーらしい文字列、パスワード
- commit に使うメールが GitHub の noreply のものか
見つかったら止める（終了コード 1）。
"""
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORDS_NAME = Path("hr") / "05_career" / "github_blocked-words.txt"
NOREPLY = re.compile(r"@users\.noreply\.github\.com$", re.I)
PATTERNS = {
    "社内のIP": re.compile(r"\b(?:10|192\.168|172\.(?:1[6-9]|2\d|3[01]))(?:\.\d{1,3}){2,3}\b"),
    "キー": re.compile(r"\b(?:sk-[A-Za-z0-9_-]{20,}|ghp_[A-Za-z0-9]{30,}|github_pat_\w{30,}|AKIA[0-9A-Z]{16})\b"),
    "パスワード": re.compile(r"(?i)\b(?:password|passwd|pwd)\s*[:=]\s*\S+"),
}


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True,
                          text=True, encoding="utf-8").stdout


def words_file():
    """止める語の一覧のファイルを探す。見つからなければ None"""
    if os.environ.get("BLOCKED_WORDS_FILE"):
        candidates = [Path(os.environ["BLOCKED_WORDS_FILE"])]
    else:
        candidates = []
        if os.environ.get("OneDriveCommercial"):
            candidates.append(Path(os.environ["OneDriveCommercial"]) / WORDS_NAME)
        home = Path(os.environ.get("USERPROFILE") or Path.home())
        candidates += sorted(d / WORDS_NAME for d in home.glob("OneDrive - *"))
    return next((p for p in candidates if p.is_file()), None)


def load_words(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    return [w.strip() for w in lines if w.strip() and not w.startswith("#")]


def word_pattern(word):
    # 大文字・数字だけの語（略称）は、大文字小文字を区別し、単語として一致したときだけ
    if re.fullmatch(r"[A-Z0-9]+", word):
        return re.compile(rf"(?<![A-Za-z0-9]){re.escape(word)}(?![A-Za-z0-9])")
    return re.compile(re.escape(word), re.I)


def main():
    problems = []
    email = git("config", "user.email").strip()
    if not NOREPLY.search(email):
        problems.append(f"commit のメールが GitHub の noreply ではありません（{email or 'なし'}）。"
                        "GitHub の noreply のメールを設定してください")

    path = words_file()
    words = load_words(path) if path else []
    if not path:
        print("警告：止める語の一覧が見つかりません。一般的な確認（IP・キー・パスワード・メール）だけを行います。"
              "仕事の内容は会社の PC で書いてください。", file=sys.stderr)

    checks = {**PATTERNS, **{f"止める語「{w}」": word_pattern(w) for w in words}}
    files = [f for f in git("diff", "--cached", "--name-only", "--diff-filter=ACMR").splitlines() if f]
    for name in files:
        text = git("show", f":{name}")
        for no, line in enumerate(text.splitlines(), 1):
            for label, pattern in checks.items():
                if pattern.search(line):
                    problems.append(f"{name}:{no}：{label}")

    if problems:
        print("commit を止めました。直してから、もう一度 commit してください。")
        print("\n".join(f"  - {p}" for p in problems))
        sys.exit(1)


if __name__ == "__main__":
    main()
