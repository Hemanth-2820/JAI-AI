import re

css_path = r'src\pages\Services\Services.module.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace .superBentoCardBg
new_bg = """
.superBentoCardBg {
  position: absolute;
  bottom: 0; left: 0; width: 100%; height: 100%;
  background-size: cover;
  background-position: center bottom;
  opacity: 1;
}
"""
css = re.sub(r'\.superBentoCardBg\s*\{[^}]+\}', new_bg.strip(), css)

# Replace .superBentoCardContent
new_content = """
.superBentoCardContent {
  position: absolute;
  top: 0; left: 0; width: 100%; height: 100%;
  padding: 40px;
  display: flex;
  flex-direction: column;
  z-index: 2;
  /* Strong solid gradient at the top that perfectly hides the image behind the text */
  background: linear-gradient(to bottom, rgba(226, 228, 219, 1) 0%, rgba(226, 228, 219, 0.95) 45%, rgba(226, 228, 219, 0) 100%);
}
"""
css = re.sub(r'\.superBentoCardContent\s*\{[^}]+\}', new_content.strip(), css)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated Bento Grid CSS!")
