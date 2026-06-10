import React from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import styles from './Services.module.css';

// Import Components
import HeroSection from './components/HeroSection';
import IntroSection from './components/IntroSection';
import HowYouWorkSection from './components/HowYouWorkSection';
import FeatureSections from './components/FeatureSections';
import TestimonialsSection from './components/TestimonialsSection';
import FaqSection from './components/FaqSection';
import SupportSection from './components/SupportSection';
import ConversionSection from './components/ConversionSection';

import CategoryDetail from './components/CategoryDetail';
import { categoryData } from './categoryData';

import imgPreProduction from './assets/pre_production.png';
import imgProduction from './assets/production.png';
import imgPostProduction from './assets/post_production.png';
import imgServiceAd from './assets/service_ad.png';
import imgServiceCharacter from './assets/service_character.png';
import imgServiceConcept from './assets/service_concept.png';
import imgServiceMusicvideo from './assets/service_musicvideo.png';
import imgServiceShortfilm from './assets/service_shortfilm.png';
import imgServiceStoryboard from './assets/service_storyboard.png';
import imgServiceTrailer from './assets/service_trailer.png';

const Services = () => {
  const { categoryId } = useParams();
  const navigate = useNavigate();

  const heroImages = [];

  const introFeatures = [
    {
      title: "AI Creative Consulting",
      desc: "Align your brand's vision with cutting-edge AI film strategy. We provide comprehensive creative direction and campaign planning.",
      link: "Explore creative consulting→",
      img: imgServiceConcept
    },
    {
      title: "AI Script Development",
      desc: "Bring your core idea to life. From story expansion to full screenplay writing, we craft dialogue and characters that resonate.",
      link: "Explore script development→",
      img: imgPreProduction
    },
    {
      title: "AI Storyboarding",
      desc: "Visualize the entire film before rendering a single frame. Rapidly generate storyboards and establish the visual direction.",
      link: "Explore storyboarding→",
      img: imgServiceStoryboard
    }
  ];

  const workTypes = [
    { id: "ai-film-production", title: "AI Film Production", img: imgProduction },
    { id: "ai-cinematic-video", title: "AI Cinematic Video", img: imgServiceTrailer },
    { id: "ai-commercial-production", title: "AI Commercial Production", img: imgServiceAd },
    { id: "ai-animation-production", title: "AI Animation Production", img: imgServiceMusicvideo },
    { id: "ai-social-media", title: "AI Social Media", img: imgServiceShortfilm }
  ];

  const featureData = [
    {
      id: "world-building",
      title: "AI Character & World Building",
      features: [
        { heading: "Character Design", desc: "Hero, Villain, Sci-Fi, and Mascot character creation with high detail." },
        { heading: "Environment Concepts", desc: "Design futuristic cities, fantasy worlds, and massive exterior spaces." },
        { heading: "Visual Consistency", desc: "Ensure your cinematic universe maintains consistent art direction." }
      ],
      link: "Explore world building→",
      images: [
        imgServiceCharacter,
        imgServiceConcept,
        imgServiceStoryboard
      ]
    },
    {
      id: "digital-humans",
      title: "AI Digital Humans & Avatars",
      features: [
        { heading: "Ultra-Realistic Presenters", desc: "Deploy digital influencers and hosts for your brand campaigns." },
        { heading: "Brand Ambassadors", desc: "Create a unique virtual face for your brand that never sleeps." }
      ],
      link: "Explore digital avatars→",
      images: [
        imgServiceCharacter,
        imgServiceMusicvideo,
        imgPostProduction
      ]
    },
    {
      id: "vfx-post",
      title: "AI Editing & VFX",
      features: [
        { heading: "Advanced Visual Effects", desc: "Explosions, sci-fi effects, and incredible CGI enhancements." },
        { heading: "Final Mastering", desc: "Color grading, sound mixing, and theatrical mastering." }
      ],
      link: "Explore VFX & Editing→",
      images: [
        imgPostProduction
      ]
    }
  ];

  const testimonials = [
    {
      quote: "ANIMA STUDIOS transformed our raw script into a breathtaking 4K cinematic commercial in under two weeks. The AI visuals were indistinguishable from a million-dollar Hollywood shoot.",
      author: "Nexus Robotics CEO, David Chen",
      img: imgServiceConcept
    },
    {
      quote: "The digital human they created for our brand became our top-performing influencer. The voice generation and lip-syncing are completely flawless.",
      author: "Aura Cosmetics CMO, Sarah Jenkins",
      img: imgServiceCharacter
    },
    {
      quote: "From storyboarding to final VFX, their AI pipeline saved us millions in production costs while delivering a sci-fi world that blew our audience away.",
      author: "Starlight Pictures Director, Marcus Vance",
      img: imgServiceStoryboard
    }
  ];

  const faqs = [
    { q: "What is AI Film Production?", a: "AI Film Production utilizes advanced artificial intelligence tools to generate, enhance, and streamline the filmmaking process. From text-to-video generation to AI voice synthesis, we create high-end cinematic content at a fraction of traditional costs." },
    { q: "Do I need a script to get started?", a: "No! We offer full AI Script Development services. You can come to us with just a one-line idea, and our team will craft a complete narrative, storyboard, and production plan." },
    { q: "Are the digital avatars realistic?", a: "Extremely. We use state-of-the-art neural rendering to create digital humans and avatars that feature photorealistic skin textures, accurate micro-expressions, and perfectly synced lip movements." },
    { q: "Can you provide voiceovers in multiple languages?", a: "Yes. Our AI Voice Generation & Dubbing service supports multiple languages including English, Telugu, Hindi, Tamil, Kannada, Malayalam, Arabic, and Japanese, all with native emotional inflection." },
    { q: "How long does a typical AI Commercial take to produce?", a: "While traditional commercials can take months, our AI pipeline allows us to deliver high-quality 15, 30, and 60-second commercials in a matter of weeks, or even days depending on the complexity." },
    { q: "Who owns the rights to the AI generated films?", a: "As a client, you retain full commercial rights to the final delivered films and assets produced by ANIMA STUDIOS during our engagement." }
  ];

  if (categoryId && categoryData[categoryId]) {
    console.log("Rendering category detail for:", categoryId);
    return (
      <CategoryDetail 
        categoryName={categoryId} 
        data={categoryData[categoryId]} 
        onBack={() => navigate('/services')} 
      />
    );
  }

  return (
    <div className={styles.pageContainer}>
      <HeroSection heroImages={heroImages} />
      <IntroSection introFeatures={introFeatures} onSelectDetail={(id) => navigate(`/services/${id}`)} />
      <HowYouWorkSection workTypes={workTypes} onSelectCategory={(id) => navigate(`/services/${id}`)} />
      <FeatureSections featureData={featureData} onSelectDetail={(id) => navigate(`/services/${id}`)} />
      <TestimonialsSection testimonials={testimonials} />
      <FaqSection faqs={faqs} />
      <SupportSection />
      <ConversionSection onSelectDetail={(id) => navigate(`/services/${id}`)} />
    </div>
  );
};

export default Services;
