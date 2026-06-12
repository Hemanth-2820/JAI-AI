import re

file_path = r'src\pages\Services\categoryData.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# First, remove any existing extendedCapabilities to avoid duplicates
content = re.sub(r'\s*"extendedCapabilities":\s*\[.*?\](,\n|\n)', r'\1', content, flags=re.DOTALL)

categories = {
    "web-development": ["Custom Web Apps", "E-Commerce Stores", "Progressive Web Apps", "CMS Integrations", "API Development", "Web Maintenance"],
    "software-development": ["Enterprise Software", "Legacy Migration", "SaaS Solutions", "System Integration", "Custom Workflows", "Desktop Apps"],
    "data-science": ["Predictive Analytics", "Data Visualization", "Machine Learning", "Big Data", "Business Intelligence", "Data Engineering"],
    "artificial-intelligence": ["NLP Systems", "Computer Vision", "Generative AI", "AI Chatbots", "RPA Automation", "AI Strategy"],
    "aws-devops": ["Cloud Architecture", "CI/CD Pipelines", "Containerization", "Infrastructure as Code", "Serverless Computing", "Performance Monitoring"],
    "cyber-security": ["Penetration Testing", "Vulnerability Assessments", "Security Audits", "Compliance Consulting", "Incident Response", "Network Security"],
    "ui-ux-design": ["User Research", "Wireframing", "Design Systems", "Usability Testing", "Interaction Design", "UI Kits"],
    "mobile-app-development": ["iOS Development", "Android Development", "Cross-Platform", "Mobile UI/UX", "App Store Optimization", "App Maintenance"],
    "digital-marketing": ["SEO Optimization", "PPC Campaigns", "Social Media", "Content Marketing", "Email Marketing", "Conversion Optimization"],
    "cloud-computing": ["Cloud Migration", "Multi-Cloud Strategy", "Cloud Security", "Disaster Recovery", "Cloud Optimization", "Serverless Architecture"],
    "blockchain-development": ["Smart Contracts", "DeFi Platforms", "NFT Marketplaces", "Custom Blockchains", "Wallet Development", "Tokenomics"]
}

# The spans, bg colors, text colors, and generic images to maintain the EXACT design structure
design_patterns = [
    {"span": 1, "bgColor": "#B48366", "textColor": "#ffffff", "image": "https://images.unsplash.com/photo-1547658719-da2b51169166?q=80&w=600&auto=format&fit=crop"},
    {"span": 1, "bgColor": "#E2C3B7", "textColor": "#0E1F1A", "image": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?q=80&w=600&auto=format&fit=crop"},
    {"span": 2, "bgColor": "#114051", "textColor": "#ffffff", "image": "https://images.unsplash.com/photo-1512428559087-560fa5ceab42?q=80&w=800&auto=format&fit=crop"},
    {"span": 2, "bgColor": "#1A3129", "textColor": "#ffffff", "image": "https://images.unsplash.com/photo-1561070791-2526d30994b5?q=80&w=800&auto=format&fit=crop"},
    {"span": 1, "bgColor": "#DDE2CD", "textColor": "#0E1F1A", "image": "https://images.unsplash.com/photo-1581291518857-4e27b48ff24e?q=80&w=600&auto=format&fit=crop"},
    {"span": 1, "bgColor": "#C3DBE3", "textColor": "#0E1F1A", "image": "https://images.unsplash.com/photo-1501250987900-2118ddeca0f6?q=80&w=600&auto=format&fit=crop"}
]

for cat_key, caps in categories.items():
    caps_json = '    "extendedCapabilities": [\n'
    for i, cap in enumerate(caps):
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
    
    # Inject it directly after "heroImage"
    pattern = r'("?' + re.escape(cat_key) + r'"?:\s*\{[\s\S]*?"heroImage":\s*"[^"]+",)'
    content = re.sub(pattern, r'\1\n' + caps_json, content, count=1)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Dynamic capabilities injected successfully!")
