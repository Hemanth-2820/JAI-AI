import React from 'react';
import styles from './Home.module.css';

const logos = [
  "https://i.postimg.cc/BvxNjs9r/client-1.png",
  "https://i.postimg.cc/rpSgDc2X/client-2.png",
  "https://i.postimg.cc/tghDsyG0/client-3.png",
  "https://i.postimg.cc/3wg9k7QH/client-4.png",
  "https://i.postimg.cc/3wg9k7QT/client-5.png",
  "https://i.postimg.cc/ZYys6gB2/Untitled-design-(1).png",
  "https://i.postimg.cc/C1KTF4mW/Untitled-design-(3).png"
];

const commercialWork = [
  { title: "AUTOTRADER X THE GREAT CELEBRITY BAKE OFF", category: "TV ADVERTISEMENT CAMPAIGN", src: "https://player.vimeo.com/video/1183747661?title=0&byline=0&portrait=0" },
  { title: "ASTRA MAKEUP", category: "AI ADVERTISEMENT", src: "https://player.vimeo.com/video/1180478406?h=42653e0ee9&title=0&byline=0&portrait=0" },
  { title: "DUAE VODKA", category: "AI ADVERTISEMENT", src: "https://player.vimeo.com/video/1100351277?title=0&byline=0&portrait=0" },
  { title: "FOURTEEN SPORTS", category: "AI ADVERTISEMENT", src: "https://player.vimeo.com/video/1088771089?title=0&byline=0&portrait=0" },
  { title: "RICOLA", category: "AI ADVERTISEMENT", src: "https://player.vimeo.com/video/1073485170?title=0&byline=0&portrait=0" }
];

const originalsWork = [
  { title: "LIMBO", category: "EP. 1 AI SERIES", src: "https://player.vimeo.com/video/1177239294?h=b7be91a5b8&title=0&byline=0&portrait=0" },
  { title: "SUPER REY", category: "AI SERIES PILOT", src: "https://player.vimeo.com/video/1163288789?title=0&byline=0&portrait=0" },
  { title: "FREJAI - ETERNAL RHYME", category: "AI MUSIC VIDEO", src: "https://player.vimeo.com/video/1141397657?title=0&byline=0&portrait=0" },
  { title: "THE MAESTRO", category: "AI FASHION FILM", src: "https://player.vimeo.com/video/1124820154?title=0&byline=0&portrait=0" },
  { title: "GREAT GALACTIC WAR", category: "AI MOVIE TRAILER", src: "https://player.vimeo.com/video/1154276656?title=0&byline=0&portrait=0" },
  { title: "BOBBY SOUL - SPICY LIFE", category: "AI MUSIC VIDEO", src: "https://player.vimeo.com/video/1100354069?title=0&byline=0&portrait=0" }
];

const VideoCard = ({ work }) => (
  <div className={styles.videoCard}>
    <div className={styles.portfolioVideoWrapper}>
      <a href={work.src} target="_blank" rel="noopener noreferrer" className={styles.externalLinkBtn} title="Open in Vimeo">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
          <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
          <polyline points="15 3 21 3 21 9"></polyline>
          <line x1="10" y1="14" x2="21" y2="3"></line>
        </svg>
      </a>
      <iframe 
        src={work.src} 
        frameBorder="0" 
        allow="autoplay; fullscreen; picture-in-picture" 
        allowFullScreen
        title={work.title}
        loading="lazy"
      ></iframe>
    </div>
    <div className={styles.cardInfo}>
      <h3 className={styles.workHeading}>{work.title}</h3>
      <p className={styles.workCategory}>{work.category}</p>
    </div>
  </div>
);

const Portfolio = () => {
  return (
    <section className={styles.portfolioSection}>
      {/* Trusted By Section */}
      <div className={styles.trustedByContainer}>
        <h2 className={styles.trustedTitle}>Trusted By</h2>
        <div className={styles.logoSlider}>
          <div className={styles.logoTrack}>
            {/* Double the logos for seamless infinite scrolling */}
            {[...logos, ...logos].map((src, index) => (
              <div key={index} className={styles.logoItem}>
                <img src={src} alt={`Client ${index}`} className={styles.clientLogo} />
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Work Lists */}
      <div className={styles.workContainer}>
        
        {/* Commercial & Brand Work */}
        <div className={styles.workSection}>
          <h2 className={styles.sectionTitle}>Commercial & Brand Work</h2>
          <div className={styles.sliderContainer}>
            {commercialWork.map((work, index) => (
              <VideoCard key={index} work={work} />
            ))}
          </div>
        </div>

        {/* Originals */}
        <div className={styles.workSection}>
          <h2 className={styles.sectionTitle}>Anima Studios Originals</h2>
          <div className={styles.sliderContainer}>
            {originalsWork.map((work, index) => (
              <VideoCard key={index} work={work} />
            ))}
          </div>
        </div>

      </div>
    </section>
  );
};

export default Portfolio;
