import os

TARGET_DIR = r"c:\Mr-Anonymous-Guy\Mr-Anonymous-Guy\Mr-Anonymous-Guy"

def make_header_dark(title_text, icon_emoji):
    return f'''<svg viewBox="0 0 900 70" width="900" height="70" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="hdr-bg" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#000000"/>
      <stop offset="30%" stop-color="#ff004d"/>
      <stop offset="70%" stop-color="#570000"/>
      <stop offset="100%" stop-color="#000000"/>
    </linearGradient>
    <linearGradient id="hdr-line" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ff004d" stop-opacity="0"/>
      <stop offset="50%" stop-color="#fdffff"/>
      <stop offset="100%" stop-color="#ff004d" stop-opacity="0"/>
    </linearGradient>
    <filter id="hdr-glow">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@800;900&amp;display=swap');
    .hdr-txt {{ font-family: 'Outfit', sans-serif; font-weight: 900; font-size: 24px; fill: #fdffff; letter-spacing: 2px; }}
    .star-hdr {{ animation: starFlash 2s infinite ease-in-out; }}
    @keyframes starFlash {{ 0%, 100% {{ opacity: 0.3; transform: scale(0.8); }} 50% {{ opacity: 1; transform: scale(1.3); }} }}
  </style>

  <rect width="900" height="70" rx="12" fill="url(#hdr-bg)"/>
  <rect width="900" height="70" rx="12" fill="none" stroke="#ff004d" stroke-width="2" filter="url(#hdr-glow)"/>

  <!-- Decorative Stars -->
  <circle cx="40" cy="35" r="3" fill="#fdffff" class="star-hdr"/>
  <circle cx="860" cy="35" r="3" fill="#fdffff" class="star-hdr"/>

  <!-- Title Text -->
  <text x="450" y="44" class="hdr-txt" text-anchor="middle" filter="url(#hdr-glow)">{icon_emoji} {title_text}</text>

  <!-- Bottom Accent Shimmer Line -->
  <rect x="150" y="60" width="600" height="2" fill="url(#hdr-line)"/>
</svg>'''

def make_header_light(title_text, icon_emoji):
    return f'''<svg viewBox="0 0 900 70" width="900" height="70" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="hdr-light-bg" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="50%" stop-color="#ffe6ed"/>
      <stop offset="100%" stop-color="#ffffff"/>
    </linearGradient>
    <linearGradient id="hdr-light-line" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#000000" stop-opacity="0"/>
      <stop offset="50%" stop-color="#ff004d"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@800;900&amp;display=swap');
    .hdr-light-txt {{ font-family: 'Outfit', sans-serif; font-weight: 900; font-size: 24px; fill: #000000; letter-spacing: 2px; }}
  </style>

  <rect width="900" height="70" rx="12" fill="url(#hdr-light-bg)" stroke="#000000" stroke-width="2"/>

  <!-- Title Text -->
  <text x="450" y="44" class="hdr-light-txt" text-anchor="middle">{icon_emoji} {title_text}</text>

  <!-- Bottom Accent Shimmer Line -->
  <rect x="150" y="60" width="600" height="2" fill="url(#hdr-light-line)"/>
</svg>'''

headers = [
    ("sec-projects", "FEATURED AI &amp; FULL-STACK PROJECTS", "🤖"),
    ("sec-stats", "GITHUB STATS &amp; TOP LANGUAGES", "📊"),
    ("sec-heatmap", "REAL-TIME JET CONTRIBUTION HEATMAP", "🛩️"),
    ("sec-trophies", "DEVELOPER ACHIEVEMENTS &amp; TROPHIES", "🏆"),
    ("sec-connect", "LET'S CONNECT &amp; COLLABORATE", "📫")
]

for filename_prefix, title, emoji in headers:
    dark_svg = make_header_dark(title, emoji)
    light_svg = make_header_light(title, emoji)

    with open(os.path.join(TARGET_DIR, f"{filename_prefix}-dark.svg"), "w", encoding="utf-8") as f:
        f.write(dark_svg)
    with open(os.path.join(TARGET_DIR, f"{filename_prefix}-light.svg"), "w", encoding="utf-8") as f:
        f.write(light_svg)

    print(f"Created {filename_prefix}-dark.svg & {filename_prefix}-light.svg")


# Update README.md with theme-switching header banners and styled section containers
readme_md = '''<div align="center">

<!-- ✨ Animated Hero Banner (Dark / Light Auto-Switch) ✨ -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./banner.svg?v=1">
  <source media="(prefers-color-scheme: light)" srcset="./banner-light.svg?v=1">
  <img src="./banner.svg?v=1" alt="Mr. Anonymous — Student & AI Engineer" width="100%"/>
</picture>

<br/><br/>

<!-- 🤖 FEATURED PROJECTS HEADER -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./sec-projects-dark.svg?v=1">
  <source media="(prefers-color-scheme: light)" srcset="./sec-projects-light.svg?v=1">
  <img src="./sec-projects-dark.svg?v=1" alt="Featured Projects" width="100%"/>
</picture>

</div>

<br/>

<table align="center" border="0" width="100%">
<tr>
<td width="36%" align="center" valign="middle">

<!-- 🪪 Swinging Lanyard ID Card (React Bits style, pure SVG) -->
<img src="./lanyard.svg?v=2" alt="Mr. Anonymous ID badge" width="330"/>

</td>
<td width="64%" valign="middle">

| 🚀 Project | 💻 Tech Stack | 📌 Description |
|:---|:---:|:---|
| [🏥 **ArogyaAI**](https://github.com/Mr-Anonymous-Guy/ArogyaAI) | `Python` `FastAPI` `RAG` `React` | AI-powered healthcare intelligence platform with risk prediction, medical pipelines &amp; explainable insights. |
| [💡 **FinSmart**](https://github.com/Mr-Anonymous-Guy/FinSmart) | `React` `FastAPI` `PostgreSQL` | Personal finance dashboard with AI-driven budgeting, transaction tracking &amp; financial insights. |
| [🌐 **Portfolio App**](https://anonymousguy.online/) | `Next.js` `TypeScript` `Framer` | Personal developer portfolio showcasing advanced animations, interactive UI &amp; smooth state management. |

<br/>

> ⚡ *"Think. Build. Ship. Repeat."*

</td>
</tr>
</table>

<br/>

<div align="center">

<!-- 📊 STATS & LANGUAGES HEADER -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./sec-stats-dark.svg?v=1">
  <source media="(prefers-color-scheme: light)" srcset="./sec-stats-light.svg?v=1">
  <img src="./sec-stats-dark.svg?v=1" alt="GitHub Stats & Languages" width="100%"/>
</picture>

<br/><br/>

<img src="./stats.svg?v=2" alt="GitHub Stats" height="185"/>
<img src="./langs.svg?v=3" alt="Top Languages" height="185"/>

<br/><br/>

<!-- 🛩️ JET HEATMAP HEADER -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./sec-heatmap-dark.svg?v=1">
  <source media="(prefers-color-scheme: light)" srcset="./sec-heatmap-light.svg?v=1">
  <img src="./sec-heatmap-dark.svg?v=1" alt="Real-Time Jet Heatmap" width="100%"/>
</picture>

<br/><br/>

![GitHub jet heatmap](https://raw.githubusercontent.com/Mr-Anonymous-Guy/Mr-Anonymous-Guy/main/dist/github-jet.svg)

<br/><br/>

<!-- 🏆 ACHIEVEMENTS & TROPHIES HEADER -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./sec-trophies-dark.svg?v=1">
  <source media="(prefers-color-scheme: light)" srcset="./sec-trophies-light.svg?v=1">
  <img src="./sec-trophies-dark.svg?v=1" alt="Developer Achievements" width="100%"/>
</picture>

<br/><br/>

<img src="./trophies.svg?v=2" alt="Developer Trophies" width="95%"/>

<br/><br/>

<!-- 📫 LET'S CONNECT HEADER -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./sec-connect-dark.svg?v=1">
  <source media="(prefers-color-scheme: light)" srcset="./sec-connect-light.svg?v=1">
  <img src="./sec-connect-dark.svg?v=1" alt="Let's Connect" width="100%"/>
</picture>

<br/><br/>

<a href="mailto:mr.anonymous071105@gmail.com"><img src="https://img.shields.io/badge/Email-ff004d?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/></a>
<a href="https://github.com/Mr-Anonymous-Guy"><img src="https://img.shields.io/badge/GitHub-280000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>
<a href="https://www.linkedin.com/in/mr-anonymous-guy/"><img src="https://img.shields.io/badge/LinkedIn-ff004d?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
<a href="https://x.com/anonymous_22181"><img src="https://img.shields.io/badge/X%2FTwitter-280000?style=for-the-badge&logo=x&logoColor=white" alt="X/Twitter"/></a>
<a href="https://anonymousguy.online/"><img src="https://img.shields.io/badge/Portfolio-ff004d?style=for-the-badge&logo=vercel&logoColor=white" alt="Portfolio"/></a>

<br/><br/>

<img src="https://komarev.com/ghpvc/?username=Mr-Anonymous-Guy&color=ff004d&style=for-the-badge&label=PROFILE+VIEWS" alt="Profile views"/>

<br/><br/>

*⚡ Always innovating, always building the future with AI.*

</div>
'''

with open(os.path.join(TARGET_DIR, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme_md)

print("Updated README.md with background header banners!")
