import re

css_path = r'src\pages\Services\Services.module.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

super_css = """
/* =========================================
   SUPERSIDE DESIGN SYSTEM CLASSES
   ========================================= */

@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400;1,500;1,600&display=swap');

.superContainer {
  background-color: #F8F9F5; /* Light beige/white from reference */
  color: #0E1F1A; /* Dark green text */
  font-family: 'Inter', sans-serif;
  width: 100%;
  overflow-x: hidden;
}

.superItalic {
  font-family: 'Playfair Display', serif;
  font-style: italic;
  font-weight: 500;
}

.superSmallLabel {
  font-size: 14px;
  font-weight: 600;
  letter-spacing: 1px;
  text-transform: uppercase;
  margin-bottom: 24px;
  color: inherit;
}

.superBtnGreen {
  background-color: #D3F36B; /* High-viz lime green */
  color: #0E1F1A;
  font-size: 16px;
  font-weight: 600;
  padding: 16px 32px;
  border-radius: 40px;
  border: none;
  cursor: pointer;
  transition: all 0.2s ease;
}

.superBtnGreen:hover {
  background-color: #C1E158;
  transform: scale(1.02);
}

/* 1. Hero Section */
.superHero {
  display: flex;
  background-color: #0E1F1A; /* Dark green background */
  color: #FFFFFF;
  padding: 100px 5% 0 5%;
  min-height: 80vh;
  align-items: center;
  position: relative;
  overflow: hidden;
}

.superHeroContent {
  width: 50%;
  padding-right: 5%;
  z-index: 2;
}

.superCategoryLabel {
  font-size: 14px;
  letter-spacing: 1.5px;
  margin-bottom: 30px;
  text-transform: uppercase;
  color: rgba(255,255,255,0.7);
}

.superHeroTitle {
  font-size: clamp(40px, 5vw, 72px);
  line-height: 1.1;
  font-weight: 500;
  margin-bottom: 30px;
}

.superHeroDesc {
  font-size: 20px;
  line-height: 1.5;
  color: rgba(255,255,255,0.8);
  margin-bottom: 40px;
  max-width: 600px;
}

.superHeroImageWrapper {
  width: 50%;
  position: absolute;
  right: 0;
  bottom: -50px;
  height: 80%;
  display: flex;
  align-items: flex-end;
}

.superHeroImg {
  width: 100%;
  height: 100%;
  object-fit: contain;
  object-position: bottom right;
}

/* 2. Bento Grid */
.superBentoSection {
  padding: 100px 5%;
  background-color: #F8F9F5;
}

.superBentoGrid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 24px;
}

.superBentoCard {
  position: relative;
  border-radius: 24px;
  overflow: hidden;
  min-height: 400px;
  background-color: #E2E4DB;
  transition: transform 0.3s ease;
}

.superBentoCard:hover {
  transform: translateY(-5px);
}

.superBentoCardBg {
  position: absolute;
  top: 0; left: 0; width: 100%; height: 100%;
  background-size: cover;
  background-position: center;
  opacity: 0.6;
}

.superBentoCardContent {
  position: absolute;
  top: 0; left: 0; width: 100%; height: 100%;
  padding: 40px;
  display: flex;
  flex-direction: column;
  color: #0E1F1A;
  background: linear-gradient(to bottom, rgba(248,249,245,0.9) 0%, rgba(248,249,245,0.2) 100%);
}

.superBentoCardContent h3 {
  font-size: 28px;
  font-weight: 500;
  margin-bottom: 16px;
}

.superBentoCardContent p {
  font-size: 16px;
  line-height: 1.5;
  color: rgba(14, 31, 26, 0.8);
}

/* 3. Split Section */
.superSplit {
  display: flex;
  padding: 100px 5%;
  align-items: center;
  background-color: #F8F9F5;
}

.superSplitLeft {
  width: 50%;
  padding-right: 8%;
}

.superSplitTitle {
  font-size: clamp(36px, 4.5vw, 64px);
  line-height: 1.1;
  font-weight: 500;
  margin-bottom: 30px;
}

.superSplitDesc {
  font-size: 20px;
  line-height: 1.6;
  color: rgba(14, 31, 26, 0.8);
}

.superSplitRight {
  width: 50%;
}

.superSplitImg {
  width: 100%;
  border-radius: 24px;
  object-fit: cover;
}

/* 4. Metrics Section */
.superMetricsSection {
  padding: 120px 5%;
  text-align: center;
  background-color: #F8F9F5;
}

.superMetricsLabel {
  font-size: 14px;
  letter-spacing: 1.5px;
  color: rgba(14, 31, 26, 0.5);
  margin-bottom: 20px;
}

.superMetricsTitle {
  font-size: clamp(32px, 4vw, 56px);
  line-height: 1.2;
  font-weight: 500;
  margin-bottom: 80px;
}

.superMetricsGrid {
  display: flex;
  justify-content: space-between;
  border-top: 1px solid rgba(14, 31, 26, 0.1);
  padding-top: 60px;
}

.superMetricCard {
  flex: 1;
  padding: 0 40px;
  text-align: left;
  border-right: 1px solid rgba(14, 31, 26, 0.1);
}

.superMetricCard:last-child {
  border-right: none;
}

.superMetricCard h3 {
  font-size: clamp(60px, 8vw, 120px);
  font-weight: 400;
  font-family: 'Playfair Display', serif;
  margin-bottom: 20px;
  line-height: 1;
}

.superMetricCard p {
  font-size: 18px;
  line-height: 1.5;
  color: rgba(14, 31, 26, 0.7);
}

/* 5. Ecosystems (Icon Grid) */
.superEcosystems {
  background-color: #0E1F1A;
  color: #FFFFFF;
  padding: 120px 5%;
}

.superEcosystemsTitle {
  font-size: clamp(32px, 4vw, 56px);
  line-height: 1.2;
  font-weight: 500;
  text-align: center;
  max-width: 900px;
  margin: 0 auto 80px auto;
}

.superEcoGrid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 40px;
}

.superEcoCard {
  padding-right: 20px;
}

.superEcoIcon {
  width: 60px;
  height: 60px;
  background-color: rgba(255,255,255,0.05);
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 30px;
}

.superEcoCard h3 {
  font-size: 24px;
  font-weight: 500;
  margin-bottom: 16px;
}

.superEcoCard p {
  font-size: 16px;
  line-height: 1.6;
  color: rgba(255,255,255,0.6);
}

/* 6. Process Section */
.superProcessSection {
  display: flex;
  padding: 120px 5%;
  background-color: #0E1F1A;
  color: #FFFFFF;
}

.superProcessSticky {
  width: 40%;
  position: sticky;
  top: 120px;
  height: fit-content;
  padding-right: 10%;
}

.superProcessTitle {
  font-size: clamp(36px, 4.5vw, 64px);
  line-height: 1.1;
  font-weight: 500;
  margin-bottom: 30px;
}

.superProcessSticky p {
  font-size: 18px;
  line-height: 1.6;
  color: rgba(255,255,255,0.7);
}

.superProcessTimeline {
  width: 60%;
  padding-left: 5%;
  border-left: 1px solid rgba(255,255,255,0.2);
}

.superProcessStep {
  position: relative;
  padding-bottom: 100px;
  padding-left: 60px;
}

.superProcessStep:last-child {
  padding-bottom: 0;
}

.superStepCircle {
  position: absolute;
  left: -24px;
  top: 0;
  width: 48px;
  height: 48px;
  border-radius: 50%;
  border: 1px solid #FFFFFF;
  background-color: #0E1F1A;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  font-family: 'Playfair Display', serif;
}

.superStepContent h3 {
  font-size: 28px;
  font-weight: 500;
  margin-bottom: 16px;
}

.superStepContent p {
  font-size: 18px;
  line-height: 1.6;
  color: rgba(255,255,255,0.7);
}

/* 7. Bottom CTA */
.superBottomCta {
  padding: 0 5% 100px 5%;
  background-color: #0E1F1A;
}

.superBottomCtaInner {
  border-radius: 24px;
  overflow: hidden;
  background-size: cover;
  background-position: center;
  position: relative;
  min-height: 600px;
  display: flex;
  align-items: center;
  padding: 80px;
}

.superBottomCtaContent {
  position: relative;
  z-index: 2;
  max-width: 600px;
  color: #FFFFFF;
}

.superBottomCtaContent h2 {
  font-size: clamp(40px, 5vw, 64px);
  line-height: 1.1;
  font-weight: 500;
  margin-bottom: 24px;
}

.superBottomCtaContent p {
  font-size: 20px;
  line-height: 1.5;
  margin-bottom: 40px;
}

/* Mobile Responsiveness */
@media (max-width: 1024px) {
  .superHero, .superSplit, .superProcessSection {
    flex-direction: column;
  }
  .superHeroContent, .superHeroImageWrapper, .superSplitLeft, .superSplitRight, .superProcessSticky, .superProcessTimeline {
    width: 100%;
  }
  .superHeroImageWrapper {
    position: relative;
    height: 400px;
    margin-top: 50px;
  }
  .superMetricsGrid, .superEcoGrid {
    flex-direction: column;
    grid-template-columns: 1fr;
  }
  .superMetricCard {
    border-right: none;
    border-bottom: 1px solid rgba(14, 31, 26, 0.1);
    padding: 40px 0;
  }
}
"""

if "SUPERSIDE DESIGN SYSTEM CLASSES" not in css:
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write("\n\n" + super_css)
    print("Appended Superside CSS to Services.module.css")
else:
    print("Superside CSS already appended!")
