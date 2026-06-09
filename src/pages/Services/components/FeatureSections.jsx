import React from 'react';
import styles from '../Services.module.css';

const FeatureSections = ({ featureData, onSelectDetail }) => {
  return (
    <div className={styles.featuresBentoWrapper}>
      {featureData.map((section, idx) => {
        if (section.images.length === 3) {
          return <ThreeImageFeatureSection key={section.id} section={section} onSelectDetail={onSelectDetail} />;
        }
        if (section.images.length === 1) {
          return <SingleImageFeatureSection key={section.id} section={section} onSelectDetail={onSelectDetail} />;
        }
        return <BentoFeatureSection key={section.id} section={section} idx={idx} onSelectDetail={onSelectDetail} />;
      })}
    </div>
  );
};

const ThreeImageFeatureSection = ({ section, onSelectDetail }) => {
  const handleLinkClick = (e, linkText) => {
    e.preventDefault();
    const linkMap = {
      "Explore world building→": "world-building",
      "Explore digital avatars→": "digital-humans",
      "Explore VFX & Editing→": "vfx-post"
    };
    if (onSelectDetail && linkMap[linkText]) {
      onSelectDetail(linkMap[linkText]);
    }
  };

  return (
    <section className={styles.bentoSection}>
      <div className={styles.bentoHeader}>
        <h2 className={styles.bentoTitle}>{section.title}</h2>
        {section.link && (
          <a href="#" className={styles.bentoLinkBtn} onClick={(e) => handleLinkClick(e, section.link)}>
            <span>{section.link.toUpperCase()}</span>
            <span className={styles.bentoLinkArrow}>→</span>
          </a>
        )}
      </div>

      <div className={styles.bentoGridThreeAsymmetric}>
        {/* Left Giant Card (Spans full height) */}
        <div className={`${styles.bentoCardImageBg} ${styles.bentoCardGiant}`}>
          {section.images[0] && <img src={section.images[0]} alt="" className={styles.bentoCardBgImg} loading="lazy" />}
          <div className={`${styles.bentoCardOverlay} ${styles.overlayBottom}`}></div>
          <div className={`${styles.bentoCardContent} ${styles.contentBottom} ${styles.textOverImage}`}>
            <h3>{section.features[0]?.heading}</h3>
            <p>{section.features[0]?.desc}</p>
          </div>
        </div>

        {/* Top Right Small Card */}
        <div className={`${styles.bentoCardImageBg} ${styles.bentoCardSmallTop}`}>
          {section.images[1] && <img src={section.images[1]} alt="" className={styles.bentoCardBgImg} loading="lazy" />}
          <div className={`${styles.bentoCardOverlay} ${styles.overlayTop}`}></div>
          <div className={`${styles.bentoCardContent} ${styles.contentTop} ${styles.textOverImage}`}>
            <h3>{section.features[1]?.heading}</h3>
            <p>{section.features[1]?.desc}</p>
          </div>
        </div>

        {/* Bottom Right Small Card */}
        <div className={`${styles.bentoCardSolid} ${styles.bentoCardSmallBottom}`} style={{ backgroundColor: '#212023' }}>
          <div className={`${styles.bentoCardContent} ${styles.contentTop}`}>
            <h3>{section.features[2]?.heading}</h3>
            <p>{section.features[2]?.desc}</p>
          </div>
          <div className={`${styles.bentoCardImgWrapper} ${styles.imgBottomRight}`}>
            {section.images[2] && <img src={section.images[2]} alt="" loading="lazy" />}
          </div>
        </div>
      </div>
    </section>
  );
};

const SingleImageFeatureSection = ({ section, onSelectDetail }) => {
  const handleLinkClick = (e, linkText) => {
    e.preventDefault();
    const linkMap = {
      "Explore world building→": "world-building",
      "Explore digital avatars→": "digital-humans",
      "Explore VFX & Editing→": "vfx-post"
    };
    if (onSelectDetail && linkMap[linkText]) {
      onSelectDetail(linkMap[linkText]);
    }
  };

  return (
    <section className={styles.singleImageSection}>
      <div className={styles.bentoHeader}>
        {section.title && <h2 className={styles.singleImageTitle} style={{ margin: 0 }}>{section.title}</h2>}
        {section.link && (
          <a href="#" className={styles.bentoLinkBtn} onClick={(e) => handleLinkClick(e, section.link)}>
            <span>{section.link.toUpperCase()}</span>
            <span className={styles.bentoLinkArrow}>→</span>
          </a>
        )}
      </div>
      
      <div className={styles.singleImageWrapper}>
        <img src={section.images[0]} alt={section.title} loading="lazy" />
      </div>

      <div className={styles.singleImageFeaturesGrid}>
        {section.features.map((feat, i) => (
          <div key={i} className={styles.singleImageFeatureItem}>
            <h3>{feat.heading}</h3>
            <p>{feat.desc}</p>
          </div>
        ))}
      </div>
    </section>
  );
};

const BentoFeatureSection = ({ section, idx, onSelectDetail }) => {
  // Use alternate background colors for variety
  const solidBgColors = ['#1f211f', '#212023', '#23211f'];
  const solidBg = solidBgColors[idx % solidBgColors.length];

  const layoutType = idx % 3;

  const handleLinkClick = (e, linkText) => {
    e.preventDefault();
    const linkMap = {
      "Explore world building→": "world-building",
      "Explore digital avatars→": "digital-humans",
      "Explore VFX & Editing→": "vfx-post"
    };
    if (onSelectDetail && linkMap[linkText]) {
      onSelectDetail(linkMap[linkText]);
    }
  };

  return (
    <section className={styles.bentoSection}>
      <div className={styles.bentoHeader}>
        <h2 className={styles.bentoTitle}>{section.title}</h2>
        {section.link && (
          <a href="#" className={styles.bentoLinkBtn} onClick={(e) => handleLinkClick(e, section.link)}>
            <span>{section.link.toUpperCase()}</span>
            <span className={styles.bentoLinkArrow}>→</span>
          </a>
        )}
      </div>

      <div className={styles.bentoGrid}>
        {layoutType === 0 && (
          <>
            <div className={styles.bentoCardSolid} style={{ backgroundColor: solidBg }}>
              <div className={`${styles.bentoCardContent} ${styles.contentTop}`}>
                <h3>{section.features[0]?.heading}</h3>
                <p>{section.features[0]?.desc}</p>
              </div>
              <div className={`${styles.bentoCardImgWrapper} ${styles.imgBottom}`}>
                {section.images[0] && <img src={section.images[0]} alt="" loading="lazy" />}
              </div>
            </div>
            <div className={styles.bentoCardImageBg}>
              {section.images[1] && <img src={section.images[1]} alt="" className={styles.bentoCardBgImg} loading="lazy" />}
              <div className={`${styles.bentoCardOverlay} ${styles.overlayTop}`}></div>
              <div className={`${styles.bentoCardContent} ${styles.contentTop} ${styles.textOverImage}`}>
                <h3>{section.features[1]?.heading}</h3>
                <p>{section.features[1]?.desc}</p>
              </div>
            </div>
          </>
        )}

        {layoutType === 1 && (
          <>
            <div className={styles.bentoCardImageBg}>
              {section.images[0] && <img src={section.images[0]} alt="" className={styles.bentoCardBgImg} loading="lazy" />}
              <div className={`${styles.bentoCardOverlay} ${styles.overlayBottom}`}></div>
              <div className={`${styles.bentoCardContent} ${styles.contentBottom} ${styles.textOverImage}`}>
                <h3>{section.features[0]?.heading}</h3>
                <p>{section.features[0]?.desc}</p>
              </div>
            </div>
            <div className={styles.bentoCardSolid} style={{ backgroundColor: solidBg }}>
              <div className={`${styles.bentoCardImgWrapper} ${styles.imgTop}`}>
                {section.images[1] && <img src={section.images[1]} alt="" loading="lazy" />}
              </div>
              <div className={`${styles.bentoCardContent} ${styles.contentBottom}`}>
                <h3>{section.features[1]?.heading}</h3>
                <p>{section.features[1]?.desc}</p>
              </div>
            </div>
          </>
        )}

        {layoutType === 2 && (
          <>
            <div className={styles.bentoCardSolid} style={{ backgroundColor: solidBg }}>
              <div className={`${styles.bentoCardContent} ${styles.contentTop}`}>
                <h3>{section.features[0]?.heading}</h3>
                <p>{section.features[0]?.desc}</p>
              </div>
              <div className={`${styles.bentoCardImgWrapper} ${styles.imgBottomRight}`}>
                {section.images[0] && <img src={section.images[0]} alt="" loading="lazy" />}
              </div>
            </div>
            <div className={styles.bentoCardImageBg}>
              {section.images[1] && <img src={section.images[1]} alt="" className={styles.bentoCardBgImg} loading="lazy" />}
              <div className={`${styles.bentoCardOverlay} ${styles.overlayCenter}`}></div>
              <div className={`${styles.bentoCardContent} ${styles.contentCenter} ${styles.textOverImage}`}>
                <h3>{section.features[1]?.heading}</h3>
                <p>{section.features[1]?.desc}</p>
              </div>
            </div>
          </>
        )}
      </div>
    </section>
  );
};

export default FeatureSections;
