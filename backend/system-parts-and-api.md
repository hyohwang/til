# Three parts of a system, and what an API is

学んだ日：2026-11-10

## Key points (EN)
- A system has three parts: **UI** (what users see), **processing**, and **storage**.
- The visible side is the **frontend**. The invisible side (processing + storage) is the **backend**. Both run on a **server**, which is a machine.
- An **API** is the agreed format of "orders and replies" between parts.
  - Request: destination (URL), purpose (GET / POST), content (JSON)
  - Response: status code + JSON

## 要点（日本語）
- システムは **画面・処理・保存** の3つの部品に分かれる
- 見える側が **フロントエンド**、見えない側（処理と保存）が **バックエンド**。どちらも **サーバー**（機械）の上で動く
- **API** は、部品どうしの「注文票と返事」の約束
  - 注文票（リクエスト）：宛先（URL）・用件（GET／POST）・内容（JSON）
  - 返事（レスポンス）：状態コードと JSON
- たとえ：画面＝客席、処理＝厨房、保存＝冷蔵庫。API は客席と厨房の間の注文票

## つまずいた点
- 「処理＝サーバー」と覚えていたが、不正確だった。サーバーは機械で、処理も保存もその上で動く

## 参考
- 次に学ぶこと：JSON の1つと、データベースの表の1行を並べて見る
