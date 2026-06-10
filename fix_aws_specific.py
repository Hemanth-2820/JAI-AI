import os
import json
import urllib.request
import urllib.parse
from PIL import Image, ImageEnhance

UNSPLASH_ACCESS_KEY = "tZmfx5hLOhrCv4-ArREaDiatzA21WBWviAlgKdu8SHk"

def main():
    out_dir = r"public\images\features"
    os.makedirs(out_dir, exist_ok=True)

    # Specific queries mapping for the 6 AWS DevOps features
    features_map = {
        "aws-devops-AWSCloudArchitecture": "cloud server architecture data center",
        "aws-devops-CI%2FCDPipelines": "software development coding computer screen",
        "aws-devops-CloudSecurityAuditing": "cyber security hacker lock digital",
        "aws-devops-Containerization(Docker%26K8s)": "shipping containers cargo port",
        "aws-devops-InfrastructureasCode": "matrix code binary screen tech",
        "aws-devops-PerformanceMonitoring": "stock market charts dashboard analytics"
    }

    success_count = 0
    for seed, query in features_map.items():
        url = f"https://api.unsplash.com/search/photos?query={urllib.parse.quote(query)}&per_page=1&orientation=landscape&client_id={UNSPLASH_ACCESS_KEY}"
        
        print(f"Fetching unique image for {seed} using query: {query}")
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

        photo_url = results[0]['urls']['regular']
        temp_path = f"temp_{seed}.jpg"
        
        try:
            urllib.request.urlretrieve(photo_url, temp_path)
            
            img = Image.open(temp_path).convert('RGB')
            img = img.resize((800, 600), Image.Resampling.LANCZOS)
            
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(0.8)
            
            out_path = os.path.join(out_dir, f"{seed}.jpg")
            img.save(out_path, quality=90)
            success_count += 1
            print(f"Fixed {seed}")
        except Exception as e:
            print(f"Error processing {seed}: {e}")
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)
                
    print(f"Successfully generated {success_count} unique and specifically-related feature images for AWS DevOps!")

if __name__ == "__main__":
    main()
