import React, { useState, useEffect } from 'react';
import { Link, NavLink } from 'react-router-dom';

const Navbar = () => {
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 50);
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  return (
    <header className={`navbar ${scrolled ? 'navbarScrolled' : ''}`}>
      <div className={`container navContainer`}>
        
        <div className="leftLinks">
          <NavLink to="/" className={({ isActive }) => isActive ? "navLink active" : "navLink"}>Home</NavLink>
          
          <div className="navDropdownWrapper">
            <NavLink to="/services" className={({ isActive }) => isActive ? "navLink active" : "navLink"}>
              Services <span className="dropdownArrow">▼</span>
            </NavLink>
            <div className="dropdownMenu">
              <div className="dropdownColumn">
                <h4>IT Services</h4>
                <div className="twoCol">
                  <Link to="/services/web-development" className="dropdownLink">Web Development</Link>
                  <Link to="/services/app-development" className="dropdownLink">App Development</Link>
                  <Link to="/services/software-development" className="dropdownLink">Software Development</Link>
                  <Link to="/services/aws-devops" className="dropdownLink">AWS &amp; DevOps</Link>
                  <Link to="/services/hosting-server" className="dropdownLink">Hosting &amp; Server</Link>
                  <Link to="/services/digital-marketing" className="dropdownLink">Digital Marketing</Link>
                  <Link to="/services/ai-chatbot" className="dropdownLink">AI &amp; Chatbots</Link>
                  <Link to="/services/ivr-services" className="dropdownLink">IVR Services</Link>
                  <Link to="/services/api-integration" className="dropdownLink">API Integrations</Link>
                  <Link to="/services/ecommerce-solutions" className="dropdownLink">E-Commerce</Link>
                  <Link to="/services/security-maintenance" className="dropdownLink">Security &amp; Maintenance</Link>
                  <Link to="/services/ai-automation" className="dropdownLink">AI &amp; Automation</Link>
                </div>
              </div>
              <div className="dropdownColumn">
                <h4>AI Film Services</h4>
                <Link to="/services/ai-creative-consulting" className="dropdownLink">Creative Consulting</Link>
                <Link to="/services/ai-film-production" className="dropdownLink">Film Production</Link>
                <Link to="/services/ai-commercial-production" className="dropdownLink">Commercials</Link>
                <Link to="/services/ai-vfx-post" className="dropdownLink">VFX & Post</Link>
                <Link to="/services/ai-animation-production" className="dropdownLink">Animation</Link>
              </div>
            </div>
          </div>

          <NavLink to="/originals" className={({ isActive }) => isActive ? "navLink active" : "navLink"}>Originals</NavLink>
          <NavLink to="/blog" className={({ isActive }) => isActive ? "navLink active" : "navLink"}>Blog</NavLink>
          <NavLink to="/contact" className={({ isActive }) => isActive ? "navLink active" : "navLink"}>Contact</NavLink>
        </div>

        <Link to="/" className="logoWrapper">
          <img 
            src="/images/logo_final_cropped.png" 
            alt="JAI TECH FILM CITY PVT LTD" 
            className="navLogo" 
          />
        </Link>

        <div className="rightLinks">
          <Link to="/contact" className="navButton">GET IN TOUCH</Link>
        </div>
        
      </div>
    </header>
  );
};

export default Navbar;
