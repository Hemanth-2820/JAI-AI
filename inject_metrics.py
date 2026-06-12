import re

file_path = r'src\pages\Services\categoryData.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add a default metrics array to each category if it doesn't exist
default_metrics = """
    "metrics": [
      {
        "value": "30%+",
        "label": "conversion after UX audit & optimization."
      },
      {
        "value": "50%",
        "label": "potential savings with modular design system."
      },
      {
        "value": "98%",
        "label": "of projects are delivered on or before the deadline."
      }
    ],
"""

# Find all "techStack": [ block to insert right before it
content = re.sub(r'(\s*"techStack": \[)', default_metrics + r'\1', content)

# Also let's ensure process exists. The script doesn't need to add it if it's mostly there, 
# but let's check if there's any missing. For now, the metrics is the only strictly missing one.

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected metrics into categoryData.js")
