#!/usr/bin/env python3
"""
Fetch real images from Unsplash API (free, no API key required for basic usage)
"""
import os
import json
import urllib.request
import urllib.parse
import urllib.error
from pathlib import Path
from PIL import Image
from io import BytesIO
import time

# Unsplash API (API key-free endpoint)
# 実際にはスクリーンショット + Web scraping で取得することもできるが、
# ここでは Unsplash の公開検索 URL から直接ダウンロード可能な画像を取得

SPOT_IMAGES = {
    "ホテルニューオータニ_spot": {
        "search": "hotel sakura cherry blossom garden",
        "unsplash": "https://images.unsplash.com/photo-1520763185298-1b434c919abe?w=1200&q=80"  # Cherry blossoms
    },
    "日中川_spot": {
        "search": "river sakura at night",
        "unsplash": "https://images.unsplash.com/photo-1557672172-298e090d0f80?w=1200&q=80"  # Night sakura
    },
    "サンシャイン60展望台_spot": {
        "search": "night city view observation deck",
        "unsplash": "https://images.unsplash.com/photo-1551799812-65b9e20df3a3?w=1200&q=80"  # Night cityscape
    },
    "千島_間_spot": {
        "search": "edo garden cherry blossom",
        "unsplash": "https://images.unsplash.com/photo-1585518419759-eec4addf0f39?w=1200&q=80"  # Garden path
    },
    "ホテル椿山荘_spot": {
        "search": "luxury hotel garden illuminated night",
        "unsplash": "https://images.unsplash.com/photo-1522159060908-ab5c1a3654c0?w=1200&q=80"  # Hotel garden at night
    },
    "六義園_spot": {
        "search": "japanese traditional garden landscape",
        "unsplash": "https://images.unsplash.com/photo-1522159060908-ab5c1a3654c0?w=1200&q=80"  # Japanese garden
    },
    "東京ミッドタウン_spot": {
        "search": "modern garden landscape roppongi",
        "unsplash": "https://images.unsplash.com/photo-1585518419759-eec4addf0f39?w=1200&q=80"  # Modern landscape
    }
}

RESTAURANT_IMAGES = {
    "lunch": {
        "search": "restaurant lunch meal presentation",
        "unsplash": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=800&q=80"  # Japanese cuisine
    },
    "dinner": {
        "search": "fine dining restaurant elegant dinner",
        "unsplash": "https://images.unsplash.com/photo-1504674900967-5f25f26b2e4f?w=800&q=80"  # Elegant dinner
    }
}

def download_image_from_url(url, filepath):
    """Download image and convert to WebP"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }
        req = urllib.request.Request(url, headers=headers)
        
        print(f"  Downloading: {url[:60]}...")
        with urllib.request.urlopen(req, timeout=15) as response:
            img_data = response.read()
        
        # Convert to WebP
        img = Image.open(BytesIO(img_data))
        
        # Ensure RGB
        if img.mode in ('RGBA', 'LA', 'P'):
            img = img.convert('RGB')
        
        # Optimize size
        max_size = 1200
        img.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
        
        # Save as WebP
        webp_path = filepath.replace('.jpg', '.webp')
        img.save(webp_path, 'WEBP', quality=80, method=6)
        
        file_size_kb = os.path.getsize(webp_path) / 1024
        print(f"  ✓ Saved: {webp_path} ({file_size_kb:.1f}KB)")
        return True
    except Exception as e:
        print(f"  ✗ Failed: {str(e)[:80]}")
        return False

def fetch_all_images():
    """Fetch all spot and restaurant images"""
    os.chdir('/Users/rai/.openclaw/workspace/sakura-site')
    
    # Spot images
    print("\n📸 Fetching spot images...")
    for spot_name, urls in SPOT_IMAGES.items():
        filepath = f"images/spots/{spot_name}.webp"
        download_image_from_url(urls["unsplash"], filepath)
        time.sleep(1)  # Rate limiting
    
    # Restaurant images
    print("\n🍽️ Fetching restaurant images...")
    for meal_type in ["lunch", "dinner"]:
        for spot_name in ["ホテルニューオータニ", "日中川", "サンシャイン60展望台", 
                          "千島_間", "ホテル椿山荘", "六義園", "東京ミッドタウン"]:
            filepath = f"images/restaurants/{spot_name}_{meal_type}.webp"
            
            # Use different URLs for lunch/dinner
            if meal_type == "lunch":
                url = RESTAURANT_IMAGES["lunch"]["unsplash"]
            else:
                url = RESTAURANT_IMAGES["dinner"]["unsplash"]
            
            download_image_from_url(url, filepath)
            time.sleep(0.5)

if __name__ == "__main__":
    fetch_all_images()
    print("\n✅ Image fetching complete!")
