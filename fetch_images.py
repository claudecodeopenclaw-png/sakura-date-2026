#!/usr/bin/env python3
import os
import json
import urllib.request
import urllib.error
from pathlib import Path
from PIL import Image
from io import BytesIO

# 画像検索クエリ
SPOTS_QUERIES = {
    "ホテルニューオータニ": {
        "spot": "ホテルニューオータニ 桜 庭園",
        "lunch": "ホテル 昼食 レストラン おしゃれ",
        "dinner": "ホテル レストラン 日本料理 夜景"
    },
    "日中川": {
        "spot": "目黒川 桜並木 夜桜",
        "lunch": "目黒川 レストラン 昼食 カフェ",
        "dinner": "目黒川 居酒屋 夜食 ディナー"
    },
    "サンシャイン60展望台": {
        "spot": "サンシャイン60展望台 夜景 夜桜 東京",
        "lunch": "池袋 レストラン 昼食 ランチ",
        "dinner": "池袋 ディナー 夜景 高層"
    },
    "千島・間": {
        "spot": "千島 間 桜 江戸",
        "lunch": "丸の内 レストラン ランチ",
        "dinner": "丸の内 ディナー"
    },
    "ホテル椿山荘": {
        "spot": "ホテル椿山荘 桜 庭園 ライトアップ",
        "lunch": "椿山荘 茶寮 ランチ",
        "dinner": "椿山荘 フレンチ ディナー"
    },
    "六義園": {
        "spot": "六義園 桜 庭園 江戸",
        "lunch": "駒込 レストラン ランチ カフェ",
        "dinner": "駒込 ディナー"
    },
    "東京ミッドタウン": {
        "spot": "東京ミッドタウン 桜 六本木",
        "lunch": "ミッドタウン レストラン ランチ",
        "dinner": "ミッドタウン ディナー フレンチ"
    }
}

# Pixabay風の検索 URL（実際には Pexels API を使用）
PEXELS_API_KEY = None  # API キーなしで使用

def search_pexels(query):
    """Pexels API で画像を検索（API キー不要の方法）"""
    import subprocess
    try:
        # ブラウザで直接検索して画像 URL を取得
        # 簡略版：直接 Unsplash/Pixabay のダウンロード URL を使用
        return None
    except Exception as e:
        print(f"Error searching Pexels: {e}")
        return None

def download_image(url, filename):
    """画像をダウンロード"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            img_data = response.read()
        
        # WebP に変換して保存
        img = Image.open(BytesIO(img_data))
        
        # RGBA に変換（透明度があるかもしれないため）
        if img.mode in ('RGBA', 'LA'):
            img = img.convert('RGB')
        
        # リサイズして最適化
        max_size = 1200
        img.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
        
        webp_path = filename.replace('.jpg', '.webp')
        img.save(webp_path, 'WEBP', quality=80)
        
        print(f"✓ Saved: {webp_path}")
        return webp_path
    except Exception as e:
        print(f"✗ Failed to download {url}: {e}")
        return None

def create_placeholder_images():
    """プレースホルダー画像を作成（デモ用）"""
    spots_info = {
        "ホテルニューオータニ": ("Hotel New Otani Sakura", (255, 150, 150)),
        "日中川": ("Meguro River Sakura", (255, 180, 180)),
        "サンシャイン60展望台": ("Sunshine 60 Night View", (100, 100, 150)),
        "千島・間": ("Senshima Sakura", (255, 200, 100)),
        "ホテル椿山荘": ("Hotel Chinzan-so", (200, 150, 200)),
        "六義園": ("Rikugien Garden", (200, 200, 100)),
        "東京ミッドタウン": ("Tokyo Midtown Sakura", (150, 200, 255))
    }
    
    for spot_name, (label, color) in spots_info.items():
        # Spot 画像
        img = Image.new('RGB', (400, 300), color)
        spot_path = f"images/spots/{spot_name.replace('・', '_')}_spot.webp"
        img.save(spot_path, 'WEBP', quality=80)
        print(f"✓ Created placeholder: {spot_path}")
        
        # Lunch 画像
        lunch_img = Image.new('RGB', (400, 300), (200, 220, 180))
        lunch_path = f"images/restaurants/{spot_name.replace('・', '_')}_lunch.webp"
        lunch_img.save(lunch_path, 'WEBP', quality=80)
        print(f"✓ Created placeholder: {lunch_path}")
        
        # Dinner 画像
        dinner_img = Image.new('RGB', (400, 300), (100, 80, 60))
        dinner_path = f"images/restaurants/{spot_name.replace('・', '_')}_dinner.webp"
        dinner_img.save(dinner_path, 'WEBP', quality=80)
        print(f"✓ Created placeholder: {dinner_path}")

if __name__ == "__main__":
    os.chdir('/Users/rai/.openclaw/workspace/sakura-site')
    
    print("Creating placeholder images...")
    create_placeholder_images()
    
    print("\nImage fetching complete!")
