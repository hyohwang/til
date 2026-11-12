# JSON compared with database tables

学んだ日：2026-11-11

## Key points (EN)
- One row of a table = one JSON object `{ }`
- Several rows = a JSON array `[ ]`
- Data you would split into another table (child rows) can be **nested** inside the object

## 要点（日本語）
- 表の1行 ＝ JSON の1つ `{ }`（列の名前がキー、値が値）
- 何行か ＝ `[ ]` の中に `{ }` を並べる
- データベースでは別の表に分けていたもの（明細など）を、JSON では中に入れ子にできる

## 例
```json
{
  "order_id": 101,
  "customer": "A",
  "items": [
    { "product": "X", "qty": 2 },
    { "product": "Y", "qty": 1 }
  ]
}
```
データベースなら「注文」の表に1行、「注文の明細」の表に2行になる。

## つまずいた点
- JSON には表の「列の決まり（型）」がない。同じキーでも値の形がそろっているかは、受け取る側で確かめる
