import os
import re
import random
import hashlib

os.makedirs(r'public\images\animated', exist_ok=True)

file_path = r'src\pages\Services\categoryData.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

def slugify(text):
    text = text.lower()
    return re.sub(r'[^a-z0-9]+', '-', text).strip('-')

# Unified generator that guarantees uniqueness by embedding the title
def gen_bespoke_svg(title, seed_num, w=800, h=600):
    random.seed(seed_num)
    
    # Randomly select a dark background color from the palette
    bg_colors = ["#0E1F1A", "#114051", "#1A3129", "#000000"]
    bg_color = random.choice(bg_colors)
    
    svg = f'<svg width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="{bg_color}" />'
    
    # 1. Base geometric background layer (completely chaotic math)
    num_shapes = random.randint(5, 15)
    for _ in range(num_shapes):
        shape_type = random.choice(['circle', 'rect', 'path'])
        color = random.choice(["#E2FA71", "#B48366", "#C3DBE3", "#DDE2CD", "#FFFFFF"])
        op = round(random.uniform(0.05, 0.3), 2)
        dur = round(random.uniform(3.0, 10.0), 1)
        
        x = random.randint(-100, w)
        y = random.randint(-100, h)
        
        if shape_type == 'circle':
            r = random.randint(20, 200)
            svg += f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}" opacity="{op}">'
            svg += f'<animate attributeName="r" values="{r};{r*1.5};{r}" dur="{dur}s" repeatCount="indefinite" />'
            svg += '</circle>'
        elif shape_type == 'rect':
            rw = random.randint(50, 300)
            rh = random.randint(50, 300)
            svg += f'<rect x="{x}" y="{y}" width="{rw}" height="{rh}" fill="{color}" opacity="{op}">'
            svg += f'<animateTransform attributeName="transform" type="rotate" from="0 {x+rw//2} {y+rh//2}" to="360 {x+rw//2} {y+rh//2}" dur="{dur*2}s" repeatCount="indefinite" />'
            svg += '</rect>'
        else:
            path_d = f"M {x} {y} Q {x+random.randint(50, 200)} {y-random.randint(50, 200)} {x+random.randint(100, 300)} {y+random.randint(100, 300)}"
            svg += f'<path d="{path_d}" fill="none" stroke="{color}" stroke-width="{random.randint(2, 10)}" opacity="{op}">'
            svg += f'<animate attributeName="opacity" values="{op};{op+0.2};{op}" dur="{dur}s" repeatCount="indefinite" />'
            svg += '</path>'

    # 2. Add the title as massive floating text in the background!
    # This guarantees the SVG looks completely bespoke to the specific capability!
    text_color = random.choice(["#E2FA71", "#FFFFFF"])
    font_size = random.randint(60, 120)
    
    # We create a scrolling marquee effect of the title across the background
    svg += f'<g font-family="sans-serif" font-weight="900" font-size="{font_size}" fill="{text_color}" opacity="0.1">'
    svg += f'<text x="0" y="300">{title.upper()}</text>'
    svg += f'<animateTransform attributeName="transform" type="translate" values="{w};-1000" dur="{random.uniform(10.0, 20.0)}s" repeatCount="indefinite" />'
    svg += '</g>'
    
    # Add a second overlapping text moving the other way
    svg += f'<g font-family="sans-serif" font-weight="900" font-size="{font_size}" fill="{text_color}" opacity="0.05">'
    svg += f'<text x="0" y="450">{title.upper()}</text>'
    svg += f'<animateTransform attributeName="transform" type="translate" values="-1000;{w}" dur="{random.uniform(15.0, 25.0)}s" repeatCount="indefinite" />'
    svg += '</g>'
    
    svg += '</svg>'
    return svg

def global_replacer(match):
    title = match.group(1)
    slug = slugify(title)
    seed = int(hashlib.md5(title.encode()).hexdigest(), 16)
    
    svg_data = gen_bespoke_svg(title, seed)
    filename = f"{slug}.svg"
    
    with open(f"public\\images\\animated\\{filename}", "w", encoding="utf-8") as svg_file:
        svg_file.write(svg_data)
        
    return match.group(0) # Keep the original text identical, we just overwrote the SVGs!

# We just run this over the whole file again to completely replace all the previously generated SVGs!
re.sub(r'"title":\s*"([^"]+)".*?"image":\s*"/images/animated/([^"]+)"', global_replacer, content, flags=re.DOTALL)

print("Regenerated absolutely unique, title-embedded SVGs!")
