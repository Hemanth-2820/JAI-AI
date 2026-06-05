import React from 'react';
import styles from './Home.module.css';

const Contact = () => {
  return (
    <section className={`section ${styles.ctaSection}`}>
      <div className={styles.ctaBgOverlay}></div>
      <div className={`container ${styles.ctaContent}`}>
        <h2 className={styles.ctaTitle}>
          ENTER THE FUTURE OF <br /> VIDEO CONTENT PRODUCTION
        </h2>
        <a href="mailto:info@animastudios.ai" className={styles.ctaButton}>GET IN TOUCH</a>
      </div>
    </section>
  );
};

export default Contact;
