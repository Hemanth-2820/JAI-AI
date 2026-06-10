import re
import os
import json
import urllib.request
import urllib.parse
from PIL import Image, ImageEnhance

UNSPLASH_ACCESS_KEY = "tZmfx5hLOhrCv4-ArREaDiatzA21WBWviAlgKdu8SHk"

def main():
    out_dir = r"public\images\features"
    os.makedirs(out_dir, exist_ok=True)

    # Parse seeds for aws-devops
    with open(r'src\pages\Services\categoryData.js', 'r', encoding='utf-8') as f:
        content = f.read()
    matches = re.finditer(r'\"image\":\s*\"/images/features/([^\.]+)\.jpg\"', content)
    seeds = sorted(list(set([m.group(1) for m in matches])))
    
    features = []
    for seed in seeds:
        if seed.startswith("aws-devops-"):
            features.append((seed, seed.replace("aws-devops-", "")))

    num_requested = len(features)
    # Use a generic query that Unsplash has lots of photos for
    query = "datacenter server cloud"
    url = f"https://api.unsplash.com/search/photos?query={urllib.parse.quote(query)}&per_page={num_requested}&orientation=landscape&client_id={UNSPLASH_ACCESS_KEY}"
    
    print(f"Fetching {num_requested} unique images for {query}...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        data = json.loads(response.read())
        results = data.get('results', [])
    except Exception as e:
        print(f"Failed to fetch for {query}: {e}")
        return
        
    if not results:
        print(f"No results for {query}")
        return

    success_count = 0
    for i, (seed, feature) in enumerate(features):
        photo_url = results[i % len(results)]['urls']['regular']
        
        temp_path = f"temp_{seed}.jpg"
        try:
            urllib.request.urlretrieve(photo_url, temp_path)
            
            img = Image.open(temp_path).convert('RGB')
            img = img.resize((800, 600), Image.Resampling.LANCZOS)
            
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(0.8) # Vibrant bright
            
            out_path = os.path.join(out_dir, f"{seed}.jpg")
            img.save(out_path, quality=90)
            success_count += 1
            print(f"Fixed {seed}")
        except Exception as e:
            print(f"Error processing {seed}: {e}")
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)
                
    print(f"Successfully generated {success_count} unique feature images for AWS DevOps!")

if __name__ == "__main__":
    main()
