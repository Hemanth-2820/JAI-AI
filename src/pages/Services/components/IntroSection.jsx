import React, { useState, useEffect } from 'react';
import styles from '../Services.module.css';

const IntroSection = ({ introFeatures, onSelectDetail }) => {
  const [activeIndex, setActiveIndex] = useState(0);

  // Auto-play loop
  useEffect(() => {
    const timer = setInterval(() => {
      setActiveIndex((prev) => (prev + 1) % introFeatures.length);
    }, 4000); // 4 seconds per item
    return () => clearInterval(timer);
  }, [introFeatures.length]);

  const handleLinkClick = (e, linkText) => {
    e.preventDefault();
    const linkMap = {
      "Explore creative consulting→": "ai-creative-consulting",
      "Explore script development→": "ai-script-development",
      "Explore storyboarding→": "ai-storyboarding"
    };
    if (onSelectDetail && linkMap[linkText]) {
      onSelectDetail(linkMap[linkText]);
    }
  };

  return (
    <section className={styles.introSliderSection}>
      <div className={styles.introSliderContainer}>
        {/* Left Side: Fixed Titles and Details */}
        <div className={styles.introSliderLeft}>
          
          {/* Static list of titles */}
          <div className={styles.introSliderList} style={{ marginBottom: '24px' }}>
            {introFeatures.map((feat, idx) => {
              const isActive = idx === activeIndex;
              return (
                <div 
                  key={idx} 
                  className={`${styles.introSliderItem} ${isActive ? styles.introSliderItemActive : ''}`}
                  onClick={() => setActiveIndex(idx)}
                >
                  <h3 className={styles.introSliderTitle}>
                    {feat.title}
                  </h3>
                </div>
              )
            })}
          </div>

          {/* Description ALWAYS at the bottom of the list */}
          <div className={styles.introSliderDetails} style={{ minHeight: '110px', marginBottom: '24px' }}>
            <p className={styles.introSliderDesc}>{introFeatures[activeIndex].desc}</p>
            <a 
              href="#" 
              className={styles.introSliderLink}
              onClick={(e) => handleLinkClick(e, introFeatures[activeIndex].link)}
            >
              {introFeatures[activeIndex].link}
            </a>
          </div>
          
          {/* Controls */}
          <div className={styles.introSliderControls}>
            <div className={styles.introSliderDots}>
              {introFeatures.map((_, idx) => (
                <button 
                  key={idx} 
                  className={`${styles.introSliderDot} ${idx === activeIndex ? styles.introSliderDotActive : ''}`}
                  onClick={() => setActiveIndex(idx)}
                  aria-label={`Go to slide ${idx + 1}`}
                />
              ))}
            </div>
            <button className={styles.introSliderPlayPause}>▶</button>
          </div>
        </div>

        {/* Right Side: Images */}
        <div className={styles.introSliderRight}>
          <div className={styles.introSliderImageContainer}>
            {introFeatures.map((feat, idx) => (
              <img 
                key={idx}
                src={feat.img} 
                alt={feat.title} 
                className={`${styles.introSliderImage} ${idx === activeIndex ? styles.activeImgDisplay : ''}`}
              />
            ))}
          </div>
        </div>
      </div>
    </section>
  );
};

export default IntroSection;
