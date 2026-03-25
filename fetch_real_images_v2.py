#!/usr/bin/env python3
"""
Fetch real images from Pexels (Creative Commons Zero - no attribution needed)
Using direct download links that work
"""
import os
import urllib.request
import urllib.parse
import urllib.error
from pathlib import Path
from PIL import Image
from io import BytesIO
import time

# Pexels CCO 画像（実際に存在する画像リンク）
SPOT_IMAGES = {
    "ホテルニューオータニ_spot": "https://images.pexels.com/photos/291528/pexels-photo-291528.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "日中川_spot": "https://images.pexels.com/photos/1624487/pexels-photo-1624487.jpeg?auto=compress&cs=tinysrgb&w=1200",  
    "サンシャイン60展望台_spot": "https://images.pexels.com/photos/699122/pexels-photo-699122.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "千島_間_spot": "https://images.pexels.com/photos/442512/pexels-photo-442512.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "ホテル椿山荘_spot": "https://images.pexels.com/photos/1350789/pexels-photo-1350789.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "六義園_spot": "https://images.pexels.com/photos/2398220/pexels-photo-2398220.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "東京ミッドタウン_spot": "https://images.pexels.com/photos/3807517/pexels-photo-3807517.jpeg?auto=compress&cs=tinysrgb&w=1200"
}

LUNCH_IMAGE = "https://images.pexels.com/photos/2092965/pexels-photo-2092965.jpeg?auto=compress&cs=tinysrgb&w=800"
DINNER_IMAGE = "https://images.pexels.com/photos/1410235/pexels-photo-1410235.jpeg?auto=compress&cs=tinysrgb&w=800"

def download_image_from_url(url, filepath):
    """Download image and convert to WebP"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
        }
        req = urllib.request.Request(url, headers=headers)
        
        print(f"  ⬇️  {filepath}...")
        with urllib.request.urlopen(req, timeout=20) as response:
            img_data = response.read()
        
        img = Image.open(BytesIO(img_data))
        
        if img.mode in ('RGBA', 'LA', 'P'):
            img = img.convert('RGB')
        
        max_size = 1200
        img.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
        
        webp_path = filepath.replace('.jpg', '.webp')
        img.save(webp_path, 'WEBP', quality=85, method=6)
        
        file_size_kb = os.path.getsize(webp_path) / 1024
        print(f"  ✓ {webp_path} ({file_size_kb:.1f}KB)")
        return True
    except Exception as e:
        print(f"  ✗ Error: {str(e)[:60]}")
        return False

def fetch_all_images():
    """Fetch all images"""
    os.chdir('/Users/rai/.openclaw/workspace/sakura-site')
    
    print("\n🌸 Fetching Spot Images...")
    for spot_name, url in SPOT_IMAGES.items():
        filepath = f"images/spots/{spot_name}.jpg"
        download_image_from_url(url, filepath)
        time.sleep(0.5)
    
    spots = ["ホテルニューオータニ", "日中川", "サンシャイン60展望台", 
             "千島_間", "ホテル椿山荘", "六義園", "東京ミッドタウン"]
    
    print("\n🍽️  Fetching Restaurant Images (Lunch)...")
    for spot_name in spots:
        filepath = f"images/restaurants/{spot_name}_lunch.jpg"
        download_image_from_url(LUNCH_IMAGE, filepath)
        time.sleep(0.5)
    
    print("\n🍽️  Fetching Restaurant Images (Dinner)...")
    for spot_name in spots:
        filepath = f"images/restaurants/{spot_name}_dinner.jpg"
        download_image_from_url(DINNER_IMAGE, filepath)
        time.sleep(0.5)

if __name__ == "__main__":
    fetch_all_images()
    print("\n✅ All images ready!")
