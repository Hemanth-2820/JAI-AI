import re

css_path = r'src\index.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Add CSS for the dropdown arrow to make it appear below the word Services
arrow_css = """
.navDropdownWrapper .navLink {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
}

.dropdownArrow {
  font-size: 10px;
  color: #cccccc;
  line-height: 1;
  transition: transform 0.3s ease;
}

.navDropdownWrapper:hover .dropdownArrow {
  transform: rotate(180deg);
}
"""

if '.dropdownArrow' not in css:
    css += "\n" + arrow_css
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)
    print("Added dropdownArrow CSS!")
else:
    # Let's replace the existing styling
    css = re.sub(r'\.dropdownArrow\s*\{[^}]+\}', '', css)
    css += "\n" + arrow_css
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)
    print("Replaced dropdownArrow CSS!")
