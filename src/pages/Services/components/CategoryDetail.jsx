import React, { useEffect, useState, useRef } from 'react';
import * as LucideIcons from 'lucide-react';
import { motion, useScroll, useTransform } from 'framer-motion';
import styles from '../Services.module.css';

const CategoryDetail = ({ categoryName, data, onBack }) => {
  const processRef = useRef(null);
  const { scrollYProgress } = useScroll({
    target: processRef,
    offset: ["start center", "end center"]
  });

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
              High-performing {
                data.title.toLowerCase().includes('app') ? 'mobile apps' :
                data.title.toLowerCase().includes('software') ? 'software solutions' :
                data.title.toLowerCase().includes('marketing') || data.title.toLowerCase().includes('seo') ? 'digital strategies' :
                data.title.toLowerCase().includes('cloud') ? 'cloud architectures' :
                data.title.toLowerCase().includes('design') ? 'design systems' :
                data.title.toLowerCase().includes('web') ? 'web solutions' :
                `${data.title.toLowerCase()} solutions`
              } <span className={styles.superItalic}>built to grow</span> with your brand
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

      {/* 2.5. Extended Capabilities - ASYMMETRIC GRID DESIGN */}
      {data.extendedCapabilities && data.extendedCapabilities.length > 0 && (
      <section className={styles.superBentoSection} style={{ paddingTop: '0px' }}>
        <p className={styles.superSmallLabel} style={{ paddingLeft: '5%', marginBottom: '40px' }}>CREATIVE CAPABILITIES</p>
        <div className={styles.superAsymGrid} style={{ padding: '0 5%' }}>
           {data.extendedCapabilities.map((feat, idx) => (
             <div key={`asym-${idx}`} className={styles.superAsymCard} style={{ gridColumn: `span ${feat.span || 1}`, border: '1px solid rgba(14, 31, 26, 0.1)' }}>
               <div className={styles.superAsymTextContent}>
                 <h3 className={styles.superAsymCardTitle} style={{ color: '#ffffff' }}>{feat.title}</h3>
                 <p className={styles.superAsymCardDesc} style={{ color: 'rgba(255, 255, 255, 0.9)' }}>{feat.desc}</p>
               </div>
               {(feat.video || feat.image) && (
                 <div className={styles.superAsymImgWrapper}>
                   {feat.video ? (
                     <video src={feat.video} autoPlay loop muted playsInline className={styles.superAsymImg} />
                   ) : (
                     <img src={feat.image} alt={feat.title} className={styles.superAsymImg} />
                   )}
                 </div>
               )}
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
          <div className={styles.superProcessTimeline} ref={processRef}>
            <motion.div 
              className={styles.superProcessLineActive} 
              style={{ scaleY: scrollYProgress }}
            />
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
        <div className={styles.superBottomCtaInner} style={{ backgroundImage: `url(https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=1200&auto=format&fit=crop)` }}>
          <div className={styles.superBottomCtaContent}>
            <h2>Now imagine this <span className={styles.superItalic}>creative power</span> behind your next project</h2>
            <p>This is just one of many creative services—what you do with them is up to you. Let's chat.</p>
            <button className={styles.superBtnLime}>Book a demo</button>
          </div>
        </div>
      </section>

    </div>
  );
};

export default CategoryDetail;
