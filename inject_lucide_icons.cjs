const fs = require('fs');

let content = fs.readFileSync('src/pages/Services/categoryData.js', 'utf8');
content = content.replace('export const categoryData = ', 'module.exports = ');
fs.writeFileSync('tempData5.cjs', content);
const data = require('./tempData5.cjs');

const customFlows = {
  "web-development": [
    { name: "Requirements", icon: "ClipboardList" },
    { name: "Wireframing", icon: "PenTool" },
    { name: "UI/UX Design", icon: "Layout" },
    { name: "Frontend Dev", icon: "Code" },
    { name: "Backend Dev", icon: "Server" },
    { name: "Launch", icon: "Rocket" }
  ],
  "app-development": [
    { name: "Market Research", icon: "LineChart" },
    { name: "Prototyping", icon: "Smartphone" },
    { name: "App Design", icon: "Figma" },
    { name: "Native Coding", icon: "Terminal" },
    { name: "Beta Testing", icon: "TestTube" },
    { name: "App Store", icon: "DownloadCloud" }
  ],
  "software-development": [
    { name: "Discovery", icon: "Search" },
    { name: "System Design", icon: "Database" },
    { name: "Development", icon: "Code2" },
    { name: "Integration", icon: "Link" },
    { name: "UAT Testing", icon: "Users" },
    { name: "Handover", icon: "PackageCheck" }
  ],
  "aws-devops": [
    { name: "Infra Audit", icon: "Activity" },
    { name: "Architecture", icon: "Cloud" },
    { name: "CI/CD Setup", icon: "GitBranch" },
    { name: "Containerization", icon: "Box" },
    { name: "Security Check", icon: "ShieldCheck" },
    { name: "Go Live", icon: "Power" }
  ],
  "hosting-server": [
    { name: "Capacity Plan", icon: "BarChart" },
    { name: "Server Setup", icon: "HardDrive" },
    { name: "OS Config", icon: "Settings" },
    { name: "Migration", icon: "ArrowRightLeft" },
    { name: "Load Testing", icon: "Gauge" },
    { name: "Monitoring", icon: "Eye" }
  ],
  "digital-marketing": [
    { name: "SEO Audit", icon: "TrendingUp" },
    { name: "Keyword Strategy", icon: "Target" },
    { name: "Ad Creation", icon: "Image" },
    { name: "Campaign Launch", icon: "Megaphone" },
    { name: "A/B Testing", icon: "SplitSquareHorizontal" },
    { name: "Optimization", icon: "DollarSign" }
  ],
  "ai-chatbot": [
    { name: "Data Scraping", icon: "Spider" },
    { name: "Vector DB", icon: "DatabaseZap" },
    { name: "LLM Training", icon: "Brain" },
    { name: "Widget UI", icon: "MessageSquare" },
    { name: "Load Testing", icon: "Scale" },
    { name: "Deployment", icon: "Bot" }
  ],
  "ivr-services": [
    { name: "Call Tree Design", icon: "Network" },
    { name: "Voice Recording", icon: "Mic" },
    { name: "Routing Logic", icon: "GitMerge" },
    { name: "API Hooks", icon: "Webhook" },
    { name: "Beta Dialing", icon: "PhoneCall" },
    { name: "Go Live", icon: "CheckCircle" }
  ],
  "api-integration": [
    { name: "API Docs Review", icon: "BookOpen" },
    { name: "Auth Setup", icon: "Key" },
    { name: "Endpoint Map", icon: "Map" },
    { name: "Data Sync", icon: "RefreshCw" },
    { name: "Error Handling", icon: "AlertTriangle" },
    { name: "Production", icon: "Check" }
  ],
  "ecommerce-solutions": [
    { name: "Market Prep", icon: "ShoppingBag" },
    { name: "Store Setup", icon: "Store" },
    { name: "Payment Gate", icon: "CreditCard" },
    { name: "Inventory Sync", icon: "Boxes" },
    { name: "Security Scan", icon: "Lock" },
    { name: "Grand Opening", icon: "PartyPopper" }
  ],
  "security-maintenance": [
    { name: "Vulnerability Scan", icon: "Scan" },
    { name: "Threat Modeling", icon: "Siren" },
    { name: "Pen Testing", icon: "Crosshair" },
    { name: "Patching", icon: "Shield" },
    { name: "Compliance Check", icon: "FileCheck" },
    { name: "Ongoing Monitor", icon: "ActivitySquare" }
  ],
  "ai-automation": [
    { name: "Process Audit", icon: "SearchCode" },
    { name: "Bot Logic", icon: "Cpu" },
    { name: "Scripting", icon: "FileCode" },
    { name: "Dry Run", icon: "PlaySquare" },
    { name: "Refinement", icon: "Wrench" },
    { name: "Full Automation", icon: "Zap" }
  ]
};

for (const key in data) {
  const title = data[key].title;
  data[key].flowSection.flowSteps = customFlows[key] || [
    { name: "Research", icon: "Search" },
    { name: "Strategy", icon: "Target" },
    { name: "Design", icon: "Palette" },
    { name: "Execution", icon: "Settings" },
    { name: "Testing", icon: "TestTube" },
    { name: "Delivery", icon: "Rocket" }
  ];
}

const outContent = `export const categoryData = ${JSON.stringify(data, null, 2)};`;
fs.writeFileSync('src/pages/Services/categoryData.js', outContent);
fs.unlinkSync('tempData5.cjs');
console.log("Injected Lucide icon flows!");
