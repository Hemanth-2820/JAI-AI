import React, { useEffect, useState } from 'react';
import * as LucideIcons from 'lucide-react';
import styles from '../Services.module.css';

const CategoryDetail = ({ categoryName, data, onBack }) => {
  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);

  if (!data) return null;

  return (
    <div className={styles.superContainer}>

      {/* 1. Hero Section */}
      <section className={styles.superHero}>
        <div className={styles.superHeroInner}>
          <div className={styles.superHeroContent}>
            <p className={styles.superCategoryLabel}>{data.title.toUpperCase()} SERVICES</p>
            <h1 className={styles.superHeroTitle}>
              High-performing web solutions <span className={styles.superItalic}>built to grow</span> with your brand
            </h1>
            <p className={styles.superHeroDesc}>{data.description}</p>
            <button className={styles.superBtnGreen}>Book a demo</button>
          </div>
          <div className={styles.superHeroImageWrapper}>
            <img src={data.heroImage} alt={data.title} className={styles.superHeroImg} />
          </div>
        </div>

        {/* Horizontal Marquee / Capabilities Scroll */}
        {data.features && data.features.length > 0 && (
          <div className={styles.superHeroMarquee}>
            <div className={styles.superMarqueeTrack}>
              {data.features.map((feat, idx) => (
                <div key={`mq1-${idx}`} className={styles.superMarqueeCard}>
                  <img src={feat.image} alt={feat.title} className={styles.superMarqueeImg} />
                  <span className={styles.superMarqueeText}>{feat.title}</span>
                </div>
              ))}
              {data.features.map((feat, idx) => (
                <div key={`mq2-${idx}`} className={styles.superMarqueeCard}>
                  <img src={feat.image} alt={feat.title} className={styles.superMarqueeImg} />
                  <span className={styles.superMarqueeText}>{feat.title}</span>
                </div>
              ))}
            </div>
          </div>
        )}
      </section>

      {/* 2. Bento Grid ("What we offer" / Features) */}
      {data.features && data.features.length > 0 && (
        <section className={styles.superBentoSection}>
          <div className={styles.superBentoGrid}>
            {data.features.map((feat, idx) => (
              <div key={idx} className={styles.superBentoCard}>
                <img src={feat.image} alt={feat.title} className={styles.superBentoImg} />

                <div className={styles.superBentoDefault}>
                  <h3>{feat.title}</h3>
                </div>

                <div className={styles.superBentoHover}>
                  <h3>{feat.title}</h3>
                  <p>{feat.desc}</p>
                </div>
              </div>
            ))}
          </div>
        </section>
      )}

      {/* 3. Split Text & Image ("Why Web") */}
      <section className={styles.superSplit}>
        <div className={styles.superSplitLeft}>
          <p className={styles.superSmallLabel}>WHY {data.title.toUpperCase()}?</p>
          <h2 className={styles.superSplitTitle}>
            Your digital presence isn't a billboard, it's a <span className={styles.superItalic}>growth engine</span>
          </h2>
          <p className={styles.superSplitDesc}>
            {data.description}
          </p>
        </div>
        <div className={styles.superSplitRight}>
          <img src={data.heroImage} alt="Growth" className={styles.superSplitImg} />
        </div>
      </section>

      {/* 4. Metrics That Matter */}
      {data.metrics && (
        <section className={styles.superMetricsSection}>
          <p className={styles.superMetricsLabel}>METRICS THAT MATTER</p>
          <h2 className={styles.superMetricsTitle}>
            A creative {data.title.toLowerCase()} partner <br /> you can trust
          </h2>
          <div className={styles.superMetricsGrid}>
            {data.metrics.map((m, idx) => (
              <div key={idx} className={styles.superMetricCard}>
                <h3>{m.value}</h3>
                <p>{m.label}</p>
              </div>
            ))}
          </div>
        </section>
      )}

      {/* 5. Icon Grid / Digital Ecosystems */}
      {data.techStack && (
        <section className={styles.superEcosystems}>
          <h2 className={styles.superEcosystemsTitle}>
            <span className={styles.superItalic}>Digital ecosystems</span> that scale across markets, campaigns, and segments
          </h2>
          <div className={styles.superEcoGrid}>
            {data.techStack.map((tech, idx) => {
              const Icon = LucideIcons['Code'] || LucideIcons.Monitor;
              return (
                <div key={idx} className={styles.superEcoCard}>
                  <div className={styles.superEcoIcon}><Icon size={24} /></div>
                  <h3>{tech}</h3>
                  <p>Scalable, performance-driven solutions built fast using {tech}.</p>
                </div>
              )
            })}
          </div>
        </section>
      )}

      {/* 6. Process Timeline ("Website workflows") */}
      {data.process && (
        <section className={styles.superProcessSection}>
          <div className={styles.superProcessSticky}>
            <p className={styles.superSmallLabel}>OUR PROCESS</p>
            <h2 className={styles.superProcessTitle}>
              {data.title} workflows, <br /><span className={styles.superItalic}>minus the friction</span>
            </h2>
            <p>No more handoffs, holdups, or creative guesswork. Just a proven system for scalable, brand-aligned solutions.</p>
          </div>
          <div className={styles.superProcessTimeline}>
            {data.process.map((step, idx) => (
              <div key={idx} className={styles.superProcessStep}>
                <div className={styles.superStepCircle}>{idx + 1}</div>
                <div className={styles.superStepContent}>
                  <h3>{step.title}</h3>
                  <p>{step.desc}</p>
                </div>
              </div>
            ))}
          </div>
        </section>
      )}

      {/* 7. Bottom CTA Overlay */}
      <section className={styles.superBottomCta}>
        <div className={styles.superBottomCtaInner} style={{ backgroundImage: `url(${data.heroImage})` }}>
          <div className={styles.superBottomCtaContent}>
            <h2>Now imagine this <span className={styles.superItalic}>creative power</span> behind your next project</h2>
            <p>This is just one of many creative services—what you do with them is up to you. Let's chat.</p>
            <button className={styles.superBtnGreen}>Book a demo</button>
          </div>
        </div>
      </section>

    </div>
  );
};

export default CategoryDetail;
