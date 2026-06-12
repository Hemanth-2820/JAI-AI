import re

css_path = r'src\pages\Services\Services.module.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Fix the Hero padding so the marquee doesn't overlap the button
css = re.sub(r'(\.superHero\s*\{[^}]*padding:\s*)(100px 5% 0 5%)', r'\g<1>100px 5% 100px 5%', css)

# Update Marquee CSS for animation
new_marquee_css = """
.superHeroMarquee {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  padding: 0 0 30px 0;
  z-index: 10;
  display: flex;
  overflow-x: hidden;
  background: linear-gradient(to top, rgba(14, 31, 26, 1) 0%, rgba(14, 31, 26, 0) 100%);
}

.superMarqueeTrack {
  display: flex;
  width: max-content;
  animation: superScrollLeftToRight 40s linear infinite;
  gap: 16px;
  padding-left: 16px;
}

.superHeroMarquee:hover .superMarqueeTrack {
  animation-play-state: paused;
}

@keyframes superScrollLeftToRight {
  0% {
    transform: translateX(calc(-50% - 8px));
  }
  100% {
    transform: translateX(0);
  }
}

.superMarqueeCard {
  flex: 0 0 auto;
  display: flex;
  align-items: center;
  background-color: #EFEFDF;
  padding: 6px 20px 6px 6px;
  border-radius: 12px;
  gap: 12px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
  cursor: pointer;
  transition: transform 0.2s ease;
}

.superMarqueeCard:hover {
  transform: translateY(-2px);
}

.superMarqueeImg {
  width: 60px;
  height: 45px;
  border-radius: 8px;
  object-fit: cover;
}

.superMarqueeText {
  color: #0E1F1A;
  font-weight: 500;
  font-size: 15px;
  white-space: nowrap;
}
"""

# Replace the old marquee CSS
css = re.sub(r'/\*\s*={41}\s*SUPERSIDE HERO MARQUEE SCROLL\s*={41}\s*\*/[\s\S]*?(?=\n\n/\*|\Z)', "/* =========================================\n   SUPERSIDE HERO MARQUEE SCROLL\n   ========================================= */\n" + new_marquee_css, css)


with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Marquee animation applied!")
