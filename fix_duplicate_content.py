import re

file_path = r'src\pages\Services\categoryData.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Completely new content for extendedCapabilities to ensure NO overlap with features
new_categories = {
    "web-development": [
        ("Headless Architecture", "Decoupled front-ends using Next.js and Gatsby for lightning-fast delivery."),
        ("Jamstack Solutions", "Pre-rendered static sites with dynamic APIs for ultimate security and speed."),
        ("Web Accessibility", "WCAG compliant designs ensuring your digital presence is accessible to everyone."),
        ("Third-Party Integrations", "Seamless connections with CRMs, payment gateways, and marketing automation tools."),
        ("Performance Optimization", "Advanced caching and asset optimization to achieve 100/100 Lighthouse scores."),
        ("Conversion Rate Optimization", "Data-backed UI tweaks designed specifically to turn your visitors into customers.")
    ],
    "software-development": [
        ("Microservices Architecture", "Scalable, independent services to replace monolithic bottlenecks."),
        ("DevSecOps Integration", "Automated security checks seamlessly built into your development pipeline."),
        ("Cloud-Native Apps", "Applications designed from the ground up to leverage cloud scalability."),
        ("Automated Testing Suites", "Comprehensive unit, integration, and E2E testing to guarantee reliability."),
        ("Technical Debt Reduction", "Strategic refactoring of legacy codebases for better maintainability."),
        ("Agile Team Augmentation", "Embedded experts to accelerate your internal development velocity.")
    ],
    "data-science": [
        ("Natural Language Processing", "Advanced text analysis for sentiment tracking and document classification."),
        ("Computer Vision Solutions", "Image recognition models for quality control and automated tagging."),
        ("Time-Series Forecasting", "Predictive models tailored for financial and inventory management."),
        ("Customer Segmentation", "Deep clustering algorithms to identify and target high-value user cohorts."),
        ("Recommendation Engines", "Personalized content delivery systems to boost user engagement."),
        ("Real-time Data Pipelines", "Streaming architectures processing millions of events per second.")
    ],
    "artificial-intelligence": [
        ("LLM Fine-Tuning", "Customized language models trained specifically on your proprietary data."),
        ("Autonomous Agents", "Self-directed AI workflows to handle complex, multi-step business tasks."),
        ("AI Ethics & Compliance", "Frameworks to ensure your AI models are unbiased and legally compliant."),
        ("Voice Synthesis", "Custom neural voice generation for immersive user experiences."),
        ("Predictive Maintenance", "AI algorithms forecasting equipment failures before they happen."),
        ("Generative Design", "Algorithmic generation of creative assets and product blueprints.")
    ],
    "aws-devops": [
        ("Disaster Recovery Planning", "Automated multi-region failovers to guarantee zero data loss."),
        ("Cost Optimization Strategies", "Deep architectural audits to drastically reduce your monthly AWS bill."),
        ("Chaos Engineering", "Proactive system stress-testing to build ultimate infrastructure resilience."),
        ("GitOps Workflows", "Infrastructure management driven entirely through version-controlled code."),
        ("Kubernetes Orchestration", "Expert EKS management for highly scalable microservice deployments."),
        ("24/7 Site Reliability (SRE)", "Always-on monitoring and incident response to keep your systems up.")
    ],
    "cyber-security": [
        ("Zero Trust Architecture", "Identity-first security frameworks eliminating implicit internal trust."),
        ("Threat Hunting", "Proactive, intelligence-driven searches for undetected network adversaries."),
        ("Ransomware Resilience", "Air-gapped backups and rapid recovery protocols to mitigate attacks."),
        ("Cloud Security Posture", "Automated scanning for misconfigurations in your AWS/Azure environments."),
        ("IoT Device Security", "Firmware hardening and encrypted communication for connected fleets."),
        ("Employee Phishing Sims", "Engaging awareness training to patch your human security vulnerabilities.")
    ],
    "ui-ux-design": [
        ("A/B Testing Strategies", "Data-driven experiments to scientifically validate design decisions."),
        ("Micro-interactions", "Subtle animations that delight users and guide them through workflows."),
        ("Accessibility Audits", "Comprehensive reviews ensuring inclusive design for impaired users."),
        ("Information Architecture", "Strategic restructuring of complex navigation for intuitive discovery."),
        ("Cross-platform Consistency", "Unified design languages scaling seamlessly from watch to desktop."),
        ("Design Sprint Workshops", "Rapid ideation and prototyping to solve big challenges in one week.")
    ],
    "mobile-app-development": [
        ("Wearable App Integration", "Companion applications designed perfectly for Apple Watch and Wear OS."),
        ("AR/VR Experiences", "Immersive augmented reality features powered by ARKit and ARCore."),
        ("Offline-First Architecture", "Robust local caching ensuring core functionality without internet."),
        ("IoT Companion Apps", "Secure Bluetooth and WiFi bridging for smart home hardware."),
        ("In-App Subscriptions", "Frictionless integration of RevenueCat and native billing SDKs."),
        ("App Bundle Optimization", "Aggressive size reduction techniques for faster app store downloads.")
    ],
    "digital-marketing": [
        ("Programmatic Advertising", "Algorithmic ad buying for highly precise audience targeting."),
        ("Influencer Partnerships", "Strategic vetting and management of niche brand ambassadors."),
        ("Interactive Content", "Quizzes, calculators, and assessments that drive massive engagement."),
        ("Local SEO Domination", "Hyper-targeted map and directory optimization for brick-and-mortar."),
        ("Marketing Automation", "Complex trigger-based email and SMS sequences to nurture leads."),
        ("Attribution Modeling", "Multi-touch analytics revealing the true ROI of every marketing channel.")
    ],
    "cloud-computing": [
        ("Edge Computing Solutions", "Processing data closer to users for ultra-low latency applications."),
        ("Multi-Cloud Federation", "Seamless workload balancing across AWS, Azure, and Google Cloud."),
        ("FinOps Governance", "Financial reporting frameworks to align cloud spend with business value."),
        ("Green Cloud Initiatives", "Carbon-aware architecture tracking and minimizing compute emissions."),
        ("Serverless Data Lakes", "Massively scalable storage architectures using S3 and Athena."),
        ("Mainframe Modernization", "Strategic roadmaps for migrating legacy workloads to cloud-native.")
    ],
    "blockchain-development": [
        ("Layer 2 Scaling", "Optimistic and ZK-rollup integrations for low-fee transactions."),
        ("DAO Governance", "Voting contracts and treasury management for decentralized orgs."),
        ("Tokenization Platforms", "Fractional ownership systems for real estate and physical assets."),
        ("Cross-Chain Bridges", "Secure interoperability protocols connecting disparate blockchains."),
        ("Zero-Knowledge Proofs", "Privacy-preserving identity and verification without data exposure."),
        ("Smart Contract Audits", "Rigorous security reviews to prevent devastating protocol hacks.")
    ],
    "app-development": [
        ("Wearable App Integration", "Companion applications designed perfectly for Apple Watch and Wear OS."),
        ("AR/VR Experiences", "Immersive augmented reality features powered by ARKit and ARCore."),
        ("Offline-First Architecture", "Robust local caching ensuring core functionality without internet."),
        ("IoT Companion Apps", "Secure Bluetooth and WiFi bridging for smart home hardware."),
        ("In-App Subscriptions", "Frictionless integration of RevenueCat and native billing SDKs."),
        ("App Bundle Optimization", "Aggressive size reduction techniques for faster app store downloads.")
    ]
}

# Find and replace each extendedCapabilities block
for cat_key, caps in new_categories.items():
    # Build replacement string, preserving exact UI properties
    replacement_items = []
    
    design_patterns = [
        {"span": 1, "bgColor": "#B48366", "textColor": "#ffffff", "image": "https://images.unsplash.com/photo-1547658719-da2b51169166?q=80&w=600&auto=format&fit=crop"},
        {"span": 1, "bgColor": "#E2C3B7", "textColor": "#0E1F1A", "image": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?q=80&w=600&auto=format&fit=crop"},
        {"span": 2, "bgColor": "#114051", "textColor": "#ffffff", "image": "https://images.unsplash.com/photo-1512428559087-560fa5ceab42?q=80&w=800&auto=format&fit=crop"},
        {"span": 2, "bgColor": "#1A3129", "textColor": "#ffffff", "image": "https://images.unsplash.com/photo-1561070791-2526d30994b5?q=80&w=800&auto=format&fit=crop"},
        {"span": 1, "bgColor": "#DDE2CD", "textColor": "#0E1F1A", "image": "https://images.unsplash.com/photo-1581291518857-4e27b48ff24e?q=80&w=600&auto=format&fit=crop"},
        {"span": 1, "bgColor": "#C3DBE3", "textColor": "#0E1F1A", "image": "https://images.unsplash.com/photo-1501250987900-2118ddeca0f6?q=80&w=600&auto=format&fit=crop"}
    ]
    
    for i, (title, desc) in enumerate(caps):
        p = design_patterns[i]
        item_json = f'''      {{
        "title": "{title}",
        "desc": "{desc}",
        "image": "{p["image"]}",
        "bgColor": "{p["bgColor"]}",
        "textColor": "{p["textColor"]}",
        "span": {p["span"]}
      }}'''
        replacement_items.append(item_json)
        
    full_array_str = '    "extendedCapabilities": [\n' + ',\n'.join(replacement_items) + '\n    ]'
    
    # We must find the specific category's extendedCapabilities and replace it
    # Pattern: "category-name": { ... "extendedCapabilities": [ ... ]
    # We can do this safely by splitting the file by category keys or just using regex carefully.
    
    # Let's use a regex that finds the key, and then non-greedily matches up to "extendedCapabilities": [ ... ]
    # It's safer to just replace it using string methods if we are careful.
    
    pattern = r'("?' + re.escape(cat_key) + r'"?:\s*\{[\s\S]*?)"extendedCapabilities":\s*\[.*?\]'
    
    def replacer(match):
        return match.group(1) + full_array_str
        
    content = re.sub(pattern, replacer, content, count=1, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected brand new non-overlapping content!")
