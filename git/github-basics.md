# Git・GitHub の基本

学んだ日：2026-11-04

## 要点
- リポジトリ：記録を残す単位（フォルダ1つ分）
- commit：変更を説明つきで手元に記録する。push：GitHub に送る。pull：GitHub から取り込む
- branch：本線を変えずに別の線で試す。Pull Request：branch の変更を本線に入れる前に確認する場所
- `.gitignore`：記録させないファイル（キー・パスワード・手元だけのもの）

## 手順・コマンド
```bash
git status                  # 何が変わったか
git diff                    # 変えた中身
git add .                   # commit に含める
git commit -m "何をしたか"   # 手元に記録
git push                    # GitHub に送る
git switch -c 試したいこと   # branch を作って移る
git log --oneline           # 記録の一覧
```

## つまずいた点
- commit に使うメールは公開される。個人の記録には GitHub の noreply のメール（`<番号>+<ユーザー名>@users.noreply.github.com`）を使う
- push の前に `git status` と `git diff` で、送る中身を確かめる

## 参考
- GitHub Docs「Setting your commit email address」
