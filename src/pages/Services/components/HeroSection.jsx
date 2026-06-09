import React from 'react';
import styles from '../Services.module.css';

// Using the exact image provided by the user in the Services/assets folder
import collageImage from '../assets/image.png';

const HeroSection = () => {
  return (
    <section 
      className={styles.heroStaticContainer} 
      style={{ backgroundImage: `url('${collageImage}')` }}
    >
      <div className={styles.heroContentCenter}>
        <h1 className={styles.h1Scale}>The Future of AI Filmmaking</h1>
        <p className={styles.pScale}>
          ANIMA STUDIOS provides <em>end-to-end</em> AI film production—from script generation to 4K cinematic rendering—all powered by the world's most advanced AI models.
        </p>
        <a href="#services-start" className={styles.btnInverse}>Explore Services</a>
      </div>
    </section>
  );
};

export default HeroSection;
