import re

def main():
    file_path = r'src\pages\Services\categoryData.js'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # We need to parse by category and replace the whyUs image.
    # We can split the content by '": {\n    "title": "' to identify categories.
    # Alternatively, a simple regex replacement function.
    
    # Let's find all category blocks:
    blocks = re.split(r'(\n  "[a-z0-9\-]+": {\n    "title":)', content)
    
    new_content = blocks[0]
    
    for i in range(1, len(blocks), 2):
        header = blocks[i]
        body = blocks[i+1]
        
        # Extract the first feature image
        feature_img_match = re.search(r'"image":\s*"(/images/features/[^"]+\.jpg)"', body)
        if feature_img_match:
            first_feature_image = feature_img_match.group(1)
            
            # Replace the whyUs image
            # Look for the whyUs section and its image
            # We'll just replace the first instance of "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?q=80&w=800&auto=format&fit=crop"
            # specifically in this block.
            body = body.replace(
                '"https://images.unsplash.com/photo-1517694712202-14dd9538aa97?q=80&w=800&auto=format&fit=crop"',
                f'"{first_feature_image}"',
                1
            )
            
        new_content += header + body
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("Successfully mapped specific feature images to the Why Us section for all categories!")

if __name__ == "__main__":
    main()
