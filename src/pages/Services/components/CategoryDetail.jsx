import React, { useEffect } from 'react';
import styles from '../Services.module.css';

const CategoryDetail = ({ categoryName, data, onBack }) => {
  // Scroll to top when this mounts
  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);

  if (!data) return null;

  return (
    <div className={styles.catDetailContainer}>
      
      {/* Premium Transparent Header */}
      <div className={styles.catHeader}>
        <button className={styles.catBackButton} onClick={onBack}>
          <span className={styles.catBackArrow}>←</span> Back
        </button>
        <div className={styles.catBrand}>ANIMA STUDIOS</div>
      </div>

      {/* Cinematic Hero Section */}
      <section className={styles.catHero}>
        <div 
          className={styles.catHeroBg} 
          style={{ backgroundImage: `url('${data.heroImage}')` }}
        ></div>
        <div className={styles.catHeroOverlay}></div>
        <div className={styles.catHeroContent}>
          <div className={styles.catHeroLabel}>Capabilities / {data.title}</div>
          <h1 className={styles.catHeroTitle}>
            {data.title.split(' ').map((word, i) => (
              <span key={i} className={i % 2 === 0 ? styles.textSolid : styles.textOutline}>{word} </span>
            ))}
          </h1>
          <p className={styles.catHeroDesc}>{data.description}</p>
        </div>
        
        <div className={styles.catScrollIndicator}>
          <span>Scroll</span>
          <div className={styles.catScrollLine}></div>
        </div>
      </section>

      {/* Premium Minimalist Features List */}
      <section className={styles.catFeatures}>
        <div className={styles.catSectionHead}>
          <h2>The approach.</h2>
          <p>{data.subtitle}</p>
        </div>
        <div className={styles.catFeatureWrapper}>
          {data.features.map((feat, idx) => (
            <div key={idx} className={styles.catFeatureRow}>
              <div className={styles.catFeatNum}>0{idx + 1}</div>
              <div className={styles.catFeatContent}>
                <h3>{feat.title}</h3>
                <p>{feat.desc}</p>
              </div>
              <div className={styles.catFeatIcon}>{feat.icon}</div>
            </div>
          ))}
        </div>
      </section>

      {/* Editorial Asymmetric Gallery */}
      <section className={styles.catGallery}>
        <div className={styles.catSectionHead}>
          <h2>Selected highlights.</h2>
          <p>A glimpse into what's possible.</p>
        </div>
        <div className={styles.catGrid}>
          {data.masonryImages.map((img, idx) => (
            <div key={idx} className={`${styles.catGridItem} ${styles[`catGridItem${idx}`]}`}>
              <div className={styles.catImgWrapper}>
                <img src={img} alt={`Highlight ${idx}`} />
                <div className={styles.catImgOverlay}>
                  <span>Explore +</span>
                </div>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* Massive Bold CTA */}
      <section className={styles.catCta}>
        <div className={styles.catCtaContent}>
          <h2>Ready to elevate your {data.title.toLowerCase()}?</h2>
          <button className={styles.catCtaBtn}>Start Your Journey ↗</button>
        </div>
      </section>

    </div>
  );
};

export default CategoryDetail;
