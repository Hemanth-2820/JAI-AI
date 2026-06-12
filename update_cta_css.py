import re

css_path = r'src\pages\Services\Services.module.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the existing superBottomCta styles with the updated, left-aligned design
new_cta_css = """
.superBottomCta {
  position: relative;
  width: 100%;
  min-height: 500px;
  display: flex;
  align-items: center;
  overflow: hidden;
  margin-top: 80px;
}

.superBottomCtaInner {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
}

.superBottomCtaInner::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(to right, rgba(14, 31, 26, 0.95) 0%, rgba(14, 31, 26, 0.7) 40%, transparent 100%);
}

.superBottomCtaContent {
  position: relative;
  z-index: 2;
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 5%;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  text-align: left;
}

.superBottomCtaContent h2 {
  font-size: clamp(40px, 5vw, 64px);
  font-weight: 500;
  color: #FFFFFF;
  line-height: 1.1;
  max-width: 700px;
  margin-bottom: 24px;
}

.superBottomCtaContent p {
  font-size: 18px;
  color: rgba(255, 255, 255, 0.85);
  max-width: 500px;
  line-height: 1.6;
  margin-bottom: 40px;
}

.superBtnLime {
  background-color: #E2FA71;
  color: #0E1F1A;
  padding: 18px 36px;
  font-size: 16px;
  font-weight: 600;
  border: none;
  border-radius: 40px;
  cursor: pointer;
  transition: all 0.3s ease;
  display: inline-block;
}

.superBtnLime:hover {
  background-color: #d1e860;
  transform: translateY(-2px);
}
"""

# Regex to strip out the old superBottomCta styles
# This will match from .superBottomCta to the end of the file or next major section.
css = re.sub(r'\.superBottomCta\s*\{[\s\S]*?(?=\n\n/\*|\Z)', '', css)
# If the regex matched too greedily or failed, let's also specifically remove these blocks
css = re.sub(r'\.superBottomCta[a-zA-Z0-9_-]*\s*\{[^}]+\}', '', css)
# Remove duplicate class matches just in case
css = re.sub(r'\.superBtnLime\s*\{[^}]+\}', '', css)
css = re.sub(r'\.superBtnLime:hover\s*\{[^}]+\}', '', css)

css += "\n" + new_cta_css

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated CTA CSS!")
