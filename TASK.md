# 3/29 花見デート サイト全面リニューアル

## 現状
- 7 つの花見スポット確定（spots.json に記載）
  1. ホテルニューオータニ（紀尾井町）
  2. 日中川（目黒・渋谷区）
  3. サンシャイン60展望台（池袋）
  4. 千島・間（千代田区）
  5. ホテル椿山荘（江戸川橋）
  6. 六義園（駒込）
  7. 東京ミッドタウン（六本木）

## やること

### 1. 各スポット周辺の実際の飲食店を調査・記録
- 各スポット × 2 店 = 14 店舗（昼食・夜食）
- Google Maps / Tabelog / 公式サイト情報
- 店名、住所、電話、営業時間、予算、URL を記録

### 2. restaurants.json を作成
```json
{
  "restaurants": [
    {
      "id": 1,
      "spotId": 1,
      "mealType": "lunch",
      "name": "店名",
      "address": "住所",
      "phone": "電話番号",
      "hours": "営業時間",
      "budget": "予算目安（例：1500-2500円）",
      "mapsUrl": "Google Maps URL",
      "websiteUrl": "公式サイト（あれば）",
      "reservation": "要予約 or 不要",
      "imageUrls": ["実際の写真 URL"]
    }
  ]
}
```

### 3. スポット情報に restaurants 情報を統合
- restaurants.json を data/ に保存
- spots.json の restaurants フィールドを参照形式に更新

### 4. index.html を更新
- 各スケジュール・カードに昼食・夜食の店情報 + 画像を表示
- 店名、予算、営業時間、リンク、画像を盛り込む
- レスポンシブ（スマホ対応）

### 5. git commit + push

## 重要
- 実在する店舗・実際の情報のみを使用
- Google Maps から実際の店舗画像を活用
- 予約必須の店は「要予約」と明示
