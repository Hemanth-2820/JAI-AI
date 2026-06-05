import fs from 'fs';
import * as cheerio from 'cheerio';

const html = fs.readFileSync('site.html', 'utf8');
const $ = cheerio.load(html);

const data = {
  title: $('title').text(),
  metaDesc: $('meta[name="description"]').attr('content'),
  styles: [],
  cssLinks: [],
  images: [],
  videos: [],
  sections: [],
  theme: {}
};

// Get CSS Links
$('link[rel="stylesheet"]').each((i, el) => {
  data.cssLinks.push($(el).attr('href'));
});

// Get Inline Styles
$('style').each((i, el) => {
  const content = $(el).html();
  if (content.includes('--') || content.includes('font-') || content.includes('color')) {
    data.styles.push(content.substring(0, 500) + '...[truncated]'); // save first part just to see
  }
});

// Get Images
$('img').each((i, el) => {
  data.images.push({
    src: $(el).attr('src') || $(el).attr('data-src'),
    alt: $(el).attr('alt'),
    class: $(el).attr('class')
  });
});

// Get Videos
$('video').each((i, el) => {
  data.videos.push({
    src: $(el).attr('src') || $(el).find('source').attr('src'),
    poster: $(el).attr('poster')
  });
});

// Get Sections and Content
// Squarespace usually uses 'section' or elements with specific classes like 'page-section'
const sectionSelector = 'section, .page-section, .sqs-layout, [data-section-id]';

$(sectionSelector).each((i, el) => {
  const section = {
    id: $(el).attr('id') || `section-${i}`,
    classes: $(el).attr('class'),
    headings: [],
    paragraphs: [],
    links: [],
    backgrounds: []
  };

  // Find headings
  $(el).find('h1, h2, h3, h4').each((j, h) => {
    section.headings.push({ tag: h.tagName, text: $(h).text().trim().replace(/\s+/g, ' ') });
  });

  // Find paragraphs
  $(el).find('p').each((j, p) => {
    const text = $(p).text().trim().replace(/\s+/g, ' ');
    if (text) section.paragraphs.push(text);
  });

  // Find links/buttons
  $(el).find('a, button').each((j, a) => {
    const text = $(a).text().trim().replace(/\s+/g, ' ');
    if (text) section.links.push({ text, href: $(a).attr('href') });
  });

  // Look for section background images if they exist as inline styles
  const bgImage = $(el).find('.section-background img, .sqs-block-image img');
  bgImage.each((j, img) => {
    section.backgrounds.push($(img).attr('src') || $(img).attr('data-src'));
  });

  // Only add if it actually has content
  if (section.headings.length > 0 || section.paragraphs.length > 0) {
    data.sections.push(section);
  }
});

fs.writeFileSync('analysis.json', JSON.stringify(data, null, 2));
console.log('Analysis saved to analysis.json');
