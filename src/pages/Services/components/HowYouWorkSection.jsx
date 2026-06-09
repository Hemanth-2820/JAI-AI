import React, { useState, useEffect } from 'react';
import styles from '../Services.module.css';

const HowYouWorkSection = ({ workTypes, onSelectCategory }) => {
  // Start in the middle of the cloned array
  const [activeIndex, setActiveIndex] = useState(workTypes.length);
  const [isTransitioning, setIsTransitioning] = useState(true);

  // Triple the array so we always have items on the left and right
  const extendedWorkTypes = [...workTypes, ...workTypes, ...workTypes];

  useEffect(() => {
    const timer = setInterval(() => {
      setIsTransitioning(true);
      setActiveIndex((prev) => prev + 1);
    }, 4000); 
    return () => clearInterval(timer);
  }, []);

  const handleTransitionEnd = () => {
    // If we've scrolled past the middle set, silently snap back to the exact same position in the middle set
    if (activeIndex >= workTypes.length * 2) {
      setIsTransitioning(false);
      setActiveIndex(activeIndex - workTypes.length);
    }
  };

  return (
    <section className={styles.howYouWorkSection}>
      <div className={styles.howYouWorkHeaderLayout}>
        <h2 className={styles.howYouWorkTitle}>Our specialized production streams</h2>
        <p className={styles.howYouWorkDesc}>From high-end commercial work to full feature films and animated experiences, ANIMA STUDIOS powers your cinematic vision.</p>
      </div>

      <div className={styles.howYouWorkCarouselWrapper}>
        <div 
          className={styles.howYouWorkTrack}
          style={{ 
            '--active-index': activeIndex,
            // Math to perfectly center 2 cards on screen:
            // 50vw is center. We offset left by the distance to the gap between activeIndex and activeIndex+1
            transform: `translateX(calc(50vw - (var(--active-index) * (var(--card-width) + var(--card-gap)) + var(--card-width) + var(--card-gap) / 2)))`,
            transition: isTransitioning ? 'transform 0.6s cubic-bezier(0.25, 1, 0.5, 1)' : 'none'
          }}
          onTransitionEnd={handleTransitionEnd}
        >
          {extendedWorkTypes.map((type, idx) => (
            <div 
              key={idx} 
              className={styles.workTypeCardSlider}
              onClick={() => onSelectCategory(type.id)}
              style={{ cursor: 'pointer' }}
            >
              <img src={type.img} alt={type.title} className={styles.workTypeImgSlider} loading="lazy" />
              <div className={styles.workTypeLabelSlider}>
                <span>{type.title}</span>
                <span>→</span>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Controls */}
      <div className={styles.howYouWorkControls}>
        <div className={styles.introSliderDots}>
          {workTypes.map((_, idx) => {
            const displayIndex = activeIndex % workTypes.length;
            return (
              <button 
                key={idx} 
                className={`${styles.introSliderDot} ${displayIndex === idx ? styles.introSliderDotActive : ''}`}
                onClick={() => {
                  setIsTransitioning(true);
                  setActiveIndex(workTypes.length + idx);
                }}
                aria-label={`Go to slide ${idx + 1}`}
              />
            )
          })}
        </div>
        <button className={styles.introSliderPlayPause}>||</button>
      </div>
    </section>
  );
};

export default HowYouWorkSection;
