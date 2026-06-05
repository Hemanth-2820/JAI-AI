import React from 'react';
import styles from './Contact.module.css';

const Contact = () => {
  return (
    <section className={styles.contactSection}>
      {/* Background overlay */}
      <div className={styles.contactBgOverlay}></div>

      {/* Main Content */}
      <div className={`container ${styles.contactContainer}`}>
        <form className={styles.contactForm}>
          
          <div className={styles.formGroup}>
            <label className={styles.mainLabel}>Email <span className={styles.required}>(required)</span></label>
            <input type="email" className={styles.inputField} required />
          </div>

          <div className={styles.formGroup}>
            <label className={styles.mainLabel}>Message</label>
            <textarea className={styles.textareaField} rows="4"></textarea>
          </div>

          <button type="submit" className={styles.submitBtn}>Send</button>
        </form>
      </div>
    </section>
  );
};

export default Contact;
