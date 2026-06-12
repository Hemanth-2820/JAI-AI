import re

file_path = r'src\pages\Services\categoryData.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix syntax errors caused by double commas
content = content.replace(',,', ',')

# Define generic capabilities to inject if a category is missing extendedCapabilities
generic_caps = [
    "Digital Strategy", "User Experience Design", "Scalable Architectures", 
    "Performance Optimization", "Data Analytics", "Maintenance & Support"
]

design_patterns = [
    {"span": 1, "bgColor": "#B48366", "textColor": "#ffffff", "image": "https://images.unsplash.com/photo-1547658719-da2b51169166?q=80&w=600&auto=format&fit=crop"},
    {"span": 1, "bgColor": "#E2C3B7", "textColor": "#0E1F1A", "image": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?q=80&w=600&auto=format&fit=crop"},
    {"span": 2, "bgColor": "#114051", "textColor": "#ffffff", "image": "https://images.unsplash.com/photo-1512428559087-560fa5ceab42?q=80&w=800&auto=format&fit=crop"},
    {"span": 2, "bgColor": "#1A3129", "textColor": "#ffffff", "image": "https://images.unsplash.com/photo-1561070791-2526d30994b5?q=80&w=800&auto=format&fit=crop"},
    {"span": 1, "bgColor": "#DDE2CD", "textColor": "#0E1F1A", "image": "https://images.unsplash.com/photo-1581291518857-4e27b48ff24e?q=80&w=600&auto=format&fit=crop"},
    {"span": 1, "bgColor": "#C3DBE3", "textColor": "#0E1F1A", "image": "https://images.unsplash.com/photo-1501250987900-2118ddeca0f6?q=80&w=600&auto=format&fit=crop"}
]

caps_json = '    "extendedCapabilities": [\n'
for i, cap in enumerate(generic_caps):
    p = design_patterns[i]
    caps_json += f'''      {{
    "title": "{cap}",
    "desc": "Expert {cap.lower()} solutions designed to scale securely and efficiently to meet your specific business requirements.",
    "image": "{p["image"]}",
    "bgColor": "{p["bgColor"]}",
    "textColor": "{p["textColor"]}",
    "span": {p["span"]}
  }}''' + (',' if i < 5 else '') + '\n'
caps_json += '    ],'

# Find all categories that are missing extendedCapabilities and inject the generic array
# A category starts with "category-name": { ... "heroImage": "...",
# We can use regex to find "heroImage": "..." and if it's NOT followed by "extendedCapabilities", inject it.
# We'll just split by heroImage and insert it if not present.

new_content = ""
parts = content.split('"heroImage":')
new_content += parts[0]

for i in range(1, len(parts)):
    part = parts[i]
    # The part starts with e.g. ' "/images/hero.jpg",\n'
    # Let's see if extendedCapabilities is within the next 100 characters
    if '"extendedCapabilities"' not in part[:150]:
        # We need to insert it right after the line break
        # Find the first newline
        newline_idx = part.find('\\n')
        if newline_idx == -1:
            newline_idx = part.find('\\n')
        
        # safely insert
        lines = part.split('\\n', 1)
        if len(lines) == 2:
            new_content += '"heroImage":' + lines[0] + '\\n' + caps_json + '\\n' + lines[1]
        else:
            # fallback
            new_content += '"heroImage":' + part.replace(',', ',\\n' + caps_json, 1)
    else:
        new_content += '"heroImage":' + part

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Fixed double commas and ensured all categories have extendedCapabilities!")
