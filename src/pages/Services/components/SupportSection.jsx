import React from 'react';
import styles from '../Services.module.css';

const SupportSection = () => {
  return (
    <section className={styles.supportSection}>
      <div className={styles.supportContainer}>
        <h2 className={`${styles.h2Scale} ${styles.supportTitle}`}>Studio Resources</h2>
        <div className={styles.supportGrid}>
          <a href="#production-support" className={styles.supportCard}>
            <div className={styles.supportCardContent}>
              <h3>Production Support</h3>
              <p className={styles.pScale}>Get 24/7 technical and creative support from our AI film specialists.</p>
            </div>
            <span className={styles.supportArrow}>→</span>
          </a>
          <a href="#workshops" className={styles.supportCard}>
            <div className={styles.supportCardContent}>
              <h3>Creative Workshops</h3>
              <p className={styles.pScale}>Join exclusive online sessions to master AI storytelling and prompt engineering.</p>
            </div>
            <span className={styles.supportArrow}>→</span>
          </a>
        </div>
      </div>
    </section>
  );
};

export default SupportSection;
