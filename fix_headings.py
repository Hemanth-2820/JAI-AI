import re

css_path = r'src\pages\Services\Services.module.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Append explicit color resets to the very bottom to ensure they override global rules
fix_css = """

/* =========================================
   SUPERSIDE TYPOGRAPHY COLOR FIXES
   ========================================= */

/* Force dark text on light backgrounds */
.superSplitTitle,
.superBentoCardContent h3,
.superMetricsTitle,
.superMetricCard h3 {
  color: #0E1F1A !important;
}

/* Force light text on dark backgrounds */
.superHeroTitle,
.superEcosystemsTitle,
.superEcoCard h3,
.superProcessTitle,
.superStepContent h3,
.superBottomCtaContent h2 {
  color: #FFFFFF !important;
}

/* Ensure descriptions also inherit correctly if global rules exist */
.superSplitDesc,
.superBentoCardContent p,
.superMetricCard p {
  color: rgba(14, 31, 26, 0.8) !important;
}

.superHeroDesc,
.superEcoCard p,
.superStepContent p,
.superBottomCtaContent p {
  color: rgba(255, 255, 255, 0.8) !important;
}

"""

with open(css_path, 'a', encoding='utf-8') as f:
    f.write(fix_css)

print("Appended color overrides!")
