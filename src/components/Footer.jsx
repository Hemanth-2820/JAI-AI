import React from 'react';
import { Link } from 'react-router-dom';

const Footer = () => {
  return (
    <footer className="footer">
      <div className="footerContent">
        
        <div className="footerLogoCol">
          <img 
            src="/images/logo_final_cropped.png" 
            alt="JAI TECH FILM CITY PVT LTD" 
            className="footerLogo" 
          />
         
        </div>
        
        <div className="footerLinkCol">
          <Link to="/general-terms-conditions" className="footerLink">Terms & Conditions</Link>
        </div>
        
        <div className="footerInfoCol">
          <p>
            <strong>Anima Studios srl</strong><br />
            Foro Buonaparte 59, 20121 Milano, Italy<br />
            <a href="mailto:info@animastudios.ai" className="footerEmail">info@animastudios.ai</a><br />
            VAT Number: IT 14270340962
          </p>
        </div>
        
        <div className="footerLinkCol">
          <Link to="/gdpr-policy" className="footerLink">GDPR Policy</Link>
        </div>
        
        <div className="footerSocialCol">
          <a href="https://instagram.com/animastudios.ai" target="_blank" rel="noopener noreferrer" className="footerSocialIcon" aria-label="Instagram">
            <i className="fa-brands fa-instagram"></i>
          </a>
          <a href="http://x.com/animastudiosai" target="_blank" rel="noopener noreferrer" className="footerSocialIcon" aria-label="X (formerly Twitter)">
            <i className="fa-brands fa-x-twitter"></i>
          </a>
          <a href="https://www.tiktok.com/@anima.journeys" target="_blank" rel="noopener noreferrer" className="footerSocialIcon" aria-label="TikTok">
            <i className="fa-brands fa-tiktok"></i>
          </a>
          <a href="https://www.youtube.com/@AnimaStudiosTV" target="_blank" rel="noopener noreferrer" className="footerSocialIcon" aria-label="YouTube">
            <i className="fa-brands fa-youtube"></i>
          </a>
        </div>

      </div>
    </footer>
  );
};

export default Footer;
