import React from 'react';
import styles from './AboutUs.module.css';

const AboutUs = () => {
  return (
    <div className={styles.aboutContainer}>
      {/* Hero Banner Section */}
      <section className={styles.heroBanner}>
        <div className={styles.heroBannerContent}>
          <div className={styles.heroTextSide}>
            <div className={styles.breadcrumbs}>
              <span>About JAI Tech</span> <br />
              <strong>Leadership & Vision</strong>
            </div>
            <h1 className={styles.heroTitle}>
              Get to know<br />our leaders
            </h1>
            <p className={styles.heroSubtitle}>
              We are the engineers building<br />your digital future.
            </p>
          </div>
        </div>
        <div className={styles.heroImageSide}>
          <div className={styles.heroImageWrapper}>
            {/* The image goes here via CSS background */}
          </div>
          <div className={styles.heroGradientCorner}></div>
        </div>
      </section>



      {/* Values Section */}
      <section className={styles.capValuesWrapper}>
        <div className={styles.capSectionHeader}>
          <h2 className={styles.capSectionTitle}>What Drives Every Build</h2>
        </div>

        {/* Value 1: Innovation */}
        <div className={styles.capOverlapSection}>
          <div className={styles.capOverlapContainer}>
            <div className={styles.capImageRight}>
              <img src="https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?q=80&w=1200&auto=format&fit=crop" alt="Innovation" />
            </div>
            <div className={`${styles.capTextLeft} ${styles.cardInnovation}`}>
              <h2>Innovation</h2>
              <p>
                We embrace emerging tech to solve hard problems with elegant, future-proof solutions. By continuously pushing boundaries, we ensure your infrastructure is always ahead of the curve.
              </p>
            </div>
          </div>
        </div>

        {/* Value 2: Reliability */}
        <div className={styles.capOverlapSection}>
          <div className={`${styles.capOverlapContainer} ${styles.reverseLayout}`}>
            <div className={styles.capImageLeft}>
              <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?q=80&w=1200&auto=format&fit=crop" alt="Reliability" />
            </div>
            <div className={`${styles.capTextRight} ${styles.cardReliability}`}>
              <h2>Reliability</h2>
              <p>
                Mission-critical systems engineered for 99.99% uptime and bulletproof resilience. We build architecture you can trust, no matter the scale or complexity of your operations.
              </p>
            </div>
          </div>
        </div>

        {/* Value 3: Transparency */}
        <div className={styles.capOverlapSection}>
          <div className={styles.capOverlapContainer}>
            <div className={styles.capImageRight}>
              <img src="https://images.unsplash.com/photo-1552664730-d307ca884978?q=80&w=1200&auto=format&fit=crop" alt="Transparency" />
            </div>
            <div className={`${styles.capTextLeft} ${styles.cardTransparency}`}>
              <h2>Transparency</h2>
              <p>
                Clear communication and honest delivery at every stage of your project journey. We believe that open collaboration is the foundation of every successful partnership.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Founder Section */}
      <section className={styles.founderSection}>
        <div className={styles.founderContainer}>
          <div className={styles.founderImageCol}>
            <div className={styles.founderImageWrapper}>
              <img src="https://images.unsplash.com/photo-1560250097-0b93528c311a?q=80&w=800&auto=format&fit=crop" alt="Founder" className={styles.founderImg} />
            </div>
          </div>
          <div className={styles.founderContentCol}>
            <h2 className={styles.founderName}>Jatin Dalal</h2>
            <h3 className={styles.founderRole}>Founder & CEO</h3>
            <div className={styles.founderDivider}></div>
            <div className={styles.founderBio}>
              <p>
                Jatin Dalal is the Founder and CEO of JAI Tech. In his role, Jatin oversees the company's worldwide strategic vision, financial planning, and enterprise growth. With a deep passion for digital transformation, he leads our mission to architect the future of business.
              </p>
              <p>
                Prior to founding JAI Tech, Jatin served in numerous executive leadership positions at top-tier multinational technology services companies. His extensive background in corporate development and risk management has shaped JAI Tech into a resilient, innovation-driven powerhouse.
              </p>
            </div>
          </div>
        </div>
      </section>




    </div>
  );
};

export default AboutUs;
