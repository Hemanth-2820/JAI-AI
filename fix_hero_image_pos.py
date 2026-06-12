import re

css_path = r'src\pages\Services\Services.module.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

new_wrapper_css = """
.superHeroImageWrapper {
  width: 50%;
  position: absolute;
  right: 0;
  top: 15%;
  height: 70%;
  display: flex;
  align-items: flex-start; /* Move to top */
  justify-content: center;
  z-index: 1;
}

.superHeroImg {
  width: 100%;
  height: 100%;
  object-fit: contain;
  object-position: center top; /* Align to top */
}
"""

# Replace existing wrapper and img CSS
css = re.sub(r'\.superHeroImageWrapper\s*\{[^}]+\}', '', css)
css = re.sub(r'\.superHeroImg\s*\{[^}]+\}', '', css)

# Append new styles
css += "\n" + new_wrapper_css

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated Hero Image position to top!")
