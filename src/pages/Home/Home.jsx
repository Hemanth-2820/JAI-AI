import React from 'react';
import Hero from './Hero';
import Portfolio from './Portfolio';
import Services from './Services';
import Contact from './Contact';

const Home = () => {
  return (
    <main>
      <Hero />
      <Portfolio />
      <Services />
      <Contact />
    </main>
  );
};

export default Home;
