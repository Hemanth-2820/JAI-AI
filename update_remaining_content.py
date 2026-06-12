import os
import re

file_path = r'src\pages\Services\categoryData.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

missing_categories = {
    "hosting-server": [
        ("High-Availability Clusters", "Load-balanced server architectures guaranteeing 99.99% uptime."),
        ("DDoS Mitigation", "Enterprise-grade traffic filtering to keep your servers online during attacks."),
        ("Automated Backups", "Geographically redundant snapshotting for instant disaster recovery."),
        ("Edge Caching", "Global CDN integration to deliver content to users in milliseconds."),
        ("Bare Metal Servers", "Dedicated, unshared hardware for maximum computational performance."),
        ("Server Migration", "Zero-downtime transfers of your existing infrastructure to our ecosystem.")
    ],
    "ai-chatbot": [
        ("Contextual NLP", "Chatbots that understand intent, nuance, and conversational history."),
        ("Omnichannel Routing", "Seamless deployment across WhatsApp, Messenger, Web, and SMS."),
        ("Human Handoff", "Intelligent escalation to live agents when complex issues arise."),
        ("Sentiment Analysis", "Real-time emotion detection to adjust the bot's tone dynamically."),
        ("Voice Bot Integration", "Spoken conversational interfaces powered by advanced speech-to-text."),
        ("Knowledge Base Sync", "Bots that dynamically read and answer questions from your company docs.")
    ],
    "ivr-services": [
        ("Dynamic Call Routing", "Intelligently direct callers to the right department based on CRM data."),
        ("Speech Recognition IVR", "Allow callers to simply speak their needs instead of pressing buttons."),
        ("Visual IVR", "Send an SMS link to transition callers to a digital smartphone menu."),
        ("Queue Callbacks", "Let customers keep their place in line without staying on hold."),
        ("Multi-language Prompts", "Automatic routing based on the caller's geographic location or preference."),
        ("Post-call Surveys", "Automated feedback collection immediately after agent interaction.")
    ],
    "api-integration": [
        ("Legacy System Bridging", "Connect modern web apps to older on-premise mainframe databases."),
        ("Custom Middleware", "Tailored translation layers to map incompatible data structures."),
        ("OAuth2 Authentication", "Secure, token-based connection protocols for third-party access."),
        ("Webhooks Architecture", "Real-time, event-driven data pushing instead of costly constant polling."),
        ("GraphQL Migration", "Transition your REST APIs to flexible, client-driven query endpoints."),
        ("Rate Limiting", "Enterprise traffic control to protect your internal systems from overload.")
    ],
    "ecommerce-solutions": [
        ("Headless Commerce", "Decouple your frontend experience from the Shopify or Magento backend."),
        ("Abandoned Cart Recovery", "Automated email and SMS sequences to drastically boost conversion rates."),
        ("Dynamic Pricing", "Algorithmic price adjustments based on real-time market demand and inventory."),
        ("AR Product Previews", "Let customers visualize products in their physical space before buying."),
        ("Subscription Billing", "Seamless integration of recurring revenue models and membership tiers."),
        ("Multi-currency Checkouts", "Localized payment gateways reducing international friction.")
    ],
    "security-maintenance": [
        ("Penetration Testing", "Ethical hacking simulations to expose vulnerabilities before bad actors do."),
        ("24/7 Threat Monitoring", "Always-on Security Operations Center (SOC) analyzing network anomalies."),
        ("Patch Management", "Automated updates of core CMS systems and plugins to close zero-days."),
        ("Data Encryption", "Military-grade AES-256 encryption for data at rest and in transit."),
        ("Uptime Monitoring", "Ping checks every 30 seconds with immediate SMS alerts on failure."),
        ("Compliance Auditing", "Quarterly reviews to ensure strict adherence to GDPR, HIPAA, or SOC2.")
    ],
    "ai-automation": [
        ("RPA Implementation", "Robotic Process Automation to eliminate repetitive data-entry tasks."),
        ("Predictive Analytics", "Machine learning models forecasting inventory shortages or churn."),
        ("Document Extraction", "Optical Character Recognition (OCR) to turn PDFs into structured data."),
        ("Automated Workflows", "Complex Zapier and Make.com integrations connecting all your SaaS tools."),
        ("Dynamic Content Generation", "AI writing models drafting personalized emails at scale."),
        ("Smart Quality Control", "Computer vision algorithms inspecting manufacturing lines in real-time.")
    ],
    "ai-creative-consulting": [
        ("Prompt Engineering", "Crafting mathematically precise inputs to yield stunning AI outputs."),
        ("Workflow Audits", "Analyzing your creative pipeline to find high-ROI AI integration points."),
        ("Custom Model Training", "Fine-tuning Stable Diffusion models strictly on your brand assets."),
        ("AI Ethics Strategy", "Developing corporate guidelines for responsible generative AI usage."),
        ("Tool Stack Curation", "Selecting the exact mix of Midjourney, Runway, and ChatGPT for your needs."),
        ("Creative Upskilling", "Hands-on workshops teaching your art directors how to pilot AI tools.")
    ],
    "ai-film-production": [
        ("Generative Storyboarding", "Rapidly visualizing scenes and camera angles using text-to-image models."),
        ("Virtual Scouting", "Generating impossible locations and backdrops without leaving the studio."),
        ("AI Voice Acting", "Synthesizing ultra-realistic, emotive scratch tracks and voiceovers."),
        ("Algorithmic Editing", "Machine learning tools that automatically rough-cut footage to the beat."),
        ("Style Transfer", "Applying distinct artistic styles to raw video footage in post-production."),
        ("Deepfake Doubles", "Seamless facial replacement for stunt doubles or dialogue localization.")
    ],
    "ai-commercial-production": [
        ("Dynamic Ad Variations", "Using AI to generate 1,000 personalized versions of a single commercial."),
        ("Virtual Influencers", "Designing entirely digital brand ambassadors powered by AI logic."),
        ("Predictive Hook Testing", "Analyzing initial script concepts to predict viewer retention rates."),
        ("Generative Product Backgrounds", "Placing 3D product renders into infinite photorealistic environments."),
        ("Automated Captioning", "Kinetic, highly-engaging subtitles generated instantly for social media."),
        ("Mood Board Generation", "Pitching commercial concepts with hyper-specific AI-generated imagery.")
    ],
    "ai-vfx-post": [
        ("Automated Rotoscoping", "Neural networks isolating complex subjects without manual frame-by-frame masking."),
        ("AI Upscaling", "Enhancing archival or low-res footage to pristine 4K and 8K resolution."),
        ("Inpainting Removal", "Flawlessly erasing wires, boom mics, or logos from moving shots."),
        ("Generative Fill", "Extending set backgrounds or altering environments natively in post."),
        ("Color Match AI", "Automatically grading footage from different cameras to match perfectly."),
        ("Audio Denoising", "Isolating crisp dialogue from heavy wind or background city noise.")
    ],
    "ai-animation-production": [
        ("Motion Capture Synthesis", "Extracting 3D skeletal data directly from standard 2D video files."),
        ("In-betweening AI", "Automatically generating smooth transition frames between key poses."),
        ("Text-to-3D Models", "Generating rigged character models from simple text descriptions."),
        ("Lip Sync Automation", "Matching character mouth shapes perfectly to any uploaded audio track."),
        ("Generative Textures", "Creating infinite, non-repeating material textures using AI diffusion."),
        ("Style Interpolation", "Blending 2D anime styles with 3D renders for unique visual aesthetics.")
    ]
}

# The span pattern
design_patterns = [
    {"span": 1, "bgColor": "#B48366", "textColor": "#ffffff"},
    {"span": 1, "bgColor": "#E2C3B7", "textColor": "#0E1F1A"},
    {"span": 2, "bgColor": "#114051", "textColor": "#ffffff"},
    {"span": 2, "bgColor": "#1A3129", "textColor": "#ffffff"},
    {"span": 1, "bgColor": "#DDE2CD", "textColor": "#0E1F1A"},
    {"span": 1, "bgColor": "#C3DBE3", "textColor": "#0E1F1A"}
]

for cat_key, caps in missing_categories.items():
    replacement_items = []
    
    for i, (title, desc) in enumerate(caps):
        p = design_patterns[i]
        
        # We will use dummy image URLs here because we will immediately run generate_semantic_svgs.py
        # which overwrites the "image" field anyway!
        item_json = f'''      {{
        "title": "{title}",
        "desc": "{desc}",
        "image": "/images/animated/dummy.svg",
        "bgColor": "{p["bgColor"]}",
        "textColor": "{p["textColor"]}",
        "span": {p["span"]}
      }}'''
        replacement_items.append(item_json)
        
    full_array_str = '    "extendedCapabilities": [\n' + ',\n'.join(replacement_items) + '\n    ]'
    
    # Safely replace using regex
    pattern = r'("?' + re.escape(cat_key) + r'"?:\s*\{[\s\S]*?)"extendedCapabilities":\s*\[.*?\]'
    
    def replacer(match):
        return match.group(1) + full_array_str
        
    content = re.sub(pattern, replacer, content, count=1, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated content for all missing categories!")
