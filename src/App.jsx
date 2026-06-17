import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Footer from './components/Footer';

// Pages
import Home from './pages/Home/Home';
import ServicesPage from './pages/Services/Services';
import AboutUs from './pages/AboutUs/AboutUs';
import BlogPage from './pages/Blog/Blog';
import ContactPage from './pages/Contact/Contact';
import ScrollToTop from './components/ScrollToTop';

import './index.css';
import './App.css'; // Contains Navbar and Footer styles
// Force Vite HMR

function App() {
  return (
    <Router>
      <ScrollToTop />
      <div className="app">
        <Navbar />
        
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/services" element={<ServicesPage />} />
          <Route path="/services/:categoryId" element={<ServicesPage />} />
          <Route path="/about-us" element={<AboutUs />} />
          <Route path="/blog" element={<BlogPage />} />
          <Route path="/contact" element={<ContactPage />} />
        </Routes>

        <Footer />
      </div>
    </Router>
  );
}

export default App;
