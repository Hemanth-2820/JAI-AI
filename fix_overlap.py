import re

css_path = r'src\pages\Services\Services.module.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Fix .superHero to be a column layout
new_super_hero = """
.superHero {
  display: flex;
  flex-direction: column;
  background-color: #0E1F1A;
  color: #FFFFFF;
  padding: 100px 0 0 0;
  min-height: 80vh;
  position: relative;
  overflow: hidden;
}

.superHeroInner {
  display: flex;
  width: 100%;
  padding: 0 5%;
  flex: 1;
  align-items: center;
  position: relative;
  padding-bottom: 60px;
}
"""

css = re.sub(r'\.superHero\s*\{[^}]+\}', new_super_hero.strip(), css)

# Fix .superHeroMarquee to flow naturally instead of absolute positioning
new_marquee = """
.superHeroMarquee {
  width: 100%;
  padding: 0 0 30px 0;
  z-index: 10;
  display: flex;
  overflow-x: hidden;
  background: linear-gradient(to top, rgba(14, 31, 26, 1) 0%, rgba(14, 31, 26, 0) 100%);
  margin-top: auto;
}
"""

css = re.sub(r'\.superHeroMarquee\s*\{[^}]+\}', new_marquee.strip(), css)

# Make sure superHeroContent width is still 55%
css = re.sub(r'(\.superHeroContent\s*\{[^}]*width:\s*)50%', r'\g<1>55%', css)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Fixed layout CSS!")
