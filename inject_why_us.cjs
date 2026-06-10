const fs = require('fs');

let content = fs.readFileSync('src/pages/Services/categoryData.js', 'utf8');
content = content.replace('export const categoryData = ', 'module.exports = ');
fs.writeFileSync('tempData.cjs', content);
const data = require('./tempData.cjs');

for (const key in data) {
  const title = data[key].title;
  
  // Custom images based on category
  let image = "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?q=80&w=800&auto=format&fit=crop";
  if (key === 'app-development') image = "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?q=80&w=800&auto=format&fit=crop";
  if (key === 'digital-marketing') image = "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=800&auto=format&fit=crop";

  data[key].whyUs = {
    title: "Why us?",
    desc: `You provide the concept And We provide you with the best technical solution for ${title}. DGT gives assurance and looks after your product requirements. Our team techies are creative and use brand new technologies, and the best tools for analysis and design process to modify your idea into a successful new product.`,
    points: [
      { title: "Strategy:", desc: `Understanding client's ideas and requirements regarding ${title}, Perceiving technical issues, and preparing an advanced solution for it.`, icon: "🎯" },
      { title: "Bracing:", desc: "Our database is secured. We guarantee to safeguard our ideas and our important statistics from our projects. we back up to data, to avoid future interventions.", icon: "📊" },
      { title: "Head Start:", desc: "We as a team are 24x7 available, technically and mentally to thrive in challenges and deliver secure solutions.", icon: "💼" },
      { title: "Analysis:", desc: `Our team analyses and builds a framework, that matches the foreseen ${title} product. Our experts can fix errors. redefine models, and provide maintenance and support. Our services are time bound and we believe in fast and accurate service deliverance.`, icon: "☕" }
    ],
    image: image
  };
}

const outContent = `export const categoryData = ${JSON.stringify(data, null, 2)};`;
fs.writeFileSync('src/pages/Services/categoryData.js', outContent);
fs.unlinkSync('tempData.cjs');
console.log("Injected Why Us data!");
