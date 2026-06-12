import os
import re
import hashlib

os.makedirs(r'public\images\animated', exist_ok=True)

file_path = r'src\pages\Services\categoryData.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

def slugify(text):
    text = text.lower()
    return re.sub(r'[^a-z0-9]+', '-', text).strip('-')

# --- SEMANTIC SVG GENERATORS ---

def gen_security(w=800, h=600):
    return f'''<svg width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#0E1F1A" />
  <g transform="translate(300, 150)" stroke="#E2FA71" stroke-width="8" fill="none" stroke-linejoin="round">
    <path d="M 100 20 L 180 60 L 180 160 C 180 240 100 300 100 300 C 100 300 20 240 20 160 L 20 60 Z">
      <animate attributeName="stroke-opacity" values="0.2;1;0.2" dur="3s" repeatCount="indefinite" />
    </path>
    <rect x="75" y="120" width="50" height="40" rx="5" />
    <path d="M 85 120 L 85 90 A 15 15 0 0 1 115 90 L 115 120" />
    <circle cx="100" cy="140" r="5" fill="#E2FA71" />
  </g>
  <circle cx="400" cy="300" r="250" fill="none" stroke="#1A3129" stroke-width="2">
    <animate attributeName="r" values="100;350" dur="4s" repeatCount="indefinite" />
    <animate attributeName="opacity" values="1;0" dur="4s" repeatCount="indefinite" />
  </circle>
</svg>'''

def gen_cloud(w=800, h=600):
    return f'''<svg width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#114051" />
  <g fill="#FFFFFF" opacity="0.8">
    <g transform="translate(150, 200)">
      <path d="M 50 80 Q 50 40 90 40 Q 110 10 150 10 Q 200 10 210 50 Q 260 50 260 90 Q 260 130 210 130 L 70 130 Q 30 130 30 90 Z" />
      <animateTransform attributeName="transform" type="translate" values="150,200; 150,180; 150,200" dur="4s" repeatCount="indefinite" />
    </g>
    <g transform="translate(450, 300)" opacity="0.5" transform-origin="center">
      <path d="M 50 80 Q 50 40 90 40 Q 110 10 150 10 Q 200 10 210 50 Q 260 50 260 90 Q 260 130 210 130 L 70 130 Q 30 130 30 90 Z" />
      <animateTransform attributeName="transform" type="translate" values="450,300; 450,320; 450,300" dur="5s" repeatCount="indefinite" />
    </g>
  </g>
  <g stroke="#E2FA71" stroke-width="4" stroke-linecap="round">
    <line x1="300" y1="400" x2="300" y2="450">
      <animate attributeName="y1" values="400;350;400" dur="2s" repeatCount="indefinite" />
      <animate attributeName="y2" values="450;400;450" dur="2s" repeatCount="indefinite" />
    </line>
    <line x1="350" y1="450" x2="350" y2="500">
      <animate attributeName="y1" values="450;400;450" dur="2.5s" repeatCount="indefinite" />
      <animate attributeName="y2" values="500;450;500" dur="2.5s" repeatCount="indefinite" />
    </line>
  </g>
</svg>'''

def gen_data(w=800, h=600):
    return f'''<svg width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#1A3129" />
  <g fill="#114051">
    <rect x="200" y="400" width="60" height="100">
      <animate attributeName="y" values="400;200;400" dur="3s" repeatCount="indefinite" />
      <animate attributeName="height" values="100;300;100" dur="3s" repeatCount="indefinite" />
    </rect>
    <rect x="300" y="300" width="60" height="200">
      <animate attributeName="y" values="300;100;300" dur="4s" repeatCount="indefinite" />
      <animate attributeName="height" values="200;400;200" dur="4s" repeatCount="indefinite" />
    </rect>
    <rect x="400" y="350" width="60" height="150">
      <animate attributeName="y" values="350;250;350" dur="2.5s" repeatCount="indefinite" />
      <animate attributeName="height" values="150;250;150" dur="2.5s" repeatCount="indefinite" />
    </rect>
    <rect x="500" y="200" width="60" height="300">
      <animate attributeName="y" values="200;50;200" dur="5s" repeatCount="indefinite" />
      <animate attributeName="height" values="300;450;300" dur="5s" repeatCount="indefinite" />
    </rect>
  </g>
  <polyline points="230,400 330,300 430,350 530,200 630,150" fill="none" stroke="#E2FA71" stroke-width="8" stroke-linejoin="round">
    <animate attributeName="points" values="230,400 330,300 430,350 530,200 630,150; 230,200 330,100 430,250 530,50 630,100; 230,400 330,300 430,350 530,200 630,150" dur="6s" repeatCount="indefinite" />
  </polyline>
</svg>'''

def gen_mobile(w=800, h=600):
    return f'''<svg width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#0E1F1A" />
  <g transform="translate(300, 100)">
    <rect x="0" y="0" width="200" height="400" rx="30" fill="none" stroke="#B48366" stroke-width="10" />
    <rect x="10" y="10" width="180" height="380" rx="20" fill="#114051" />
    <rect x="70" y="20" width="60" height="8" rx="4" fill="#0E1F1A" />
    
    <g fill="#E2FA71">
      <circle cx="50" cy="100" r="15"><animate attributeName="opacity" values="0.2;1;0.2" dur="2s" repeatCount="indefinite" /></circle>
      <circle cx="100" cy="100" r="15"><animate attributeName="opacity" values="0.2;1;0.2" dur="2.5s" repeatCount="indefinite" /></circle>
      <circle cx="150" cy="100" r="15"><animate attributeName="opacity" values="0.2;1;0.2" dur="3s" repeatCount="indefinite" /></circle>
      <rect x="35" y="150" width="130" height="100" rx="10" fill="#FFFFFF" opacity="0.8">
        <animate attributeName="height" values="100;120;100" dur="4s" repeatCount="indefinite" />
      </rect>
    </g>
  </g>
  <circle cx="400" cy="300" r="300" fill="none" stroke="#E2FA71" stroke-width="2" opacity="0.3">
    <animateTransform attributeName="transform" type="rotate" from="0 400 300" to="360 400 300" dur="10s" repeatCount="indefinite" />
    <animate attributeName="stroke-dasharray" values="10,20; 50,50; 10,20" dur="5s" repeatCount="indefinite" />
  </circle>
</svg>'''

def gen_web(w=800, h=600):
    return f'''<svg width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#1A3129" />
  <g transform="translate(100, 150)">
    <rect x="0" y="0" width="400" height="300" rx="10" fill="#114051" />
    <rect x="0" y="0" width="400" height="40" rx="10" fill="#0E1F1A" />
    <circle cx="20" cy="20" r="6" fill="#E2FA71" />
    <circle cx="40" cy="20" r="6" fill="#B48366" />
    <circle cx="60" cy="20" r="6" fill="#FFFFFF" />
    <rect x="20" y="70" width="150" height="20" fill="#FFFFFF" opacity="0.5" />
    <rect x="20" y="110" width="250" height="10" fill="#E2FA71" opacity="0.3" />
    <rect x="20" y="130" width="200" height="10" fill="#E2FA71" opacity="0.3" />
    <animateTransform attributeName="transform" type="translate" values="100,150; 120,130; 100,150" dur="5s" repeatCount="indefinite" />
  </g>
  <g transform="translate(300, 250)">
    <rect x="0" y="0" width="400" height="300" rx="10" fill="#0E1F1A" stroke="#E2FA71" stroke-width="4" />
    <rect x="0" y="0" width="400" height="40" rx="10" fill="#114051" />
    <rect x="30" y="80" width="100" height="100" fill="#FFFFFF" opacity="0.2">
        <animate attributeName="width" values="100;150;100" dur="3s" repeatCount="indefinite" />
    </rect>
    <rect x="150" y="80" width="200" height="15" fill="#E2FA71" />
    <rect x="150" y="110" width="150" height="15" fill="#E2FA71" opacity="0.5" />
    <animateTransform attributeName="transform" type="translate" values="300,250; 280,270; 300,250" dur="4s" repeatCount="indefinite" />
  </g>
</svg>'''

def gen_ai(w=800, h=600):
    return f'''<svg width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#0E1F1A" />
  <g stroke="#E2FA71" stroke-width="3" opacity="0.6">
    <line x1="300" y1="200" x2="500" y2="200"><animate attributeName="stroke-opacity" values="0.1;1;0.1" dur="2s" repeatCount="indefinite" /></line>
    <line x1="500" y1="200" x2="400" y2="400"><animate attributeName="stroke-opacity" values="0.1;1;0.1" dur="2.5s" repeatCount="indefinite" /></line>
    <line x1="400" y1="400" x2="300" y2="200"><animate attributeName="stroke-opacity" values="0.1;1;0.1" dur="3s" repeatCount="indefinite" /></line>
    <line x1="300" y1="200" x2="200" y2="300"><animate attributeName="stroke-opacity" values="0.1;1;0.1" dur="1.5s" repeatCount="indefinite" /></line>
    <line x1="500" y1="200" x2="600" y2="300"><animate attributeName="stroke-opacity" values="0.1;1;0.1" dur="3.5s" repeatCount="indefinite" /></line>
    <line x1="400" y1="400" x2="400" y2="500"><animate attributeName="stroke-opacity" values="0.1;1;0.1" dur="2.2s" repeatCount="indefinite" /></line>
  </g>
  <g fill="#FFFFFF">
    <circle cx="300" cy="200" r="15"><animate attributeName="r" values="15;25;15" dur="2s" repeatCount="indefinite" /></circle>
    <circle cx="500" cy="200" r="15"><animate attributeName="r" values="15;25;15" dur="2.5s" repeatCount="indefinite" /></circle>
    <circle cx="400" cy="400" r="20"><animate attributeName="r" values="20;30;20" dur="3s" repeatCount="indefinite" /></circle>
    <circle cx="200" cy="300" r="10"><animate attributeName="r" values="10;20;10" dur="1.5s" repeatCount="indefinite" /></circle>
    <circle cx="600" cy="300" r="10"><animate attributeName="r" values="10;20;10" dur="3.5s" repeatCount="indefinite" /></circle>
    <circle cx="400" cy="500" r="10"><animate attributeName="r" values="10;20;10" dur="2.2s" repeatCount="indefinite" /></circle>
  </g>
  <circle cx="400" cy="300" r="150" fill="none" stroke="#114051" stroke-width="40" stroke-dasharray="20 40">
    <animateTransform attributeName="transform" type="rotate" from="0 400 300" to="360 400 300" dur="20s" repeatCount="indefinite" />
  </circle>
</svg>'''

def gen_code(w=800, h=600):
    return f'''<svg width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#114051" />
  <g font-family="monospace" font-size="150" font-weight="bold" fill="#E2FA71">
    <text x="150" y="350">
      &lt;
      <animateTransform attributeName="transform" type="translate" values="0; -50; 0" dur="3s" repeatCount="indefinite" />
    </text>
    <text x="350" y="350" fill="#FFFFFF">
      /
      <animateTransform attributeName="transform" type="rotate" values="0 400 300; 360 400 300" dur="5s" repeatCount="indefinite" />
    </text>
    <text x="500" y="350">
      &gt;
      <animateTransform attributeName="transform" type="translate" values="0; 50; 0" dur="3s" repeatCount="indefinite" />
    </text>
  </g>
  <g font-family="monospace" font-size="40" fill="#B48366" opacity="0.3">
    <text x="50" y="100">function init() {{</text>
    <text x="100" y="150">const app = render();</text>
    <text x="100" y="200">return app.scale();</text>
    <text x="50" y="250">}}</text>
    <animate attributeName="opacity" values="0.1;0.5;0.1" dur="4s" repeatCount="indefinite" />
  </g>
</svg>'''

def gen_generic(w=800, h=600):
    return f'''<svg width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#0E1F1A" />
  <g fill="none" stroke="#B48366" stroke-width="4">
    <rect x="250" y="150" width="300" height="300">
      <animateTransform attributeName="transform" type="rotate" from="0 400 300" to="360 400 300" dur="15s" repeatCount="indefinite" />
    </rect>
    <rect x="300" y="200" width="200" height="200" stroke="#E2FA71">
      <animateTransform attributeName="transform" type="rotate" from="360 400 300" to="0 400 300" dur="10s" repeatCount="indefinite" />
    </rect>
  </g>
  <circle cx="400" cy="300" r="20" fill="#FFFFFF">
    <animate attributeName="r" values="20;50;20" dur="3s" repeatCount="indefinite" />
  </circle>
</svg>'''

# Map keywords to generators
def get_generator_for_title(title):
    t = title.lower()
    if any(k in t for k in ['secur', 'trust', 'audit', 'threat', 'phish', 'compliance']):
        return gen_security
    if any(k in t for k in ['cloud', 'aws', 'server', 'edge', 'federation']):
        return gen_cloud
    if any(k in t for k in ['data', 'analytic', 'optimiz', 'rate', 'metric', 'finops']):
        return gen_data
    if any(k in t for k in ['app', 'mobil', 'wearable', 'ar', 'vr']):
        return gen_mobile
    if any(k in t for k in ['web', 'ux', 'ui', 'access', 'design', 'jamstack']):
        return gen_web
    if any(k in t for k in ['ai', 'bot', 'language', 'neural', 'machine', 'generative']):
        return gen_ai
    if any(k in t for k in ['code', 'dev', 'microservice', 'git', 'api']):
        return gen_code
    return gen_generic

def global_replacer(match):
    title = match.group(1)
    slug = slugify(title)
    
    generator = get_generator_for_title(title)
    svg_data = generator()
    
    filename = f"{slug}.svg"
    with open(f"public\\images\\animated\\{filename}", "w", encoding="utf-8") as svg_file:
        svg_file.write(svg_data)
        
    return match.group(0)

# Replace images and write new semantic SVGs
new_content = re.sub(r'"title":\s*"([^"]+)".*?"image":\s*"/images/animated/([^"]+)"', global_replacer, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Generated and linked 100% SEMANTIC SVGs!")
