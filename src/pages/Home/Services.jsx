import React from 'react';
import styles from './Home.module.css';

const servicesList = [
  {
    title: "Next-Gen Advertising",
    description: "High-end 15” and 30” TV spots and Hero videos. We visualize impossible concepts for global campaigns at a fraction of traditional production constraints.",
    watermark: "fa-solid fa-clapperboard",
    icon: "fas fa-film"
  },
  {
    title: "Branded Storytelling",
    description: "Deep narrative experiences. We produce fashion films, brand documentaries, and narrative shorts that connect with audiences on an emotional level.",
    watermark: "fa-solid fa-bullhorn",
    icon: "fas fa-feather-pointed"
  },
  {
    title: "Premium Social Assets",
    description: "Stop the scroll with high-frequency cinematic assets. We create high-conversion viral video content tailored for TikTok, Reels, and digital-first campaigns.",
    watermark: "fa-solid fa-hashtag",
    icon: "fas fa-mobile-screen"
  },
  {
    title: "Entertainment IP",
    description: "From original concepting to existing IP expansion. We develop Children’s Series, Vertical Micro-dramas, and franchise extensions for global broadcasters.",
    watermark: "fa-solid fa-tv",
    icon: "fas fa-chess-knight"
  },
  {
    title: "Movie Integration & VFX",
    description: "Elevating short movie production through digital wizardry. We provide full Post-Production, AI-VFX, and seamless CGI integration for cinematic storytelling.",
    watermark: "fa-solid fa-wand-magic-sparkles",
    icon: "fas fa-hat-wizard"
  },
  {
    title: "Trailers & Teasers",
    description: "Explosive Movie Trailers and hype reels. We create atmospheric previews for films, games, and series that demand immediate attention and drive engagement.",
    watermark: "fa-solid fa-fire-flame-curved",
    icon: "fas fa-video"
  }
];

const Services = () => {
  return (
    <section id="services" className={styles.animaPremiumServices}>
      <div className={styles.servicesMainBg}></div>
      <div className={styles.servicesGradientOverlay}></div>

      <div className={styles.servicesContainer}>
        <header className={styles.servicesIntro}>
          <h2 className={styles.servicesLabel}>The Future of Video Production</h2>
          <h3 className={styles.servicesHeadline}>AI-POWERED CINEMATIC SOLUTIONS</h3>
          <p className={styles.servicesLead}>
            Blending human direction with generative acceleration to deliver high-end content for visionary brands and broadcasters.
          </p>
        </header>

        <div className={styles.servicesBentoGrid}>
          {servicesList.map((service, index) => (
            <div key={index} className={styles.sCard}>
              <i className={`${service.watermark} ${styles.sWatermark}`}></i>
              <div className={styles.sIcon}>
                <i className={service.icon}></i>
              </div>
              <h4 className={styles.sTitle}>{service.title}</h4>
              <p className={styles.sText}>{service.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Services;
