import heroImg from './assets/hero.png';
import preProdImg from './assets/pre_production.png';
import prodImg from './assets/production.png';
import postProdImg from './assets/post_production.png';
import adImg from './assets/service_ad.png';
import characterImg from './assets/service_character.png';
import conceptImg from './assets/service_concept.png';
import musicImg from './assets/service_musicvideo.png';
import shortfilmImg from './assets/service_shortfilm.png';
import storyboardImg from './assets/service_storyboard.png';
import trailerImg from './assets/service_trailer.png';

export const categoryData = {
  "ai-creative-consulting": {
    title: "AI Creative Consulting",
    subtitle: "Strategy service for your brand.",
    description: "Align your brand's vision with cutting-edge AI film strategy. We provide comprehensive creative direction, campaign planning, and visual identity mapping to ensure maximum impact.",
    heroImage: conceptImg,
    features: [
      { title: "Film Strategy", desc: "Develop a cohesive AI film strategy tailored to your target audience.", icon: "🎯" },
      { title: "Brand Storytelling", desc: "Craft compelling narratives that elevate your brand's core messaging.", icon: "📖" },
      { title: "Creative Direction", desc: "Complete visual identity planning and overarching campaign strategy.", icon: "🎨" }
    ],
    masonryImages: [ adImg, storyboardImg, prodImg ]
  },
  "ai-script-development": {
    title: "AI Script Development",
    subtitle: "Client idea ni complete screenplay ga convert cheyyadam.",
    description: "Bring your core idea to life with AI-assisted narrative structuring. From story expansion to full screenplay writing, we craft dialogue and characters that resonate.",
    heroImage: preProdImg,
    features: [
      { title: "Story Development", desc: "Story expansion, narrative structuring, and scene breakdown.", icon: "✍️" },
      { title: "Screenplay Writing", desc: "Full script writing with professional dialogue and character creation.", icon: "📜" },
      { title: "Deliverables", desc: "Concept Note, Synopsis, Treatment, and Full Script ready for production.", icon: "📑" }
    ],
    masonryImages: [ storyboardImg, conceptImg, shortfilmImg ]
  },
  "ai-storyboarding": {
    title: "AI Storyboarding & Previsualization",
    subtitle: "Film shoot mundu complete visualization.",
    description: "Visualize the entire film before rendering a single frame. We use AI to rapidly generate storyboards, plan camera angles, and establish the visual direction.",
    heroImage: storyboardImg,
    features: [
      { title: "Shot Planning", desc: "Meticulous camera planning and scene visualization.", icon: "🎥" },
      { title: "Mood Development", desc: "Establish sequence planning and overall visual direction.", icon: "🖼️" },
      { title: "Deliverables", desc: "Comprehensive storyboards, shot lists, and a full production blueprint.", icon: "📐" }
    ],
    masonryImages: [ trailerImg, preProdImg, prodImg ]
  },

  "ai-film-production": {
    title: "AI Film Production",
    subtitle: "Idea nunchi final film export varaku complete production.",
    description: "Our core service. We manage the entire pipeline from the spark of an idea to the final export, delivering high-end AI films for any medium.",
    heroImage: prodImg,
    features: [
      { title: "Diverse Formats", desc: "Short Films, Brand Films, Documentaries, and Corporate Films.", icon: "🎬" },
      { title: "End-to-End Pipeline", desc: "Script, Visual Development, AI Production, and Editing.", icon: "⚙️" },
      { title: "Final Delivery", desc: "Exporting in high-fidelity formats ready for distribution.", icon: "📤" }
    ],
    masonryImages: [ heroImg, shortfilmImg, trailerImg ]
  },
  "ai-cinematic-video": {
    title: "AI Cinematic Video Generation",
    subtitle: "Actual scenes create cheyyadam.",
    description: "Cutting-edge scene generation using the latest Text-to-Video and Image-to-Video models. We create emotional, action-packed cinematic sequences.",
    heroImage: trailerImg,
    features: [
      { title: "Generative Video", desc: "Text-to-Video and Image-to-Video scene generation.", icon: "🧠" },
      { title: "Cinematic Sequences", desc: "Action sequences, emotional sequences, and brand story films.", icon: "🎞️" },
      { title: "Deliverables", desc: "Stunning HD and 4K resolution cinematic sequences.", icon: "📺" }
    ],
    masonryImages: [ prodImg, postProdImg, shortfilmImg ]
  },
  "ai-commercial-production": {
    title: "AI Commercial Production",
    subtitle: "Business advertisements.",
    description: "High-conversion commercials created at a fraction of traditional production costs. Perfect for startups, corporate campaigns, and performance marketing.",
    heroImage: adImg,
    features: [
      { title: "Ad Campaigns", desc: "Product commercials, service ads, and corporate campaigns.", icon: "📈" },
      { title: "Performance Marketing", desc: "Highly optimized creatives designed for social media platforms.", icon: "🎯" },
      { title: "Deliverables", desc: "15 Sec, 30 Sec, and 60 Sec Ad campaign videos.", icon: "⏱️" }
    ],
    masonryImages: [ characterImg, conceptImg, heroImg ]
  },
  "ai-animation-production": {
    title: "AI Animation Production",
    subtitle: "Animation-based films.",
    description: "Push the boundaries of 2D and 3D animation. We blend AI rendering with traditional motion graphics to produce captivating explainer animations and character films.",
    heroImage: musicImg,
    features: [
      { title: "Animation Styles", desc: "2D Animation, 3D Animation, and Motion Graphics.", icon: "🖌️" },
      { title: "Character Animation", desc: "Expressive character rigging and explainer animations.", icon: "🕺" },
      { title: "Deliverables", desc: "Animated Films, Animated Ads, and Explainer Videos.", icon: "🎬" }
    ],
    masonryImages: [ storyboardImg, characterImg, conceptImg ]
  },
  "ai-social-media": {
    title: "AI Social Media Content Studio",
    subtitle: "Short-form content creation.",
    description: "Dominate the feed with highly engaging, rapid-production short-form content tailored for Instagram, YouTube Shorts, TikTok, and LinkedIn.",
    heroImage: shortfilmImg,
    features: [
      { title: "Short-Form Video", desc: "Instagram Reels, YouTube Shorts, and TikTok videos.", icon: "📱" },
      { title: "B2B Content", desc: "Professional LinkedIn content and marketing creatives.", icon: "💼" },
      { title: "Deliverables", desc: "Monthly Content Packs and structured campaign assets.", icon: "📦" }
    ],
    masonryImages: [ adImg, trailerImg, preProdImg ]
  },

  "ai-world-building": {
    title: "AI Character & World Building",
    subtitle: "Movie world and Characters create cheyyadam.",
    description: "Design heroes, villains, and entire cinematic universes. From futuristic sci-fi worlds to historical villages, we generate assets for production.",
    heroImage: characterImg,
    features: [
      { title: "Character Design", desc: "Hero, Villain, Sci-Fi, and Mascot character creation.", icon: "👤" },
      { title: "Environment Concepts", desc: "Futuristic cities, fantasy worlds, and interior/exterior spaces.", icon: "🏙️" },
      { title: "Deliverables", desc: "Expression sheets, costume variations, and scene assets.", icon: "🗺️" }
    ],
    masonryImages: [ conceptImg, adImg, trailerImg ]
  },
  "ai-digital-humans": {
    title: "AI Digital Humans & Avatars",
    subtitle: "Growing category.",
    description: "Deploy ultra-realistic digital influencers, AI presenters, and virtual characters for your brand campaigns and training videos.",
    heroImage: heroImg,
    features: [
      { title: "Digital Avatars", desc: "AI Presenters, Hosts, and Digital Influencers.", icon: "🤖" },
      { title: "Brand Integration", desc: "Virtual characters acting as AI Brand Ambassadors.", icon: "🌟" },
      { title: "Deliverables", desc: "Talking avatars, presenter videos, and training videos.", icon: "🗣️" }
    ],
    masonryImages: [ characterImg, prodImg, adImg ]
  },
  "ai-vfx-post": {
    title: "AI Editing & VFX",
    subtitle: "Most important service & Advanced visual effects.",
    description: "The magic happens in post. We provide final mastering, color grading, CGI enhancements, and explosive visual effects to make your film theater-ready.",
    heroImage: postProdImg,
    features: [
      { title: "Visual Effects", desc: "Explosions, Weather Effects, Environment Extensions, Object Removal.", icon: "💥" },
      { title: "Post Production", desc: "Video Editing, Color Grading, Sound Mixing, Final Mastering.", icon: "🖥️" },
      { title: "Deliverables", desc: "Composited Scenes, TV Versions, Cinema Versions, and OTT Versions.", icon: "🍿" }
    ],
    masonryImages: [ musicImg, trailerImg, prodImg ]
  },
  "ai-audio-voice": {
    title: "AI Voice Generation & Music",
    subtitle: "Voice and Audio production.",
    description: "Immersive soundscapes. We generate custom background scores, sound effects, and multi-language AI dubbing with perfect lip-sync.",
    heroImage: musicImg,
    features: [
      { title: "Voice & Dubbing", desc: "Voiceovers, Lip Sync, and Multi-language Voice Production.", icon: "🎙️" },
      { title: "Languages", desc: "English, Telugu, Hindi, Tamil, Kannada, Malayalam, Arabic, Japanese.", icon: "🌐" },
      { title: "Music & Sound", desc: "Background Scores, Theme Music, and Atmosphere Design.", icon: "🎵" }
    ],
    masonryImages: [ adImg, shortfilmImg, trailerImg ]
  },
  
  "ai-product-visualization": {
    title: "AI Product Visualization",
    subtitle: "Products ni realistic ga show cheyyadam.",
    description: "Perfect for SaaS, Real Estate, Fashion, and Electronics. Showcase your products realistically with stunning AI animations and explainer visuals.",
    heroImage: conceptImg,
    features: [
      { title: "Product Showcase", desc: "E-commerce visuals, Product Explainer, and Product Launch Videos.", icon: "📦" },
      { title: "Best For", desc: "SaaS, Real Estate, Electronics, Fashion, Consumer Brands.", icon: "💎" },
      { title: "Deliverables", desc: "Highly realistic product renders and animations.", icon: "🎥" }
    ],
    masonryImages: [ adImg, prodImg, postProdImg ]
  },
  "ai-content-localization": {
    title: "AI Content Localization",
    subtitle: "Global audience kosam.",
    description: "Take your film to a global audience. We provide seamless translation, dubbing, and cultural adaptation across multiple languages.",
    heroImage: preProdImg,
    features: [
      { title: "Translation", desc: "Accurate script and subtitle creation.", icon: "🔤" },
      { title: "Cultural Adaptation", desc: "Adapting content to fit local cultural nuances.", icon: "🌍" },
      { title: "Publishing", desc: "Multi-language publishing and distribution.", icon: "📡" }
    ],
    masonryImages: [ adImg, musicImg, trailerImg ]
  },
  "get-started": {
    title: "Start Your Production",
    subtitle: "Begin your creative journey with ANIMA.",
    description: "Ready to revolutionize your production pipeline? Contact us to discuss your vision, script, or campaign, and let AI elevate your storytelling.",
    heroImage: heroImg,
    features: [
      { title: "Free Consultation", desc: "Discuss your project scope and creative requirements.", icon: "💬" },
      { title: "Custom Quote", desc: "Receive a detailed breakdown of costs and timelines.", icon: "📊" },
      { title: "Full Scale Production", desc: "From ideation to final render, we've got you covered.", icon: "🚀" }
    ],
    masonryImages: [ prodImg, adImg, postProdImg ]
  }
};
