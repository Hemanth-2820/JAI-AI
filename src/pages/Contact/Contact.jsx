import React from 'react';
import { motion } from 'framer-motion';
import { Mail, MapPin, Phone, ArrowRight } from 'lucide-react';
import styles from './Contact.module.css';

const Contact = () => {
  return (
    <section className={styles.contactSection}>
      {/* Background ambient glows */}
      <div className={styles.glowBlob1}></div>
      <div className={styles.glowBlob2}></div>

      <div className={`container ${styles.contactContainer}`}>
        
        {/* Left Side: Contact Information */}
        <motion.div 
          className={styles.contactInfo}
          initial={{ opacity: 0, x: -50 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.8, ease: "easeOut" }}
        >
          <h1 className={styles.title}>
            Let's talk about<br />
            <span className={styles.gradientText}>your project.</span>
          </h1>
          <p className={styles.subtitle}>
            We're here to help and answer any question you might have. We look forward to hearing from you.
          </p>

          <div className={styles.infoList}>
            <div className={styles.infoItem}>
              <div className={styles.iconBox}>
                <Mail className={styles.icon} />
              </div>
              <div>
                <h4 className={styles.infoLabel}>Email Us</h4>
                <a href="mailto:hello@jaiai.com" className={styles.infoText}>hello@jaiai.com</a>
              </div>
            </div>
            
            <div className={styles.infoItem}>
              <div className={styles.iconBox}>
                <Phone className={styles.icon} />
              </div>
              <div>
                <h4 className={styles.infoLabel}>Call Us</h4>
                <a href="tel:+15551234567" className={styles.infoText}>+1 (555) 123-4567</a>
              </div>
            </div>

            <div className={styles.infoItem}>
              <div className={styles.iconBox}>
                <MapPin className={styles.icon} />
              </div>
              <div>
                <h4 className={styles.infoLabel}>Visit Us</h4>
                <span className={styles.infoText}>123 Innovation Drive, Tech City, TC 90210</span>
              </div>
            </div>
          </div>
        </motion.div>

        {/* Right Side: Contact Form */}
        <motion.div 
          className={styles.formWrapper}
          initial={{ opacity: 0, x: 50 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.8, ease: "easeOut", delay: 0.2 }}
        >
          <form className={styles.contactForm}>
            <div className={styles.formGrid}>
              <div className={styles.formGroup}>
                <label className={styles.label}>First Name</label>
                <input type="text" className={styles.input} placeholder="John" required />
              </div>
              <div className={styles.formGroup}>
                <label className={styles.label}>Last Name</label>
                <input type="text" className={styles.input} placeholder="Doe" required />
              </div>
            </div>

            <div className={styles.formGroup}>
              <label className={styles.label}>Email Address</label>
              <input type="email" className={styles.input} placeholder="john@example.com" required />
            </div>

            <div className={styles.formGroup}>
              <label className={styles.label}>Message</label>
              <textarea className={styles.textarea} rows="5" placeholder="Tell us about your project..."></textarea>
            </div>

            <button type="submit" className={styles.submitBtn}>
              <span>Send Message</span>
              <ArrowRight size={20} className={styles.btnIcon} />
            </button>
          </form>
        </motion.div>

      </div>
    </section>
  );
};

export default Contact;
