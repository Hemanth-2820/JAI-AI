import os
import re

os.makedirs(r'public\images\animated', exist_ok=True)

# 1. Tech Nodes (Network)
svg1 = '''<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="grad1" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#1A3129" />
      <stop offset="100%" stop-color="#0E1F1A" />
    </radialGradient>
  </defs>
  <rect width="100%" height="100%" fill="url(#grad1)" />
  <g stroke="rgba(226, 250, 113, 0.3)" stroke-width="2">
    <line x1="200" y1="200" x2="600" y2="400" />
    <line x1="200" y1="400" x2="600" y2="200" />
    <line x1="400" y1="100" x2="400" y2="500" />
    <line x1="100" y1="300" x2="700" y2="300" />
  </g>
  <circle cx="200" cy="200" r="10" fill="#E2FA71">
    <animate attributeName="r" values="8;15;8" dur="2s" repeatCount="indefinite" />
  </circle>
  <circle cx="600" cy="400" r="15" fill="#E2FA71">
    <animate attributeName="r" values="10;20;10" dur="3s" repeatCount="indefinite" />
  </circle>
  <circle cx="200" cy="400" r="12" fill="#E2FA71">
    <animate attributeName="r" values="8;18;8" dur="2.5s" repeatCount="indefinite" />
  </circle>
  <circle cx="600" cy="200" r="10" fill="#E2FA71">
    <animate attributeName="r" values="10;15;10" dur="1.5s" repeatCount="indefinite" />
  </circle>
  <circle cx="400" cy="300" r="25" fill="#FFFFFF">
    <animate attributeName="r" values="20;30;20" dur="4s" repeatCount="indefinite" />
  </circle>
</svg>'''

# 2. Cyber Hex (Hexagons)
svg2 = '''<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#0E1F1A" />
  <g fill="none" stroke="#E2FA71" stroke-width="2">
    <polygon points="400,200 486,250 486,350 400,400 314,350 314,250">
      <animate attributeName="opacity" values="0.2;1;0.2" dur="3s" repeatCount="indefinite" />
      <animateTransform attributeName="transform" type="scale" values="1;1.1;1" cx="400" cy="300" dur="3s" repeatCount="indefinite" />
    </polygon>
    <polygon points="400,100 486,150 486,250 400,200 314,250 314,150" opacity="0.3">
      <animate attributeName="opacity" values="1;0.2;1" dur="4s" repeatCount="indefinite" />
    </polygon>
    <polygon points="400,400 486,450 486,550 400,600 314,550 314,450" opacity="0.3">
      <animate attributeName="opacity" values="1;0.2;1" dur="4s" repeatCount="indefinite" />
    </polygon>
  </g>
</svg>'''

# 3. Pulse Rings (Data waves)
svg3 = '''<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#114051" />
  <circle cx="400" cy="300" r="50" fill="none" stroke="#FFFFFF" stroke-width="4">
    <animate attributeName="r" values="50;300" dur="3s" repeatCount="indefinite" />
    <animate attributeName="opacity" values="1;0" dur="3s" repeatCount="indefinite" />
  </circle>
  <circle cx="400" cy="300" r="50" fill="none" stroke="#E2FA71" stroke-width="2">
    <animate attributeName="r" values="50;300" dur="3s" begin="1s" repeatCount="indefinite" />
    <animate attributeName="opacity" values="1;0" dur="3s" begin="1s" repeatCount="indefinite" />
  </circle>
  <circle cx="400" cy="300" r="50" fill="none" stroke="#FFFFFF" stroke-width="1">
    <animate attributeName="r" values="50;300" dur="3s" begin="2s" repeatCount="indefinite" />
    <animate attributeName="opacity" values="1;0" dur="3s" begin="2s" repeatCount="indefinite" />
  </circle>
</svg>'''

# 4. Code Lines (Server terminal)
svg4 = '''<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#000000" />
  <g fill="#E2FA71" font-family="monospace" font-size="20">
    <rect x="50" y="100" height="15" fill="#E2FA71">
      <animate attributeName="width" values="0;400;400;0" dur="4s" repeatCount="indefinite" />
    </rect>
    <rect x="50" y="150" height="15" fill="#FFFFFF" opacity="0.7">
      <animate attributeName="width" values="0;250;250;0" dur="3.5s" begin="0.5s" repeatCount="indefinite" />
    </rect>
    <rect x="50" y="200" height="15" fill="#E2FA71">
      <animate attributeName="width" values="0;600;600;0" dur="5s" begin="1s" repeatCount="indefinite" />
    </rect>
    <rect x="50" y="250" height="15" fill="#FFFFFF" opacity="0.5">
      <animate attributeName="width" values="0;350;350;0" dur="4s" begin="1.5s" repeatCount="indefinite" />
    </rect>
    <rect x="50" y="300" height="15" fill="#E2FA71">
      <animate attributeName="width" values="0;500;500;0" dur="6s" begin="2s" repeatCount="indefinite" />
    </rect>
  </g>
</svg>'''

# 5. Data Flow (Blocks falling/moving)
svg5 = '''<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#1A3129" />
  <g fill="#E2FA71">
    <rect x="100" y="0" width="40" height="80">
      <animate attributeName="y" values="-80;600" dur="4s" repeatCount="indefinite" />
      <animate attributeName="opacity" values="0;1;0" dur="4s" repeatCount="indefinite" />
    </rect>
    <rect x="300" y="0" width="60" height="120" fill="#FFFFFF">
      <animate attributeName="y" values="-120;600" dur="5s" begin="1s" repeatCount="indefinite" />
      <animate attributeName="opacity" values="0;0.5;0" dur="5s" begin="1s" repeatCount="indefinite" />
    </rect>
    <rect x="500" y="0" width="30" height="60">
      <animate attributeName="y" values="-60;600" dur="3s" begin="2s" repeatCount="indefinite" />
      <animate attributeName="opacity" values="0;1;0" dur="3s" begin="2s" repeatCount="indefinite" />
    </rect>
    <rect x="700" y="0" width="80" height="160" fill="#FFFFFF">
      <animate attributeName="y" values="-160;600" dur="6s" begin="0.5s" repeatCount="indefinite" />
      <animate attributeName="opacity" values="0;0.3;0" dur="6s" begin="0.5s" repeatCount="indefinite" />
    </rect>
  </g>
</svg>'''

# 6. Digital Sun (Gradient rotation)
svg6 = '''<svg width="800" height="600" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#E2FA71" />
      <stop offset="100%" stop-color="#114051" />
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="#0E1F1A" />
  <circle cx="400" cy="300" r="200" fill="url(#grad2)">
    <animateTransform attributeName="transform" type="rotate" from="0 400 300" to="360 400 300" dur="10s" repeatCount="indefinite" />
  </circle>
  <circle cx="400" cy="300" r="150" fill="#0E1F1A" />
  <circle cx="400" cy="300" r="100" fill="url(#grad2)">
    <animateTransform attributeName="transform" type="rotate" from="360 400 300" to="0 400 300" dur="7s" repeatCount="indefinite" />
  </circle>
</svg>'''

svgs = [svg1, svg2, svg3, svg4, svg5, svg6]
svg_names = ['tech-nodes.svg', 'cyber-hex.svg', 'pulse-rings.svg', 'code-lines.svg', 'data-flow.svg', 'digital-sun.svg']

for i, svg in enumerate(svgs):
    with open(f'public\\images\\animated\\{svg_names[i]}', 'w', encoding='utf-8') as f:
        f.write(svg)

# Now update categoryData.js to use these SVGs as images, and remove the video field so the ternary falls back to <img>!
file_path = r'src\pages\Services\categoryData.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# First, strip out the "video": "..." fields
content = re.sub(r',\s*"video":\s*"[^"]+"', '', content)
content = re.sub(r'"video":\s*"[^"]+"\s*,', '', content)
content = re.sub(r'"video":\s*"[^"]+"', '', content)

# Next, we will replace the "image": "..." inside extendedCapabilities cyclically with our SVGs.
def replacer(match):
    global idx
    svg_file = svg_names[idx % 6]
    idx += 1
    return f'"image": "/images/animated/{svg_file}"'

# We match the entire extendedCapabilities block, then replace images inside it.
def block_replacer(match):
    block = match.group(0)
    global idx
    idx = 0
    return re.sub(r'"image":\s*"[^"]+"', replacer, block)

new_content = re.sub(r'"extendedCapabilities":\s*\[(.*?)\]', block_replacer, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Generated and injected animated SVGs successfully!")
