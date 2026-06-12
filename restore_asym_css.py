import re

css_path = r'src\pages\Services\Services.module.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# I will cleanly append the full Asymmetric CSS without any nth-child overrides.
asym_css = """
/* =========================================
   ASYMMETRIC BENTO GRID (CREATIVE CAPABILITIES)
   ========================================= */

.superAsymGrid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
}

.superAsymCard {
  position: relative;
  border-radius: 24px;
  overflow: hidden;
  min-height: 480px;
  background-color: #E2E4DB;
  transition: transform 0.3s ease;
}

.superAsymCard:hover {
  transform: translateY(-4px);
}

.superAsymTextContent {
  position: absolute;
  top: 0; left: 0; width: 100%;
  padding: 40px;
  z-index: 2;
}

.superAsymCardTitle {
  font-size: 28px;
  font-weight: 500;
  margin-bottom: 16px;
}

.superAsymCardDesc {
  font-size: 16px;
  line-height: 1.6;
}

.superAsymImgWrapper {
  position: absolute;
  bottom: 0; right: 0; width: 100%; height: 55%;
  display: flex;
  align-items: flex-end;
  justify-content: flex-end;
  overflow: hidden;
}

.superAsymImg {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: bottom;
  mask-image: linear-gradient(to bottom, transparent 0%, black 20%);
  -webkit-mask-image: linear-gradient(to bottom, transparent 0%, black 20%);
}

@media (max-width: 1024px) {
  .superAsymGrid {
    grid-template-columns: repeat(2, 1fr);
  }
  .superAsymCard {
    grid-column: span 1 !important;
  }
}

@media (max-width: 600px) {
  .superAsymGrid {
    grid-template-columns: 1fr;
  }
}
"""

# Remove any broken remnants of superAsym CSS
css = re.sub(r'/\*\s*={41}\s*ASYMMETRIC BENTO GRID\s*={41}\s*\*/[\s\S]*?(?=\n\n/\*|\Z)', '', css)
css = re.sub(r'\.superAsym[a-zA-Z0-9_-]+\s*\{[^}]+\}', '', css)

css += "\n\n" + asym_css

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Restored clean superAsym CSS!")
