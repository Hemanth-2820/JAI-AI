import os
import re
import random
import hashlib

os.makedirs(r'public\images\animated', exist_ok=True)

file_path = r'src\pages\Services\categoryData.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# We need to find all extendedCapabilities objects
# We can use regex to find blocks, or better, we can parse it carefully.
# Let's extract all capability titles and generate a unique SVG for each.
# We will use the capability's "title" to determine the slug.

def slugify(text):
    text = text.lower()
    return re.sub(r'[^a-z0-9]+', '-', text).strip('-')

# The patterns available
def gen_nodes(seed_num, w=800, h=600):
    random.seed(seed_num)
    svg = f'<svg width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="#0E1F1A" />'
    num_nodes = random.randint(8, 15)
    nodes = [(random.randint(50, w-50), random.randint(50, h-50)) for _ in range(num_nodes)]
    
    # Draw lines
    svg += '<g stroke="rgba(226, 250, 113, 0.2)" stroke-width="2">'
    for i in range(num_nodes):
        for j in range(i+1, min(i+4, num_nodes)):
            if random.random() > 0.3:
                svg += f'<line x1="{nodes[i][0]}" y1="{nodes[i][1]}" x2="{nodes[j][0]}" y2="{nodes[j][1]}" />'
    svg += '</g>'
    
    # Draw glowing circles
    for x, y in nodes:
        r = random.randint(5, 15)
        dur = round(random.uniform(2.0, 5.0), 1)
        delay = round(random.uniform(0.0, 2.0), 1)
        color = random.choice(["#E2FA71", "#FFFFFF", "#114051", "#B48366"])
        svg += f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}">'
        svg += f'<animate attributeName="r" values="{r};{r+10};{r}" dur="{dur}s" begin="{delay}s" repeatCount="indefinite" />'
        svg += f'<animate attributeName="opacity" values="0.5;1;0.5" dur="{dur}s" begin="{delay}s" repeatCount="indefinite" />'
        svg += '</circle>'
    svg += '</svg>'
    return svg

def gen_waves(seed_num, w=800, h=600):
    random.seed(seed_num)
    svg = f'<svg width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="#0E1F1A" />'
    num_waves = random.randint(4, 8)
    for i in range(num_waves):
        y_offset = random.randint(100, 500)
        dur = round(random.uniform(3.0, 8.0), 1)
        amp = random.randint(30, 100)
        color = random.choice(["rgba(226, 250, 113, 0.4)", "rgba(17, 64, 81, 0.8)", "rgba(255, 255, 255, 0.3)"])
        
        path1 = f"M 0 {y_offset} Q 200 {y_offset-amp} 400 {y_offset} T 800 {y_offset}"
        path2 = f"M 0 {y_offset} Q 200 {y_offset+amp} 400 {y_offset} T 800 {y_offset}"
        
        svg += f'<path d="{path1}" fill="none" stroke="{color}" stroke-width="{random.randint(2,6)}">'
        svg += f'<animate attributeName="d" values="{path1};{path2};{path1}" dur="{dur}s" repeatCount="indefinite" />'
        svg += '</path>'
    svg += '</svg>'
    return svg

def gen_data_blocks(seed_num, w=800, h=600):
    random.seed(seed_num)
    svg = f'<svg width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="#1A3129" />'
    num_blocks = random.randint(10, 25)
    for i in range(num_blocks):
        x = random.randint(0, w)
        width = random.randint(10, 80)
        height = random.randint(20, 150)
        dur = round(random.uniform(2.0, 7.0), 1)
        delay = round(random.uniform(0.0, 5.0), 1)
        color = random.choice(["#E2FA71", "#FFFFFF", "#114051"])
        op = round(random.uniform(0.2, 0.8), 2)
        
        svg += f'<rect x="{x}" y="-200" width="{width}" height="{height}" fill="{color}" opacity="{op}">'
        svg += f'<animate attributeName="y" values="-200;{h+200}" dur="{dur}s" begin="{delay}s" repeatCount="indefinite" />'
        svg += '</rect>'
    svg += '</svg>'
    return svg

def gen_radar(seed_num, w=800, h=600):
    random.seed(seed_num)
    svg = f'<svg width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="#0E1F1A" />'
    num_rings = random.randint(4, 9)
    cx, cy = w//2, h//2
    for i in range(num_rings):
        r = random.randint(50, 400)
        dur = round(random.uniform(4.0, 12.0), 1)
        color = random.choice(["#E2FA71", "#114051", "#FFFFFF"])
        width = random.randint(1, 4)
        dash = f"{random.randint(5, 50)} {random.randint(10, 50)}"
        svg += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{color}" stroke-width="{width}" stroke-dasharray="{dash}">'
        svg += f'<animateTransform attributeName="transform" type="rotate" from="0 {cx} {cy}" to="{random.choice([360, -360])} {cx} {cy}" dur="{dur}s" repeatCount="indefinite" />'
        svg += '</circle>'
    svg += '</svg>'
    return svg

generators = [gen_nodes, gen_waves, gen_data_blocks, gen_radar]

def replace_cap_image(match):
    title = match.group(1)
    slug = slugify(title)
    
    # Hash the title to create a deterministic seed
    seed = int(hashlib.md5(title.encode()).hexdigest(), 16)
    random.seed(seed)
    
    # Pick a generator
    generator = random.choice(generators)
    svg_data = generator(seed)
    
    # Save SVG
    filename = f"{slug}.svg"
    with open(f"public\\images\\animated\\{filename}", "w", encoding="utf-8") as svg_file:
        svg_file.write(svg_data)
    
    # Replace the image field in the JSON block
    # match.group(0) is the entire object up to the "image" field.
    # We reconstruct it with the new image URL.
    return match.group(0).replace(match.group(2), f'"{slug}.svg"')

# Find blocks like "title": "...", ... "image": "..."
# We need a regex that grabs title, then anything until image.
pattern = r'"title":\s*"([^"]+)".*?"image":\s*"/images/animated/([^"]+)"'
# Wait! We need to make sure we only replace within extendedCapabilities.
# Actually, if we just find all occurrences of "title" followed by "image" that use animated svgs, we can replace them.
# The previous script set all images inside extendedCapabilities to "/images/animated/..."
# So this regex will perfectly isolate the ones we just added!

def global_replacer(match):
    title = match.group(1)
    slug = slugify(title)
    seed = int(hashlib.md5(title.encode()).hexdigest(), 16)
    random.seed(seed)
    generator = random.choice(generators)
    svg_data = generator(seed)
    filename = f"{slug}.svg"
    with open(f"public\\images\\animated\\{filename}", "w", encoding="utf-8") as svg_file:
        svg_file.write(svg_data)
    return f'"title": "{title}"' + match.group(0)[len(f'"title": "{title}"'):-len(match.group(2))-1] + f'{filename}"'

# re.DOTALL to allow matching across newlines between title and image
new_content = re.sub(r'"title":\s*"([^"]+)".*?"image":\s*"/images/animated/([^"]+)"', global_replacer, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Generated 100% unique animated SVGs based on titles!")
