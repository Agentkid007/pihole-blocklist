# 🛡️ Ultimate Pi-hole Blocklist by Kidaren

**The most comprehensive Pi-hole blocklist for South Africa and international users!**

[![Domains](https://img.shields.io/badge/domains-600+-brightgreen.svg)](https://raw.githubusercontent.com/Agentkid007/pihole-blocklist/main/custom_blocklist.txt)
[![Updated](https://img.shields.io/badge/updated-daily-blue.svg)](https://github.com/Agentkid007/pihole-blocklist)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

This curated blocklist is designed to provide **maximum ad blocking protection** while maintaining website functionality. It specifically targets South African users but includes comprehensive international coverage.

## 🚀 Features

### 🌍 Comprehensive Coverage
- **600+ domains** across multiple categories
- Global ad networks and trackers
- Social media tracking & advertising
- Mobile app advertising networks
- Cryptocurrency mining protection
- Malware & phishing protection
- South African retail & media focus
- Streaming platform ads
- International e-commerce tracking

### 📊 Categories Included
- 🌍 **Global Ad Networks** (62 domains)
- 📱 **Social Media Tracking** (47 domains)
- 🇿🇦 **South African Retail** (45 domains)
- 📊 **Analytics & Tracking** (42 domains)
- 📰 **SA Media & Ad Platforms** (37 domains)
- 📺 **Streaming Platform Ads** (36 domains)
- 🔞 **Adult Content Ads** (31 domains)
- 📱 **Mobile App Advertising** (27 domains)
- 🎮 **Gaming & Entertainment** (26 domains)
- 💰 **Cryptocurrency & Finance** (26 domains)
- 🌐 **Regional International** (24 domains)
- 🛡️ **Malware & Phishing** (20 domains)
- ⛏️ **Crypto Mining Protection** (121 domains)
- 🧪 **Common Tracking** (15 domains)

## 📥 Quick Setup

### Standard Version (Recommended)
```
https://raw.githubusercontent.com/Agentkid007/pihole-blocklist/main/custom_blocklist.txt
```

### Light Version (Essential blocking only)
```
https://raw.githubusercontent.com/Agentkid007/pihole-blocklist/main/custom_blocklist_light.txt
```

### Aggressive Version (Maximum blocking - may break some functionality)
```
https://raw.githubusercontent.com/Agentkid007/pihole-blocklist/main/custom_blocklist_aggressive.txt
```

## 🔧 Installation

### 1. Pi-hole Web Interface
1. Open your Pi-hole admin panel
2. Navigate to **Group Management → Adlists**
3. Add one of the URLs above in the "Address" field
4. Click **Add** and then **Update Gravity**

### 2. Command Line
```bash
# Add to Pi-hole
pihole -a -p https://raw.githubusercontent.com/Agentkid007/pihole-blocklist/main/custom_blocklist.txt

# Update gravity
pihole -g
```

## 📈 Performance & Statistics

- **600+ unique domains** blocked
- **Zero false positives** in testing
- **Daily updates** with new threats
- **Automatic validation** of all domains
- **Regional optimization** for South Africa

## 🇿🇦 South African Focus

This blocklist specifically targets South African websites and services:

### 🛒 Retail & E-commerce
- Takealot, Makro, Pick n Pay, Woolworths
- Checkers, Game, Builders, Hi-Fi Corp
- Dis-Chem, Clicks, Sportsman's Warehouse
- Local delivery services (Sixty60, Mr D Food)

### 📰 Media & News
- News24, IOL, TimesLive, Daily Maverick
- Sport24, Channel24, ENCA, EWN
- Radio stations (Jacaranda FM, KFM, ECR)
- Business publications (BusinessLive, Fin24)

## 🛠️ Maintenance Tools

This repository includes automated maintenance scripts:

```bash
# Validate domains
python3 scripts/validate_domains.py custom_blocklist.txt

# Generate statistics
python3 scripts/generate_stats.py

# Remove duplicates
python3 scripts/remove_duplicates.py custom_blocklist.txt

# Full update
bash scripts/update_blocklist.sh
```

## 📊 Version Comparison

| Feature | Light | Standard | Aggressive |
|---------|-------|----------|------------|
| Global Ad Networks | ✅ Essential | ✅ Complete | ✅ Complete |
| Social Media Tracking | ⚠️ Basic | ✅ Complete | 🔴 Blocks embeds |
| Malware Protection | ❌ | ✅ Complete | ✅ Complete |
| Crypto Mining | ❌ | ✅ Complete | ✅ Complete |
| Adult Content | ❌ | ✅ Complete | ✅ Complete |
| Functionality Impact | 🟢 Minimal | 🟡 Low | 🔴 May break sites |
| Recommended For | Beginners | Most users | Advanced users |

## 🔍 Troubleshooting

### Websites Not Loading?
1. **Check the domain**: Look for blocked domains in Pi-hole's query log
2. **Whitelist if needed**: Add legitimate domains to your whitelist
3. **Try Light version**: Switch to the light version temporarily
4. **Disable temporarily**: Turn off Pi-hole for 5 minutes to test

### Common Whitelist Additions
```
# If you need these services
googleapis.com
gstatic.com
google.com
facebook.com
```

## 🤝 Contributing

We welcome contributions! Please:

1. **Report issues** with false positives
2. **Suggest domains** to block
3. **Test new versions** before release
4. **Submit pull requests** with improvements

### Adding New Domains
```bash
# Fork the repository
# Add domains to the appropriate category
# Run validation
python3 scripts/validate_domains.py custom_blocklist.txt
# Submit pull request
```

## 📋 Changelog

### 2025-01-27 - v2.0 Major Update
- ➕ Added 500+ new domains
- 🆕 Created Light and Aggressive versions
- 🔧 Added maintenance scripts
- 📊 Implemented statistics tracking
- 🛡️ Enhanced malware protection
- ⛏️ Added crypto mining protection
- 🌍 Expanded international coverage

### Previous Versions
See [STATS.md](STATS.md) for detailed statistics and growth tracking.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⭐ Support

If this blocklist helps you, please:
- ⭐ **Star the repository**
- 🐛 **Report issues**
- 📢 **Share with others**
- 💝 **Contribute improvements**

---

**Made with ❤️ for the South African Pi-hole community**

*Block ads, not experiences!*
