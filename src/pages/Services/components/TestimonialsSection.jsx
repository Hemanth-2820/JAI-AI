import React from 'react';
import styles from '../Services.module.css';

const TestimonialsSection = ({ testimonials }) => {
  return (
    <section className={styles.testimonialsSection}>
      <div className={styles.masonryGrid}>
        
        {/* Column 1: Text Top, Image Bottom */}
        <div className={styles.masonryColumn}>
          <div className={styles.masonryTextCard}>
            <blockquote>“{testimonials[0]?.quote}”</blockquote>
            <p>{testimonials[0]?.author}</p>
          </div>
          <div className={styles.masonryImageCardPortrait}>
            {testimonials[0]?.img && <img src={testimonials[0].img} alt="" loading="lazy" />}
          </div>
        </div>

        {/* Column 2: Image Top, Text Bottom */}
        <div className={styles.masonryColumn}>
          <div className={styles.masonryImageCardSquare}>
            {testimonials[1]?.img && <img src={testimonials[1].img} alt="" loading="lazy" />}
          </div>
          <div className={styles.masonryTextCard}>
            <blockquote>“{testimonials[1]?.quote}”</blockquote>
            <p>{testimonials[1]?.author}</p>
          </div>
        </div>

        {/* Column 3: Text Top, Image Bottom */}
        <div className={styles.masonryColumn}>
          <div className={styles.masonryTextCard}>
            <blockquote>“{testimonials[2]?.quote}”</blockquote>
            <p>{testimonials[2]?.author}</p>
          </div>
          <div className={styles.masonryImageCardPortrait}>
            {testimonials[2]?.img && <img src={testimonials[2].img} alt="" loading="lazy" />}
          </div>
        </div>

      </div>
    </section>
  );
};

export default TestimonialsSection;
