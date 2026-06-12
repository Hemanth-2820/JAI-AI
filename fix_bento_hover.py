import re

css_path = r'src\pages\Services\Services.module.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the old bento card bg and content CSS with the new hover state logic
new_css = """
.superBentoCard {
  position: relative;
  border-radius: 24px;
  overflow: hidden;
  min-height: 400px;
  background-color: #E2E4DB;
  cursor: pointer;
}

.superBentoImg {
  position: absolute;
  top: 0; left: 0; width: 100%; height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.superBentoCard:hover .superBentoImg {
  transform: scale(1.05);
}

.superBentoDefault {
  position: absolute;
  bottom: 0; left: 0; width: 100%;
  padding: 40px;
  background: linear-gradient(to top, rgba(0,0,0,0.8) 0%, transparent 100%);
  display: flex;
  align-items: flex-end;
  z-index: 2;
  transition: opacity 0.3s ease;
}

.superBentoDefault h3 {
  font-size: 28px;
  font-weight: 500;
  margin: 0;
  color: #ffffff !important;
}

.superBentoCard:hover .superBentoDefault {
  opacity: 0;
}

.superBentoHover {
  position: absolute;
  top: 0; left: 0; width: 100%; height: 100%;
  padding: 40px;
  background: rgba(14, 31, 26, 0.9);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  z-index: 3;
  opacity: 0;
  transform: translateY(20px);
  transition: all 0.4s ease;
}

.superBentoHover h3 {
  font-size: 28px;
  font-weight: 500;
  margin-bottom: 16px;
  color: #ffffff !important;
}

.superBentoHover p {
  font-size: 16px;
  line-height: 1.6;
  color: rgba(255, 255, 255, 0.8) !important;
}

.superBentoCard:hover .superBentoHover {
  opacity: 1;
  transform: translateY(0);
}
"""

# Remove old .superBentoCard:hover transform, .superBentoCardBg, .superBentoCardContent
css = re.sub(r'\.superBentoCard\s*\{[^}]+\}', '', css)
css = re.sub(r'\.superBentoCard:hover\s*\{[^}]+\}', '', css)
css = re.sub(r'\.superBentoCardBg\s*\{[^}]+\}', '', css)
css = re.sub(r'\.superBentoCardContent\s*\{[^}]+\}', '', css)
css = re.sub(r'\.superBentoCardContent\s+h3\s*\{[^}]+\}', '', css)
css = re.sub(r'\.superBentoCardContent\s+p\s*\{[^}]+\}', '', css)

# Append the new css
with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css + "\n\n" + new_css)

print("Hover state CSS applied!")
