import re

css_path = r'src\pages\Services\Services.module.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# I will update the superHeroImageWrapper and superHeroContent widths to give text more room,
# and reduce the image height to make it less overwhelming.

# 1. Update text content width
css = re.sub(r'(\.superHeroContent\s*\{[^}]*width:\s*)50%', r'\g<1>55%', css)

# 2. Update wrapper width and height
css = re.sub(r'(\.superHeroImageWrapper\s*\{[^}]*width:\s*)50%', r'\g<1>45%', css)
css = re.sub(r'(\.superHeroImageWrapper\s*\{[^}]*height:\s*)70%', r'\g<1>60%', css)

# 3. Scale down the image itself inside the wrapper
css = re.sub(r'(\.superHeroImg\s*\{[^}]*width:\s*)100%', r'\g<1>80%', css)
css = re.sub(r'(\.superHeroImg\s*\{[^}]*height:\s*)100%', r'\g<1>80%', css)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Reduced Hero Image size and adjusted text width!")
