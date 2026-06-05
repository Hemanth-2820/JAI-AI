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
          <NavLink to="/services" className={({ isActive }) => isActive ? "navLink active" : "navLink"}>Services</NavLink>
          <NavLink to="/originals" className={({ isActive }) => isActive ? "navLink active" : "navLink"}>Originals</NavLink>
          <NavLink to="/blog" className={({ isActive }) => isActive ? "navLink active" : "navLink"}>Blog</NavLink>
          <NavLink to="/contact" className={({ isActive }) => isActive ? "navLink active" : "navLink"}>Contact</NavLink>
        </div>

        <Link to="/" className="logoWrapper">
          <img 
            src="https://images.squarespace-cdn.com/content/v1/6701097f9e93b178e9a6a834/636e9411-2bf8-4818-afc5-7b4d6befbf8d/Bianco_trasparente.png?format=1500w" 
            alt="Anima Studios" 
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
