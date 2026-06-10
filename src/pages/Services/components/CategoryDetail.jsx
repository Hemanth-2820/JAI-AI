import React, { useEffect, useState, useRef } from 'react';
import * as LucideIcons from 'lucide-react';
import styles from '../Services.module.css';



const CategoryDetail = ({ categoryName, data, onBack }) => {
  const [scrollY, setScrollY] = useState(0);

  useEffect(() => {
    window.scrollTo(0, 0);
    const handleScroll = () => setScrollY(window.scrollY);
    window.addEventListener('scroll', handleScroll, { passive: true });
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  if (!data) return null;

  const heroScale = Math.max(1, 1.15 - scrollY * 0.0002);

  return (
    <div className={styles.ssContainer}>
      {/* Navigation */}
      <div className={styles.ssNav}>
        <button onClick={onBack} className={styles.ssBackBtn}>← Back</button>
      </div>

      {/* Squarespace Hero */}
      <section className={styles.ssHero}>
        <div 
          className={styles.ssHeroBg} 
          style={{ backgroundImage: `url('${data.heroImage}')`, transform: `scale(${heroScale})` }}
        ></div>
        <div className={styles.ssHeroOverlay}></div>
        <div className={styles.ssHeroContent}>
          <h1 className={styles.ssHeroTitle}>{data.title}</h1>
          <button className={styles.ssHeroBtn}>GET STARTED</button>
          <p className={styles.ssHeroSub}>{data.subtitle}</p>
        </div>
      </section>

      {/* Features Text Area */}
      <section className={styles.ssFeatures}>
        <div className={styles.ssFeaturesContainer}>
          <h2>{data.subtitle}</h2>
          <p className={styles.ssFeaturesDesc}>{data.description}</p>
          <div className={styles.ssFeatureImageGrid}>
             {data.features.map((feat, idx) => (
                <div key={idx} className={styles.featureCardImage}>
                  <img src={feat.image} alt={feat.title} className={styles.featureImgBg} />
                  
                  <div className={styles.featureDefaultOverlay}>
                    <h3>{feat.title}</h3>
                  </div>

                  <div className={styles.featureHoverOverlay}>
                    <h3>{feat.title}</h3>
                    <p>{feat.desc}</p>
                    <button className={styles.featureReadMore}>Read More</button>
                  </div>
                </div>
             ))}
          </div>
        </div>
      </section>


      {/* Why Us Section */}
      {data.whyUs && (
        <section className={styles.ssWhyUs}>
          <div className={styles.ssWhyUsContainer}>
            <div className={styles.ssWhyUsHeader}>
              <h2>{data.whyUs.title}</h2>
              <div className={styles.ssWhyUsLine}></div>
              <p>{data.whyUs.desc}</p>
            </div>
            
            <div className={styles.ssWhyUsContent}>
              <div className={styles.ssWhyUsLeft}>
                {data.whyUs.points.map((pt, idx) => (
                  <div key={idx} className={styles.ssWhyUsItem}>
                    <div className={styles.ssWhyUsIcon}>{pt.icon}</div>
                    <div className={styles.ssWhyUsText}>
                      <h3>{pt.title}</h3>
                      <p>{pt.desc}</p>
                    </div>
                  </div>
                ))}
              </div>
              <div className={styles.ssWhyUsRight}>
                <img src={data.whyUs.image} alt="Why Us Dashboard" className={styles.ssWhyUsImg} />
              </div>
            </div>
          </div>
        </section>
      )}

      {/* Tech Stack Showcase */}
      {data.techStack && (
        <section className={styles.ssTechStack}>
          <h2>Technologies We Use</h2>
          <div className={styles.ssTechList}>
            {data.techStack.map((tech, idx) => (
              <span key={idx} className={styles.ssTechBadge}>{tech}</span>
            ))}
          </div>
        </section>
      )}

      {/* Stats Section */}
      {data.stats && (
        <section className={styles.ssStats}>
          <div className={styles.ssStatsGrid}>
            {data.stats.map((stat, idx) => (
              <div key={idx} className={styles.ssStatItem}>
                <div className={styles.ssStatValue}>{stat.value}</div>
                <div className={styles.ssStatLabel}>{stat.label}</div>
              </div>
            ))}
          </div>
        </section>
      )}

      {/* Process Timeline */}
      {data.process && (
        <section className={styles.ssProcess}>
          <div className={styles.ssProcessGrid}>
            {data.process.map((p, idx) => {
              const isEven = idx % 2 !== 0;
              const boxClass = isEven ? styles.processBoxWhite : styles.processBoxRed;
              const icon = idx === 0 ? "⊞" : idx === 1 ? "📚" : idx === 2 ? "⚙️" : "🚀";
              
              return (
                <div key={idx} className={styles.processCard}>
                  <div className={styles.processCardTop}>
                    <h3>{p.title}</h3>
                    <div className={styles.processArrow}>↗</div>
                  </div>
                  <p className={styles.processDesc}>{p.desc}</p>
                  <div className={styles.processCardBottom}>
                    <div className={styles.processStepInfo}>
                      <span className={styles.processStepLabel}>STEP</span>
                      <span className={styles.processStepNum}>{p.step}</span>
                    </div>
                    <div className={`${styles.processIconBox} ${boxClass}`}>
                      {icon}
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        </section>
      )}

      {/* Engagement Models */}
      {data.engagementModels && (
        <section className={styles.ssEngagement}>
          <h2>Engagement Models</h2>
          <div className={styles.ssEngagementGrid}>
            {data.engagementModels.map((model, idx) => (
              <div key={idx} className={styles.ssEngagementCard}>
                <h3>{model.title}</h3>
                <p>{model.desc}</p>
              </div>
            ))}
          </div>
        </section>
      )}

      {/* Service Testimonial */}
      {data.testimonial && (
        <section className={styles.ssTestimonial}>
          <div className={styles.ssTestimonialInner}>
            <p className={styles.ssTestimonialQuote}>"{data.testimonial.quote}"</p>
            <div className={styles.ssTestimonialAuthor}>
              <img src={data.testimonial.img} alt={data.testimonial.author} className={styles.ssTestimonialImg} />
              <div className={styles.ssTestimonialName}>{data.testimonial.author}</div>
            </div>
          </div>
        </section>
      )}

      {/* FAQs */}
      {data.faqs && (
        <section className={styles.ssFaqs}>
          <h2>Frequently Asked Questions</h2>
          <div className={styles.ssFaqList}>
            {data.faqs.map((faq, idx) => (
              <div key={idx} className={styles.ssFaqItem}>
                <h4>{faq.q}</h4>
                <p>{faq.a}</p>
              </div>
            ))}
          </div>
        </section>
      )}

      {/* Snake Flow Section */}
      {data.flowSection && (
        <section className={styles.ssFlowSection}>
          <div className={styles.ssFlowContainer}>
            
            <div className={styles.ssFlowLeft}>
              <div className={styles.ssSnakeGrid}>
                {data.flowSection.flowSteps.map((step, idx) => {
                  const IconComp = LucideIcons[step.icon] || LucideIcons.CheckCircle;
                  return (
                    <div key={idx} className={styles.ssSnakeItem}>
                      <div className={styles.ssSnakeIconBox}>
                        <IconComp size={36} strokeWidth={1.5} />
                      </div>
                      <span>{step.name}</span>
                    </div>
                  );
                })}
              </div>
            </div>

            <div className={styles.ssFlowRight}>
              <h3>{data.flowSection.title}</h3>
              <ul className={styles.ssFlowList}>
                {data.flowSection.points.map((pt, idx) => (
                  <li key={idx}>
                    <strong>{pt.title} - </strong>
                    {pt.desc}
                  </li>
                ))}
              </ul>
            </div>

          </div>
        </section>
      )}

      {/* Lead Magnet */}
      <section className={styles.ssLeadMagnet}>
        <div className={styles.ssLeadMagnetInner}>
          <h3>Not ready to talk yet?</h3>
          <p>Download our comprehensive 2026 {data.title} Case Studies & Pricing Brochure.</p>
          <div className={styles.ssLeadMagnetForm}>
            <input type="email" placeholder="Enter your email address" className={styles.ssLeadMagnetInput} />
            <button className={styles.ssLeadMagnetBtn}>DOWNLOAD PDF</button>
          </div>
        </div>
      </section>

      {/* Bottom CTA */}
      <section className={styles.ssBottomCta}>
        <div className={styles.ssBottomCtaInner}>
          <h2>Ready to transform your business?</h2>
          <p>Let's discuss how our {data.title} services can accelerate your growth.</p>
          <a href="/contact" style={{ textDecoration: 'none' }}>
            <button className={styles.ssBottomCtaBtn}>START YOUR PROJECT</button>
          </a>
        </div>
      </section>
    </div>
  );
};

export default CategoryDetail;
