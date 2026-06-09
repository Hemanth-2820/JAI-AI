import React from 'react';
import styles from '../Services.module.css';

const ConversionSection = ({ onSelectDetail }) => {
  return (
    <section className={styles.conversionSection}>
      <div className={styles.conversionContainer}>
        <div className={styles.conversionContent}>
          <h2 className={`${styles.h1Scale} ${styles.conversionTitle}`}>Start your production journey today</h2>
          <p className={styles.conversionSubtitle}>Book a free consultation. <strong>Bring your vision to life.</strong></p>
          <div className={styles.conversionActions}>
            <a 
              href="#" 
              className={styles.btnInverse}
              onClick={(e) => {
                e.preventDefault();
                if (onSelectDetail) onSelectDetail("get-started");
              }}
            >
              Get started
            </a>
          </div>
        </div>
      </div>
    </section>
  );
};

export default ConversionSection;
