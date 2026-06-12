import re

# 1. Update categoryData.js
file_path = r'src\pages\Services\categoryData.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

extended_capabilities = """
    "extendedCapabilities": [
      {
        "title": "Website design",
        "desc": "Website UX research, wireframes, responsive design, and high-fidelity UI, tailored to your goals.",
        "image": "https://images.unsplash.com/photo-1547658719-da2b51169166?q=80&w=600&auto=format&fit=crop",
        "bgColor": "#B48366",
        "textColor": "#ffffff",
        "span": 1
      },
      {
        "title": "Webflow development",
        "desc": "Certified Webflow partner offering flexible, scalable builds with CMS integration.",
        "image": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?q=80&w=600&auto=format&fit=crop",
        "bgColor": "#E2C3B7",
        "textColor": "#0E1F1A",
        "span": 1
      },
      {
        "title": "Landing pages",
        "desc": "Funnel-stage pages that launch fast—fully optimized, mobile first, and on brand. Ideal for product launches, paid media, lifecycle marketing, and SEO.",
        "image": "https://images.unsplash.com/photo-1512428559087-560fa5ceab42?q=80&w=800&auto=format&fit=crop",
        "bgColor": "#114051",
        "textColor": "#ffffff",
        "span": 2
      },
      {
        "title": "Design systems and UI kits",
        "desc": "Reusable component libraries built following the Atomic design methodology to scale with consistency",
        "image": "https://images.unsplash.com/photo-1561070791-2526d30994b5?q=80&w=800&auto=format&fit=crop",
        "bgColor": "#1A3129",
        "textColor": "#ffffff",
        "span": 2
      },
      {
        "title": "UX/UI audits",
        "desc": "Deep research into conversion leaks and usability gaps, plus expert recs to boost performance.",
        "image": "https://images.unsplash.com/photo-1581291518857-4e27b48ff24e?q=80&w=600&auto=format&fit=crop",
        "bgColor": "#DDE2CD",
        "textColor": "#0E1F1A",
        "span": 1
      },
      {
        "title": "Copy & motion support",
        "desc": "Full-stack creative including headlines, content hierarchy, microcopy, and animation.",
        "image": "https://images.unsplash.com/photo-1501250987900-2118ddeca0f6?q=80&w=600&auto=format&fit=crop",
        "bgColor": "#C3DBE3",
        "textColor": "#0E1F1A",
        "span": 1
      }
    ],
"""

if '"extendedCapabilities"' not in content:
    content = re.sub(r'("heroImage":\s*"[^"]+",)', r'\1\n' + extended_capabilities, content)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)


# 2. Update Services.module.css to remove hardcoded nth-child overrides so inline styles work
css_path = r'src\pages\Services\Services.module.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Remove the hardcoded nth-child rules that override inline styles
css = re.sub(r'/\*\s*Asymmetric Grid Sizing & Background Colors\s*\*/[\s\S]*?/\*\s*Text Content\s*\*/', '/* Text Content */', css)
css = re.sub(r'/\*\s*Force text to white for dark backgrounds.*?\}', '', css, flags=re.DOTALL)
# Also remove any remaining nth-child rules for superAsymCard
css = re.sub(r'\.superAsymCard:nth-child\([^\)]+\)\s*\{[^}]+\}', '', css)
css = re.sub(r'\.superAsymCard:nth-child\([^\)]+\)\s*\.superAsymCardTitle\s*\{[^}]+\}', '', css)
css = re.sub(r'\.superAsymCard:nth-child\([^\)]+\)\s*\.superAsymCardDesc\s*\{[^}]+\}', '', css)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Data injected and CSS updated!")
