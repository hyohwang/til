# Share Git settings across PCs with dotfiles

学んだ日：2026-11-12

## Key points (EN)
- Put shared settings in a private **dotfiles** repository. On a new PC: clone it and run a setup script once.
- Use `includeIf` in the global Git config to switch name and email only under a folder (e.g. `C:/dev/`).
- The repository config (`.git/config`) is **not cloned**, so settings like `core.hooksPath` must be set again on each PC. The setup script does this.
- Never put secrets or sensitive word lists in the repository. Keep them in a separate, protected place.

## 要点（日本語）
- 複数の PC で同じ設定を使うには、非公開の **dotfiles**（設定ファイル群）のリポジトリに入れる。新しい PC では clone して、設定のスクリプトを1回実行する
- Git の全体の設定で `includeIf` を使うと、決まったフォルダの下だけ名前とメールを切り替えられる
- リポジトリごとの設定（`.git/config`）は clone では付いてこない。`core.hooksPath`（フック＝commit の前などに動くスクリプトを置くフォルダを指す設定）も、PC ごとに設定し直す。スクリプトで行う
- キーや、伏せたい言葉の一覧はリポジトリに入れない。別の守られた場所に置く

## 手順・コマンド
```powershell
git config --global "includeIf.gitdir/i:C:/dev/.path" C:/dev/dotfiles/gitconfig-personal
# 各リポジトリの中で実行する
git config core.hooksPath .githooks
```

## つまずいた点
- `git remote add origin` で `remote origin already exists` と出た → 送り先の登録が先に済んでいたための、害のないエラー。`git remote -v` で登録先が正しいかを確かめる
