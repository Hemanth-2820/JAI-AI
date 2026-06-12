import re

css_path = r'src\pages\Services\Services.module.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

marquee_css = """
/* =========================================
   SUPERSIDE HERO MARQUEE SCROLL
   ========================================= */

.superHeroMarquee {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  padding: 0 5% 30px 5%;
  z-index: 10;
  display: flex;
  overflow-x: auto;
  gap: 16px;
  scrollbar-width: none; /* Firefox */
}

.superHeroMarquee::-webkit-scrollbar {
  display: none; /* Chrome/Safari */
}

.superMarqueeCard {
  flex: 0 0 auto;
  display: flex;
  align-items: center;
  background-color: #EFEFDF; /* Light beige matching screenshot */
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

if "SUPERSIDE HERO MARQUEE SCROLL" not in css:
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write("\n\n" + marquee_css)
    print("Added Marquee CSS!")
else:
    print("Marquee CSS already exists!")
