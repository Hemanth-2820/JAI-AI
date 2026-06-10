import React, { useState, useRef, useEffect } from 'react';
import styles from './Home.module.css';

// Import local videos from assets
import video1 from '../../assets/video.1.mp4';
import video2 from '../../assets/video.2.mp4';
import video3 from '../../assets/video.3.mp4';

const videos = [video1, video2, video3];

const Hero = () => {
  const [currentVideoIndex, setCurrentVideoIndex] = useState(0);
  const videoRef = useRef(null);

  const handleVideoEnded = () => {
    // When a video ends, move to the next one in the array, looping back to 0
    setCurrentVideoIndex((prevIndex) => (prevIndex + 1) % videos.length);
  };

  useEffect(() => {
    // Whenever the index changes, load and play the new video
    if (videoRef.current) {
      // Force muted for mobile browsers to allow autoplay
      videoRef.current.defaultMuted = true;
      videoRef.current.muted = true;
      videoRef.current.load();
      const playPromise = videoRef.current.play();
      if (playPromise !== undefined) {
        playPromise.catch(error => {
          console.log("Autoplay was prevented by the browser, falling back to poster:", error);
        });
      }
    }
  }, [currentVideoIndex]);

  return (
    <section className={styles.hero}>
      {/* Background Videos */}
      <div className={styles.heroVideoWrapper}>
        <video 
          ref={videoRef}
          autoPlay 
          muted 
          playsInline 
          onEnded={handleVideoEnded}
          className={styles.backgroundVideo}
          poster="https://i.postimg.cc/Njxvn3YR/HOMEPAGE-1.png"
        >
          <source src={videos[currentVideoIndex]} type="video/mp4" />
        </video>
        {/* Overlay to darken video slightly */}
        <div className={styles.heroBgOverlay}></div>
      </div>

      {/* Content */}
      <div className={`container ${styles.heroContent}`}>
        <h1 className={`${styles.heroTitle} animate-in`}>
          AI-POWERED CREATIVE STUDIO<br />
          FOR BRANDS, AGENCIES &<br />
          STORYTELLERS
        </h1>
      </div>
    </section>
  );
};

export default Hero;
