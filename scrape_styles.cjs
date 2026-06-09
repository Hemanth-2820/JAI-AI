const puppeteer = require('puppeteer');
const fs = require('fs');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  
  // Set viewport to a standard desktop size
  await page.setViewport({ width: 1440, height: 900 });

  console.log("Navigating to Squarespace Services...");
  await page.goto('https://www.squarespace.com/services', { waitUntil: 'networkidle2' });

  console.log("Evaluating CSS...");
  const styles = await page.evaluate(() => {
    const getStyle = (el) => {
      if (!el) return null;
      const s = window.getComputedStyle(el);
      return {
        padding: s.padding,
        margin: s.margin,
        fontSize: s.fontSize,
        fontWeight: s.fontWeight,
        lineHeight: s.lineHeight,
        letterSpacing: s.letterSpacing,
        color: s.color,
        backgroundColor: s.backgroundColor,
        width: s.width,
        height: s.height,
        gap: s.gap
      };
    };

    return {
      h1: getStyle(document.querySelector('h1')),
      h1Parent: getStyle(document.querySelector('h1')?.parentElement),
      h2: getStyle(document.querySelector('h2')),
      primaryBtn: getStyle(document.querySelector('a[href*="started"]')),
      introSection: getStyle(document.querySelector('#everything-in-one-place')),
      faqSection: getStyle(document.querySelector('.faq-section, section:has(.faq)')),
      conversionSection: getStyle(document.querySelector('section:last-of-type')),
    };
  });

  fs.writeFileSync('squarespace_styles.json', JSON.stringify(styles, null, 2));
  console.log("Styles saved to squarespace_styles.json");

  await browser.close();
})();
