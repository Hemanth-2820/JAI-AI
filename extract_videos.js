import fs from 'fs';
import * as cheerio from 'cheerio';

const html = fs.readFileSync('site.html', 'utf8');
const $ = cheerio.load(html);

const videos = [];

$('.netflix-card').each((i, el) => {
  const iframeSrc = $(el).find('iframe').attr('src');
  const title = $(el).find('h3').text().trim();
  const category = $(el).find('p').text().trim();
  
  if (title) {
    videos.push({ title, category, iframeSrc });
  }
});

fs.writeFileSync('videos.json', JSON.stringify(videos, null, 2));
console.log('Saved to videos.json');
