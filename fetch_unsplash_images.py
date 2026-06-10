import re
import os
import json
import urllib.request
import urllib.parse
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import textwrap

UNSPLASH_ACCESS_KEY = "tZmfx5hLOhrCv4-ArREaDiatzA21WBWviAlgKdu8SHk"

def split_camel_case(s):
    return re.sub(r'([a-z0-9])([A-Z])', r'\1 \2', s)

def main():
    out_dir = r"public\images\features"
    os.makedirs(out_dir, exist_ok=True)

    font_path = r"C:\Windows\Fonts\arialbd.ttf"
    try:
        font_title = ImageFont.truetype(font_path, 48)
        font_sub = ImageFont.truetype(font_path, 24)
    except:
        font_title = ImageFont.load_default()
        font_sub = ImageFont.load_default()

    # Parse seeds
    with open(r'src\pages\Services\categoryData.js', 'r', encoding='utf-8') as f:
        content = f.read()
    matches = re.finditer(r'\"image\":\s*\"/images/features/([^\.]+)\.jpg\"', content)
    seeds = sorted(list(set([m.group(1) for m in matches])))
    
    # Group by category
    categories = {}
    for seed in seeds:
        parts = seed.split('-', 2)
        if len(parts) >= 2:
            cat_key = f"{parts[0]}-{parts[1]}"
            feature = parts[-1]
        else:
            cat_key = parts[0]
            feature = "-".join(parts[1:])
            
        if cat_key not in categories:
            categories[cat_key] = []
        categories[cat_key].append((seed, feature))

    print(f"Grouped into {len(categories)} categories. This will use only {len(categories)} API requests out of your 50 limit!")

    success_count = 0

    for cat_key, features in categories.items():
        # Search Unsplash for this category
        query = cat_key.replace('-', ' ')
        num_requested = len(features)
        url = f"https://api.unsplash.com/search/photos?query={urllib.parse.quote(query)}&per_page={num_requested}&orientation=landscape&client_id={UNSPLASH_ACCESS_KEY}"
        
        print(f"Fetching {num_requested} unique images for {query}...")
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            response = urllib.request.urlopen(req)
            data = json.loads(response.read())
            results = data.get('results', [])
        except Exception as e:
            print(f"Failed to fetch for {query}: {e}")
            continue
            
        if not results:
            print(f"No results for {query}")
            continue

        # Assign unique images to features
        for i, (seed, feature) in enumerate(features):
            photo_url = results[i % len(results)]['urls']['regular']
            
            # Download image
            temp_path = f"temp_{seed}.jpg"
            try:
                urllib.request.urlretrieve(photo_url, temp_path)
            except Exception as e:
                print(f"Failed to download image for {seed}: {e}")
                continue

            # Process image
            try:
                img = Image.open(temp_path).convert('RGB')
                img = img.resize((800, 600), Image.Resampling.LANCZOS)
                
                # Darken slightly to keep white text readable but keep image bright
                # 0.8 means it retains 80% of its original brightness
                enhancer = ImageEnhance.Brightness(img)
                img = enhancer.enhance(0.8)
                
                out_path = os.path.join(out_dir, f"{seed}.jpg")
                img.save(out_path, quality=90)
                success_count += 1
                
            except Exception as e:
                print(f"Error processing {seed}: {e}")
            finally:
                if os.path.exists(temp_path):
                    os.remove(temp_path)
                    
    print(f"Successfully generated {success_count} absolutely unique feature images using Unsplash!")

if __name__ == "__main__":
    main()
