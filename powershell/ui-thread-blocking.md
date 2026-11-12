# Don't run slow work on the UI thread

学んだ日：2026-11-11

## Key points (EN)
- A window (WinForms / WPF) is driven by a single **UI thread**.
- If slow work (sound playback, network, file I/O) runs on that thread, the window freezes and buttons like "Close" stop working.
- Run slow work in another thread or process.

## 要点（日本語）
- 画面（WinForms・WPF）は、1本の **UI スレッド** で動いている
- そのスレッドで時間のかかる処理（音の再生・通信・ファイル）をすると、処理が終わるまで画面が固まり、「閉じる」も効かなくなる
- 時間のかかる処理は、別のスレッドか別のプロセスで動かす

## つまずいた点
- 通知の画面で音を鳴らしたら、音の機器（ドライバー）の応答待ちで止まり、強制終了も効かなかった。音を別のプロセスで鳴らす形にして直した
