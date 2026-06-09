import React, { useState } from 'react';
import styles from '../Services.module.css';

const FaqSection = ({ faqs }) => {
  const [openFaqIndex, setOpenFaqIndex] = useState(null);

  const toggleFaq = (index) => {
    setOpenFaqIndex(openFaqIndex === index ? null : index);
  };

  return (
    <section className={styles.faqSection}>
      <div className={styles.faqContainer}>
        <h2 className={`${styles.h2Scale} ${styles.faqSectionTitle}`}>Frequently asked questions</h2>
        <div className={styles.faqList}>
          {faqs.map((faq, idx) => (
            <div key={idx} className={`${styles.faqItem} ${openFaqIndex === idx ? styles.faqOpen : ''}`}>
              <button 
                className={styles.faqQuestion} 
                onClick={() => toggleFaq(idx)}
                aria-expanded={openFaqIndex === idx}
              >
                <span>{faq.q}</span>
                <span className={styles.faqIcon}>{openFaqIndex === idx ? '−' : '+'}</span>
              </button>
              <div className={styles.faqAnswer} style={{ maxHeight: openFaqIndex === idx ? '800px' : '0' }}>
                <div className={styles.faqAnswerContent}>
                  <p>{faq.a}</p>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default FaqSection;
