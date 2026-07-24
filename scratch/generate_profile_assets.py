import os
import base64
from PIL import Image
import io

# 1. Prepare Base64 Image strings
TARGET_DIR = r"c:\Mr-Anonymous-Guy\Mr-Anonymous-Guy\Mr-Anonymous-Guy"
ORIG_IMG_PATH = os.path.join(TARGET_DIR, "public", "Images", "Image.png")

print("Processing character image from:", ORIG_IMG_PATH)
img = Image.open(ORIG_IMG_PATH).convert('RGBA')

# White background removal
import numpy as np
arr = np.array(img)
r, g, b, a = arr[:,:,0], arr[:,:,1], arr[:,:,2], arr[:,:,3]
dist = np.sqrt((255 - r.astype(float))**2 + (255 - g.astype(float))**2 + (255 - b.astype(float))**2)
alpha = np.clip((dist - 15) / 20.0 * 255, 0, 255).astype(np.uint8)
arr[:,:,3] = np.minimum(a, alpha)
transparent_img = Image.fromarray(arr)

# Resize main character image for banner (width 480px for crisp render and light payload)
w, h = transparent_img.size
new_h = int(h * (480.0 / w))
char_banner = transparent_img.resize((480, new_h), Image.Resampling.LANCZOS)
buf_char = io.BytesIO()
char_banner.save(buf_char, format='PNG', optimize=True)
B64_CHAR = base64.b64encode(buf_char.getvalue()).decode('utf-8')

# Crop avatar for lanyard (face region centered)
crop_box = (200, 160, 520, 480)
avatar_crop = transparent_img.crop(crop_box).resize((220, 220), Image.Resampling.LANCZOS)
buf_av = io.BytesIO()
avatar_crop.save(buf_av, format='PNG', optimize=True)
B64_AVATAR = base64.b64encode(buf_av.getvalue()).decode('utf-8')

print("Character Base64 ready. Length:", len(B64_CHAR))
print("Avatar Base64 ready. Length:", len(B64_AVATAR))

# Colors
# Palette: #fdffff (white), #ff004d (hot fuchsia), #570000 (black cherry), #280000 (rich mahogany), #000000 (black)

# --- 1. banner.svg (Dark Mode) ---
banner_dark_svg = f'''<svg viewBox="0 0 1280 740" width="1280" height="740" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Background Gradients -->
    <radialGradient id="bg-grad" cx="70%" cy="30%" r="85%">
      <stop offset="0%" stop-color="#570000" stop-opacity="0.5"/>
      <stop offset="45%" stop-color="#280000" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#000000"/>
    </radialGradient>
    
    <linearGradient id="neon-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#fdffff"/>
      <stop offset="50%" stop-color="#ff004d"/>
      <stop offset="100%" stop-color="#fdffff"/>
    </linearGradient>

    <linearGradient id="scan-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ff004d" stop-opacity="0"/>
      <stop offset="50%" stop-color="#ff004d" stop-opacity="0.85"/>
      <stop offset="100%" stop-color="#ff004d" stop-opacity="0"/>
    </linearGradient>

    <linearGradient id="card-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ff004d" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#570000" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#ff004d" stop-opacity="0.6"/>
    </linearGradient>

    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
    
    <filter id="neon-glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="4" result="blur1"/>
      <feGaussianBlur stdDeviation="12" result="blur2"/>
      <feMerge>
        <feMergeNode in="blur2"/>
        <feMergeNode in="blur1"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <clipPath id="banner-clip">
      <rect x="0" y="0" width="1280" height="740" rx="20" ry="20"/>
    </clipPath>
  </defs>

  <style>
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600&amp;family=Outfit:wght@400;600;800;900&amp;display=swap');

    .bg {{ fill: url(#bg-grad); }}
    .title {{ font-family: 'Outfit', sans-serif; font-weight: 900; font-size: 54px; fill: url(#neon-grad); letter-spacing: -1px; }}
    .terminal-text {{ font-family: 'Fira Code', monospace; font-size: 15px; fill: #fdffff; }}
    .code-text {{ font-family: 'Fira Code', monospace; font-size: 14px; fill: #fdffff; }}
    .pill-text {{ font-family: 'Outfit', sans-serif; font-weight: 600; font-size: 13px; fill: #fdffff; }}
    .neon-text {{ font-family: 'Outfit', sans-serif; font-weight: 800; font-size: 18px; fill: #ff004d; letter-spacing: 3px; filter: url(#neon-glow); }}

    .flicker {{
      animation: neonFlicker 3s infinite ease-in-out;
    }}
    
    @keyframes neonFlicker {{
      0%, 100% {{ opacity: 1; }}
      3%, 6% {{ opacity: 0.4; }}
      7%, 9% {{ opacity: 1; }}
      50% {{ opacity: 0.95; }}
      52%, 54% {{ opacity: 0.5; }}
      55% {{ opacity: 1; }}
    }}

    .star {{
      animation: starBlink 2.5s infinite ease-in-out;
    }}
    @keyframes starBlink {{
      0%, 100% {{ opacity: 0.2; transform: scale(0.8); }}
      50% {{ opacity: 1; transform: scale(1.3); }}
    }}
  </style>

  <g clip-path="url(#banner-clip)">
    <!-- Base Background -->
    <rect width="1280" height="740" class="bg"/>
    <rect width="1280" height="740" fill="none" stroke="url(#card-border)" stroke-width="4" rx="20"/>

    <!-- Ambient glowing circle behind character -->
    <circle cx="980" cy="370" r="280" fill="#ff004d" opacity="0.12" filter="url(#glow)"/>

    <!-- Floating Particles & Stars -->
    <g opacity="0.6">
      <circle cx="120" cy="100" r="2.5" fill="#ff004d" class="star" style="animation-delay: 0s;"/>
      <circle cx="550" cy="80" r="2" fill="#fdffff" class="star" style="animation-delay: 0.7s;"/>
      <circle cx="620" cy="220" r="3" fill="#ff004d" class="star" style="animation-delay: 1.4s;"/>
      <circle cx="1150" cy="140" r="2" fill="#fdffff" class="star" style="animation-delay: 0.3s;"/>
      <circle cx="720" cy="650" r="2.5" fill="#ff004d" class="star" style="animation-delay: 1.1s;"/>
      <circle cx="1200" cy="620" r="3" fill="#fdffff" class="star" style="animation-delay: 1.8s;"/>
    </g>

    <!-- LEFT COLUMN CONTENT -->

    <!-- 1. Terminal Bar -->
    <rect x="55" y="45" width="580" height="42" rx="8" fill="#120207" stroke="#570000" stroke-width="1.5"/>
    <circle cx="75" cy="66" r="6" fill="#ff5f56"/>
    <circle cx="95" cy="66" r="6" fill="#ffbd2e"/>
    <circle cx="115" cy="66" r="6" fill="#27c93f"/>
    <text x="140" y="71" class="terminal-text">user@dev:~$ <tspan fill="#ff004d">cat README.md</tspan></text>
    <rect x="350" y="58" width="8" height="17" fill="#ff004d">
      <animate attributeName="opacity" values="1;0;1" dur="0.8s" repeatCount="indefinite"/>
    </rect>

    <!-- 2. Main Title Name -->
    <text x="55" y="145" class="title" filter="url(#glow)">Mr. Anonymous</text>

    <!-- 3. Cycling Role Subtitle -->
    <text x="58" y="182" font-family="'Outfit', sans-serif" font-weight="600" font-size="22" fill="#ff004d">
      <animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.1;0.9;1" dur="4s" repeatCount="indefinite"/>
      <tspan>⚡ </tspan>
      <animate attributeName="textContent" 
               values="Student / AI Engineer;LLM &amp; RAG Architecture Specialist;Autonomous AI Agent Developer;Full-Stack Innovator" 
               dur="16s" repeatCount="indefinite"/>
    </text>

    <!-- 4. Tagline Quote Card -->
    <rect x="55" y="210" width="580" height="48" rx="8" fill="#18040b" stroke="#570000" stroke-width="1"/>
    <text x="75" y="240" font-family="'Fira Code', monospace" font-size="15" fill="#fdffff">
      <tspan fill="#ff004d">"</tspan>Think. Build. Ship. Repeat.<tspan fill="#ff004d">"</tspan>
    </text>

    <!-- 5. Tech Stack Pills -->
    <g transform="translate(55, 275)">
      <!-- Row 1 -->
      <g transform="translate(0,0)">
        <rect width="90" height="30" rx="15" fill="#280000" stroke="#ff004d" stroke-width="1"/>
        <text x="45" y="20" class="pill-text" text-anchor="middle">🐍 Python</text>
      </g>
      <g transform="translate(100,0)">
        <rect width="135" height="30" rx="15" fill="#280000" stroke="#ff004d" stroke-width="1"/>
        <text x="67" y="20" class="pill-text" text-anchor="middle">🤖 AI Engineering</text>
      </g>
      <g transform="translate(245,0)">
        <rect width="85" height="30" rx="15" fill="#280000" stroke="#ff004d" stroke-width="1"/>
        <text x="42" y="20" class="pill-text" text-anchor="middle">🧠 LLMs</text>
      </g>
      <g transform="translate(340,0)">
        <rect width="80" height="30" rx="15" fill="#280000" stroke="#ff004d" stroke-width="1"/>
        <text x="40" y="20" class="pill-text" text-anchor="middle">⚡ RAG</text>
      </g>
      <g transform="translate(430,0)">
        <rect width="95" height="30" rx="15" fill="#280000" stroke="#ff004d" stroke-width="1"/>
        <text x="47" y="20" class="pill-text" text-anchor="middle">🚀 FastAPI</text>
      </g>

      <!-- Row 2 -->
      <g transform="translate(0,40)">
        <rect width="115" height="30" rx="15" fill="#280000" stroke="#ff004d" stroke-width="1"/>
        <text x="57" y="20" class="pill-text" text-anchor="middle">📘 TypeScript</text>
      </g>
      <g transform="translate(125,40)">
        <rect width="95" height="30" rx="15" fill="#280000" stroke="#ff004d" stroke-width="1"/>
        <text x="47" y="20" class="pill-text" text-anchor="middle">▲ Next.js</text>
      </g>
      <g transform="translate(230,40)">
        <rect width="85" height="30" rx="15" fill="#280000" stroke="#ff004d" stroke-width="1"/>
        <text x="42" y="20" class="pill-text" text-anchor="middle">⚛️ React</text>
      </g>
      <g transform="translate(325,40)">
        <rect width="105" height="30" rx="15" fill="#280000" stroke="#ff004d" stroke-width="1"/>
        <text x="52" y="20" class="pill-text" text-anchor="middle">🐘 PostgreSQL</text>
      </g>
      <g transform="translate(440,40)">
        <rect width="85" height="30" rx="15" fill="#280000" stroke="#ff004d" stroke-width="1"/>
        <text x="42" y="20" class="pill-text" text-anchor="middle">🐳 Docker</text>
      </g>
    </g>

    <!-- 6. Code Editor Snippet Window -->
    <g transform="translate(55, 365)">
      <rect width="580" height="245" rx="10" fill="#0d0206" stroke="#570000" stroke-width="1.5"/>
      <rect width="580" height="30" rx="10" fill="#1c040d"/>
      <!-- Window title -->
      <text x="20" y="20" font-family="'Fira Code', monospace" font-size="12" fill="#a0a0a0">ai_agent_core.py</text>
      
      <!-- Code lines -->
      <g class="code-text" transform="translate(20, 55)">
        <text y="0"><tspan fill="#ff004d">class</tspan> <tspan fill="#fdffff">AIAgent</tspan>:</text>
        <text y="24">    <tspan fill="#ff004d">def</tspan> <tspan fill="#fdffff">__init__</tspan>(self, dev=<tspan fill="#ff004d">"Mr. Anonymous"</tspan>):</text>
        <text y="48">        self.role = <tspan fill="#ff004d">"Student &amp; AI Engineer"</tspan></text>
        <text y="72">        self.stack = [<tspan fill="#ff004d">"Python"</tspan>, <tspan fill="#ff004d">"RAG"</tspan>, <tspan fill="#ff004d">"FastAPI"</tspan>]</text>
        <text y="96">        self.focus = <tspan fill="#ff004d">"Autonomous AI Agents"</tspan></text>
        <text y="120">    <tspan fill="#ff004d">async def</tspan> <tspan fill="#fdffff">ship_innovation</tspan>(self):</text>
        <text y="144">        <tspan fill="#ff004d">return</tspan> <tspan fill="#fdffff">await</tspan> self.build_future()</text>
      </g>
    </g>

    <!-- 7. Flickering Neon Sign -->
    <g transform="translate(55, 640)">
      <rect width="580" height="52" rx="8" fill="#150208" stroke="#ff004d" stroke-width="1.5" filter="url(#glow)"/>
      <text x="290" y="32" class="neon-text flicker" text-anchor="middle">⚡ KEEP CODING • KEEP GROWING ⚡</text>
    </g>

    <!-- RIGHT COLUMN: Character Image & Hologram Scanner -->
    <g transform="translate(690, 20)">
      <!-- Character Base64 Image -->
      <image href="data:image/png;base64,{B64_CHAR}" width="540" height="710" x="0" y="0"/>
      
      <!-- Continuous Hologram Scan Line -->
      <rect x="0" y="0" width="540" height="25" fill="url(#scan-grad)">
        <animate attributeName="y" values="0;680;0" dur="3.8s" repeatCount="indefinite"/>
      </rect>
    </g>
  </g>
</svg>'''

with open(os.path.join(TARGET_DIR, "banner.svg"), "w", encoding="utf-8") as f:
    f.write(banner_dark_svg)

print("Created banner.svg")


# --- 2. banner-light.svg (Light Mode) ---
banner_light_svg = f'''<svg viewBox="0 0 1280 740" width="1280" height="740" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Background Gradients for Light Mode -->
    <radialGradient id="bg-light-grad" cx="70%" cy="30%" r="85%">
      <stop offset="0%" stop-color="#fff0f4"/>
      <stop offset="50%" stop-color="#fde8ed"/>
      <stop offset="100%" stop-color="#fdffff"/>
    </radialGradient>
    
    <linearGradient id="neon-light-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#280000"/>
      <stop offset="50%" stop-color="#ff004d"/>
      <stop offset="100%" stop-color="#570000"/>
    </linearGradient>

    <linearGradient id="scan-light-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ff004d" stop-opacity="0"/>
      <stop offset="50%" stop-color="#ff004d" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#ff004d" stop-opacity="0"/>
    </linearGradient>

    <clipPath id="banner-light-clip">
      <rect x="0" y="0" width="1280" height="740" rx="20" ry="20"/>
    </clipPath>
  </defs>

  <style>
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600&amp;family=Outfit:wght@400;600;800;900&amp;display=swap');

    .bg-light {{ fill: url(#bg-light-grad); }}
    .title-light {{ font-family: 'Outfit', sans-serif; font-weight: 900; font-size: 54px; fill: url(#neon-light-grad); letter-spacing: -1px; }}
    .terminal-text-light {{ font-family: 'Fira Code', monospace; font-size: 15px; fill: #280000; }}
    .code-text-light {{ font-family: 'Fira Code', monospace; font-size: 14px; fill: #280000; }}
    .pill-text-light {{ font-family: 'Outfit', sans-serif; font-weight: 600; font-size: 13px; fill: #fdffff; }}
    .neon-text-light {{ font-family: 'Outfit', sans-serif; font-weight: 800; font-size: 18px; fill: #ff004d; letter-spacing: 3px; }}

    .star-light {{
      animation: starBlinkLight 2.5s infinite ease-in-out;
    }}
    @keyframes starBlinkLight {{
      0%, 100% {{ opacity: 0.3; transform: scale(0.8); }}
      50% {{ opacity: 1; transform: scale(1.3); }}
    }}
  </style>

  <g clip-path="url(#banner-light-clip)">
    <!-- Base Background -->
    <rect width="1280" height="740" class="bg-light"/>
    <rect width="1280" height="740" fill="none" stroke="#ff004d" stroke-opacity="0.3" stroke-width="4" rx="20"/>

    <!-- Ambient soft glow circle -->
    <circle cx="980" cy="370" r="280" fill="#ff004d" opacity="0.08"/>

    <!-- Floating Sparkles -->
    <g opacity="0.7">
      <circle cx="120" cy="100" r="2.5" fill="#ff004d" class="star-light" style="animation-delay: 0s;"/>
      <circle cx="550" cy="80" r="2" fill="#570000" class="star-light" style="animation-delay: 0.7s;"/>
      <circle cx="620" cy="220" r="3" fill="#ff004d" class="star-light" style="animation-delay: 1.4s;"/>
      <circle cx="1150" cy="140" r="2" fill="#570000" class="star-light" style="animation-delay: 0.3s;"/>
    </g>

    <!-- LEFT COLUMN CONTENT -->

    <!-- 1. Terminal Bar -->
    <rect x="55" y="45" width="580" height="42" rx="8" fill="#ffffff" stroke="#ff004d" stroke-opacity="0.4" stroke-width="1.5"/>
    <circle cx="75" cy="66" r="6" fill="#ff5f56"/>
    <circle cx="95" cy="66" r="6" fill="#ffbd2e"/>
    <circle cx="115" cy="66" r="6" fill="#27c93f"/>
    <text x="140" y="71" class="terminal-text-light">user@dev:~$ <tspan fill="#ff004d">cat README.md</tspan></text>
    <rect x="350" y="58" width="8" height="17" fill="#ff004d">
      <animate attributeName="opacity" values="1;0;1" dur="0.8s" repeatCount="indefinite"/>
    </rect>

    <!-- 2. Main Title Name -->
    <text x="55" y="145" class="title-light">Mr. Anonymous</text>

    <!-- 3. Cycling Role Subtitle -->
    <text x="58" y="182" font-family="'Outfit', sans-serif" font-weight="600" font-size="22" fill="#ff004d">
      <animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.1;0.9;1" dur="4s" repeatCount="indefinite"/>
      <tspan>⚡ </tspan>
      <animate attributeName="textContent" 
               values="Student / AI Engineer;LLM &amp; RAG Architecture Specialist;Autonomous AI Agent Developer;Full-Stack Innovator" 
               dur="16s" repeatCount="indefinite"/>
    </text>

    <!-- 4. Tagline Quote Card -->
    <rect x="55" y="210" width="580" height="48" rx="8" fill="#ffffff" stroke="#ff004d" stroke-opacity="0.3" stroke-width="1"/>
    <text x="75" y="240" font-family="'Fira Code', monospace" font-size="15" fill="#280000">
      <tspan fill="#ff004d">"</tspan>Think. Build. Ship. Repeat.<tspan fill="#ff004d">"</tspan>
    </text>

    <!-- 5. Tech Stack Pills -->
    <g transform="translate(55, 275)">
      <!-- Row 1 -->
      <g transform="translate(0,0)">
        <rect width="90" height="30" rx="15" fill="#ff004d"/>
        <text x="45" y="20" class="pill-text-light" text-anchor="middle">🐍 Python</text>
      </g>
      <g transform="translate(100,0)">
        <rect width="135" height="30" rx="15" fill="#280000"/>
        <text x="67" y="20" class="pill-text-light" text-anchor="middle">🤖 AI Engineering</text>
      </g>
      <g transform="translate(245,0)">
        <rect width="85" height="30" rx="15" fill="#ff004d"/>
        <text x="42" y="20" class="pill-text-light" text-anchor="middle">🧠 LLMs</text>
      </g>
      <g transform="translate(340,0)">
        <rect width="80" height="30" rx="15" fill="#570000"/>
        <text x="40" y="20" class="pill-text-light" text-anchor="middle">⚡ RAG</text>
      </g>
      <g transform="translate(430,0)">
        <rect width="95" height="30" rx="15" fill="#ff004d"/>
        <text x="47" y="20" class="pill-text-light" text-anchor="middle">🚀 FastAPI</text>
      </g>

      <!-- Row 2 -->
      <g transform="translate(0,40)">
        <rect width="115" height="30" rx="15" fill="#280000"/>
        <text x="57" y="20" class="pill-text-light" text-anchor="middle">📘 TypeScript</text>
      </g>
      <g transform="translate(125,40)">
        <rect width="95" height="30" rx="15" fill="#ff004d"/>
        <text x="47" y="20" class="pill-text-light" text-anchor="middle">▲ Next.js</text>
      </g>
      <g transform="translate(230,40)">
        <rect width="85" height="30" rx="15" fill="#570000"/>
        <text x="42" y="20" class="pill-text-light" text-anchor="middle">⚛️ React</text>
      </g>
      <g transform="translate(325,40)">
        <rect width="105" height="30" rx="15" fill="#280000"/>
        <text x="52" y="20" class="pill-text-light" text-anchor="middle">🐘 PostgreSQL</text>
      </g>
      <g transform="translate(440,40)">
        <rect width="85" height="30" rx="15" fill="#ff004d"/>
        <text x="42" y="20" class="pill-text-light" text-anchor="middle">🐳 Docker</text>
      </g>
    </g>

    <!-- 6. Code Editor Snippet Window -->
    <g transform="translate(55, 365)">
      <rect width="580" height="245" rx="10" fill="#ffffff" stroke="#ff004d" stroke-opacity="0.4" stroke-width="1.5"/>
      <rect width="580" height="30" rx="10" fill="#fff0f4"/>
      <text x="20" y="20" font-family="'Fira Code', monospace" font-size="12" fill="#570000">ai_agent_core.py</text>
      
      <g class="code-text-light" transform="translate(20, 55)">
        <text y="0"><tspan fill="#ff004d">class</tspan> <tspan fill="#280000">AIAgent</tspan>:</text>
        <text y="24">    <tspan fill="#ff004d">def</tspan> <tspan fill="#280000">__init__</tspan>(self, dev=<tspan fill="#ff004d">"Mr. Anonymous"</tspan>):</text>
        <text y="48">        self.role = <tspan fill="#ff004d">"Student &amp; AI Engineer"</tspan></text>
        <text y="72">        self.stack = [<tspan fill="#ff004d">"Python"</tspan>, <tspan fill="#ff004d">"RAG"</tspan>, <tspan fill="#ff004d">"FastAPI"</tspan>]</text>
        <text y="96">        self.focus = <tspan fill="#ff004d">"Autonomous AI Agents"</tspan></text>
        <text y="120">    <tspan fill="#ff004d">async def</tspan> <tspan fill="#280000">ship_innovation</tspan>(self):</text>
        <text y="144">        <tspan fill="#ff004d">return</tspan> <tspan fill="#280000">await</tspan> self.build_future()</text>
      </g>
    </g>

    <!-- 7. Neon Sign -->
    <g transform="translate(55, 640)">
      <rect width="580" height="52" rx="8" fill="#ffffff" stroke="#ff004d" stroke-width="1.5"/>
      <text x="290" y="32" class="neon-text-light" text-anchor="middle">⚡ KEEP CODING • KEEP GROWING ⚡</text>
    </g>

    <!-- RIGHT COLUMN: Character Image & Hologram Scanner -->
    <g transform="translate(690, 20)">
      <image href="data:image/png;base64,{B64_CHAR}" width="540" height="710" x="0" y="0"/>
      <rect x="0" y="0" width="540" height="25" fill="url(#scan-light-grad)">
        <animate attributeName="y" values="0;680;0" dur="3.8s" repeatCount="indefinite"/>
      </rect>
    </g>
  </g>
</svg>'''

with open(os.path.join(TARGET_DIR, "banner-light.svg"), "w", encoding="utf-8") as f:
    f.write(banner_light_svg)

print("Created banner-light.svg")


# --- 3. lanyard.svg (Swinging ID Badge) ---
lanyard_svg = f'''<svg viewBox="0 0 340 480" width="340" height="480" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="strap-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ff004d"/>
      <stop offset="50%" stop-color="#d90445"/>
      <stop offset="100%" stop-color="#ff004d"/>
    </linearGradient>

    <linearGradient id="metal-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#e0e0e0"/>
      <stop offset="50%" stop-color="#888888"/>
      <stop offset="100%" stop-color="#ffffff"/>
    </linearGradient>

    <linearGradient id="card-bg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#18040b"/>
      <stop offset="50%" stop-color="#100207"/>
      <stop offset="100%" stop-color="#000000"/>
    </linearGradient>

    <linearGradient id="shine-sweep" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0"/>
      <stop offset="45%" stop-color="#ffffff" stop-opacity="0"/>
      <stop offset="50%" stop-color="#ffffff" stop-opacity="0.35"/>
      <stop offset="55%" stop-color="#ffffff" stop-opacity="0"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>
    </linearGradient>

    <filter id="badge-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="5" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>

    <clipPath id="avatar-clip">
      <circle cx="170" cy="205" r="46"/>
    </clipPath>
  </defs>

  <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;800&amp;family=Fira+Code:wght@400;600&amp;display=swap');

    .card-title {{ font-family: 'Outfit', sans-serif; font-weight: 800; font-size: 20px; fill: #fdffff; }}
    .card-role {{ font-family: 'Outfit', sans-serif; font-weight: 600; font-size: 13px; fill: #ff004d; letter-spacing: 1px; }}
    .card-handle {{ font-family: 'Fira Code', monospace; font-size: 12px; fill: #a0a0a0; }}
    .card-badge {{ font-family: 'Outfit', sans-serif; font-weight: 600; font-size: 10px; fill: #fdffff; }}
  </style>

  <!-- SWINGING WRAPPER WITH DAMPED PENDULUM PHYSICS -->
  <g transform-origin="170 0">
    <animateTransform attributeName="transform" type="rotate"
                      values="-3.5; 3.5; -3.5"
                      dur="5.5s" repeatCount="indefinite"
                      calcMode="spline" keySplines="0.4 0 0.6 1; 0.4 0 0.6 1"/>

    <!-- Lanyard Strap -->
    <path d="M150 0 L150 70 L190 70 L190 0 Z" fill="url(#strap-grad)"/>
    <text x="170" y="45" font-family="'Outfit', sans-serif" font-weight="800" font-size="11" fill="#fdffff" text-anchor="middle" transform="rotate(-90 170 45)" letter-spacing="2">STUDENT // AI ENGINEER</text>

    <!-- Metal Buckle Ring -->
    <rect x="154" y="66" width="32" height="12" rx="3" fill="url(#metal-grad)"/>
    <circle cx="170" cy="85" r="10" fill="none" stroke="url(#metal-grad)" stroke-width="4"/>

    <!-- Main Glass ID Badge -->
    <g transform="translate(45, 95)">
      <!-- Base Card Container -->
      <rect width="250" height="365" rx="16" fill="url(#card-bg)"/>
      <rect width="250" height="365" rx="16" fill="none" stroke="#ff004d" stroke-width="2" filter="url(#badge-glow)"/>

      <!-- Header Banner -->
      <path d="M0 16 Q0 0 16 0 L234 0 Q250 0 250 16 L250 45 L0 45 Z" fill="#280000"/>
      <text x="125" y="28" font-family="'Outfit', sans-serif" font-weight="800" font-size="12" fill="#ff004d" text-anchor="middle" letter-spacing="2">DEV PASSPORT • VERIFIED</text>

      <!-- Avatar Outer Ring -->
      <circle cx="125" cy="110" r="52" fill="none" stroke="#ff004d" stroke-width="3" filter="url(#badge-glow)"/>
      
      <!-- Cropped Avatar Image -->
      <g transform="translate(-45, -95)">
        <image href="data:image/png;base64,{B64_AVATAR}" width="96" height="96" x="122" y="157" clip-path="url(#avatar-clip)"/>
      </g>

      <!-- Name & Title -->
      <text x="125" y="195" class="card-title" text-anchor="middle">Mr. Anonymous</text>
      <text x="125" y="215" class="card-role" text-anchor="middle">STUDENT / AI ENGINEER</text>
      <text x="125" y="233" class="card-handle" text-anchor="middle">@Mr-Anonymous-Guy</text>

      <!-- Skill Pills -->
      <g transform="translate(25, 252)">
        <rect x="0" y="0" width="60" height="20" rx="10" fill="#570000"/>
        <text x="30" y="14" class="card-badge" text-anchor="middle">PYTHON</text>

        <rect x="68" y="0" width="64" height="20" rx="10" fill="#ff004d"/>
        <text x="100" y="14" class="card-badge" text-anchor="middle">AI AGENTS</text>

        <rect x="140" y="0" width="60" height="20" rx="10" fill="#570000"/>
        <text x="170" y="14" class="card-badge" text-anchor="middle">FASTAPI</text>
      </g>

      <!-- Barcode Section -->
      <g transform="translate(35, 292)">
        <!-- Barcode lines -->
        <rect x="0" y="0" width="3" height="30" fill="#fdffff"/>
        <rect x="5" y="0" width="1.5" height="30" fill="#fdffff"/>
        <rect x="9" y="0" width="4" height="30" fill="#fdffff"/>
        <rect x="16" y="0" width="2" height="30" fill="#fdffff"/>
        <rect x="21" y="0" width="5" height="30" fill="#fdffff"/>
        <rect x="29" y="0" width="1.5" height="30" fill="#fdffff"/>
        <rect x="33" y="0" width="3" height="30" fill="#fdffff"/>
        <rect x="39" y="0" width="6" height="30" fill="#fdffff"/>
        <rect x="48" y="0" width="2" height="30" fill="#fdffff"/>
        <rect x="53" y="0" width="4" height="30" fill="#fdffff"/>
        <rect x="60" y="0" width="1.5" height="30" fill="#fdffff"/>
        <rect x="64" y="0" width="5" height="30" fill="#fdffff"/>
        <rect x="72" y="0" width="3" height="30" fill="#fdffff"/>
        <rect x="78" y="0" width="2" height="30" fill="#fdffff"/>
        <rect x="83" y="0" width="6" height="30" fill="#fdffff"/>
        <rect x="92" y="0" width="1.5" height="30" fill="#fdffff"/>
        <rect x="96" y="0" width="4" height="30" fill="#fdffff"/>
        <rect x="103" y="0" width="2" height="30" fill="#fdffff"/>
        <rect x="108" y="0" width="5" height="30" fill="#fdffff"/>
        <rect x="116" y="0" width="3" height="30" fill="#fdffff"/>
        <rect x="122" y="0" width="1.5" height="30" fill="#fdffff"/>
        <rect x="126" y="0" width="4" height="30" fill="#fdffff"/>
        <rect x="133" y="0" width="2" height="30" fill="#fdffff"/>
        <rect x="138" y="0" width="6" height="30" fill="#fdffff"/>
        <rect x="147" y="0" width="3" height="30" fill="#fdffff"/>
        <rect x="153" y="0" width="1.5" height="30" fill="#fdffff"/>
        <rect x="157" y="0" width="4" height="30" fill="#fdffff"/>
        <rect x="164" y="0" width="2" height="30" fill="#fdffff"/>
        <rect x="169" y="0" width="5" height="30" fill="#fdffff"/>
        <rect x="177" y="0" width="3" height="30" fill="#fdffff"/>

        <text x="90" y="44" font-family="'Fira Code', monospace" font-size="10" fill="#ff004d" text-anchor="middle" letter-spacing="2">ID: 071105-AI-ENGINEER</text>
      </g>

      <!-- Holographic Shine Sweep Overlay -->
      <rect width="250" height="365" rx="16" fill="url(#shine-sweep)" pointer-events="none">
        <animateTransform attributeName="transform" type="translate" values="-250 -365; 250 365" dur="4s" repeatCount="indefinite"/>
      </rect>
    </g>
  </g>
</svg>'''

with open(os.path.join(TARGET_DIR, "lanyard.svg"), "w", encoding="utf-8") as f:
    f.write(lanyard_svg)

print("Created lanyard.svg")


# --- 4. stats.svg (Local Animated GitHub Stats) ---
stats_svg = '''<svg viewBox="0 0 450 195" width="450" height="195" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="card-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#18040b"/>
      <stop offset="100%" stop-color="#0a0104"/>
    </linearGradient>
    <filter id="stat-glow">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@600;800&amp;family=Fira+Code:wght@600&amp;display=swap');
    .stat-title {{ font-family: 'Outfit', sans-serif; font-weight: 800; font-size: 17px; fill: #fdffff; }}
    .stat-label {{ font-family: 'Outfit', sans-serif; font-weight: 600; font-size: 13px; fill: #a0a0a0; }}
    .stat-val {{ font-family: 'Fira Code', monospace; font-weight: 600; font-size: 14px; fill: #fdffff; }}
    .rank-text {{ font-family: 'Outfit', sans-serif; font-weight: 800; font-size: 24px; fill: #ff004d; }}
  </style>

  <rect width="450" height="195" rx="14" fill="url(#card-grad)" stroke="#ff004d" stroke-opacity="0.5" stroke-width="1.5"/>

  <!-- Card Header -->
  <g transform="translate(25, 32)">
    <text class="stat-title">⚡ Mr. Anonymous's GitHub Stats</text>
  </g>

  <!-- Left: S Rank Circular Ring -->
  <g transform="translate(75, 115)">
    <circle r="42" fill="none" stroke="#280000" stroke-width="8"/>
    <circle r="42" fill="none" stroke="#ff004d" stroke-width="8" stroke-dasharray="264" stroke-dashoffset="40" filter="url(#stat-glow)">
      <animate attributeName="stroke-dashoffset" values="264;40" dur="1.5s" ease="ease-out"/>
    </circle>
    <text class="rank-text" text-anchor="middle" dy="8" filter="url(#stat-glow)">S Rank</text>
  </g>

  <!-- Right: Stat Rows -->
  <g transform="translate(170, 60)">
    <!-- Row 1: Commits -->
    <g transform="translate(0, 0)">
      <text class="stat-label">Total Commits</text>
      <text x="240" class="stat-val" text-anchor="end">485+</text>
      <rect y="10" width="240" height="6" rx="3" fill="#280000"/>
      <rect y="10" width="210" height="6" rx="3" fill="#ff004d">
        <animate attributeName="width" values="0;210" dur="1.2s" ease="ease-out"/>
      </rect>
    </g>

    <!-- Row 2: Pull Requests -->
    <g transform="translate(0, 30)">
      <text class="stat-label">Pull Requests</text>
      <text x="240" class="stat-val" text-anchor="end">65+</text>
      <rect y="10" width="240" height="6" rx="3" fill="#280000"/>
      <rect y="10" width="180" height="6" rx="3" fill="#ff004d">
        <animate attributeName="width" values="0;180" dur="1.4s" ease="ease-out"/>
      </rect>
    </g>

    <!-- Row 3: Total Stars -->
    <g transform="translate(0, 60)">
      <text class="stat-label">Total Stars Earned</text>
      <text x="240" class="stat-val" text-anchor="end">120+</text>
      <rect y="10" width="240" height="6" rx="3" fill="#280000"/>
      <rect y="10" width="195" height="6" rx="3" fill="#ff004d">
        <animate attributeName="width" values="0;195" dur="1.6s" ease="ease-out"/>
      </rect>
    </g>

    <!-- Row 4: Contributed Repos -->
    <g transform="translate(0, 90)">
      <text class="stat-label">Contributed Repos</text>
      <text x="240" class="stat-val" text-anchor="end">28</text>
      <rect y="10" width="240" height="6" rx="3" fill="#280000"/>
      <rect y="10" width="165" height="6" rx="3" fill="#ff004d">
        <animate attributeName="width" values="0;165" dur="1.8s" ease="ease-out"/>
      </rect>
    </g>
  </g>
</svg>'''

with open(os.path.join(TARGET_DIR, "stats.svg"), "w", encoding="utf-8") as f:
    f.write(stats_svg)

print("Created stats.svg")


# --- 5. langs.svg (Local Animated Top Languages) ---
langs_svg = '''<svg viewBox="0 0 450 195" width="450" height="195" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="card-grad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#18040b"/>
      <stop offset="100%" stop-color="#0a0104"/>
    </linearGradient>
  </defs>

  <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@600;800&amp;family=Fira+Code:wght@600&amp;display=swap');
    .lang-title {{ font-family: 'Outfit', sans-serif; font-weight: 800; font-size: 17px; fill: #fdffff; }}
    .lang-name {{ font-family: 'Outfit', sans-serif; font-weight: 600; font-size: 13px; fill: #fdffff; }}
    .lang-pct {{ font-family: 'Fira Code', monospace; font-size: 12px; fill: #ff004d; }}
  </style>

  <rect width="450" height="195" rx="14" fill="url(#card-grad2)" stroke="#ff004d" stroke-opacity="0.5" stroke-width="1.5"/>

  <!-- Card Header -->
  <g transform="translate(25, 32)">
    <text class="lang-title">🔥 Most Used Languages</text>
  </g>

  <g transform="translate(25, 55)">
    <!-- Language 1: Python -->
    <g transform="translate(0, 0)">
      <text class="lang-name">Python (AI / FastAPI / RAG)</text>
      <text x="400" class="lang-pct" text-anchor="end">42%</text>
      <rect y="10" width="400" height="8" rx="4" fill="#280000"/>
      <rect y="10" width="168" height="8" rx="4" fill="#ff004d">
        <animate attributeName="width" values="0;168" dur="1.2s" ease="ease-out"/>
      </rect>
    </g>

    <!-- Language 2: TypeScript / Next.js -->
    <g transform="translate(0, 26)">
      <text class="lang-name">TypeScript / Next.js / React</text>
      <text x="400" class="lang-pct" text-anchor="end">30%</text>
      <rect y="10" width="400" height="8" rx="4" fill="#280000"/>
      <rect y="10" width="120" height="8" rx="4" fill="#d90445">
        <animate attributeName="width" values="0;120" dur="1.4s" ease="ease-out"/>
      </rect>
    </g>

    <!-- Language 3: HTML5 / CSS3 / Framer -->
    <g transform="translate(0, 52)">
      <text class="lang-name">HTML5 / CSS3 / Tailwind / Framer</text>
      <text x="400" class="lang-pct" text-anchor="end">15%</text>
      <rect y="10" width="400" height="8" rx="4" fill="#280000"/>
      <rect y="10" width="60" height="8" rx="4" fill="#8b002e">
        <animate attributeName="width" values="0;60" dur="1.6s" ease="ease-out"/>
      </rect>
    </g>

    <!-- Language 4: SQL & PostgreSQL -->
    <g transform="translate(0, 78)">
      <text class="lang-name">SQL / PostgreSQL / Supabase</text>
      <text x="400" class="lang-pct" text-anchor="end">8%</text>
      <rect y="10" width="400" height="8" rx="4" fill="#280000"/>
      <rect y="10" width="32" height="8" rx="4" fill="#570000">
        <animate attributeName="width" values="0;32" dur="1.8s" ease="ease-out"/>
      </rect>
    </g>

    <!-- Language 5: Docker & Shell -->
    <g transform="translate(0, 104)">
      <text class="lang-name">Docker / Bash / Git</text>
      <text x="400" class="lang-pct" text-anchor="end">5%</text>
      <rect y="10" width="400" height="8" rx="4" fill="#280000"/>
      <rect y="10" width="20" height="8" rx="4" fill="#fdffff">
        <animate attributeName="width" values="0;20" dur="2.0s" ease="ease-out"/>
      </rect>
    </g>
  </g>
</svg>'''

with open(os.path.join(TARGET_DIR, "langs.svg"), "w", encoding="utf-8") as f:
    f.write(langs_svg)

print("Created langs.svg")


# --- 6. trophies.svg (Local Animated Trophies) ---
trophies_svg = '''<svg viewBox="0 0 880 150" width="880" height="150" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="trophy-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1c040d"/>
      <stop offset="100%" stop-color="#0a0104"/>
    </linearGradient>
    <filter id="trophy-glow">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@700;800&amp;display=swap');
    .trophy-title {{ font-family: 'Outfit', sans-serif; font-weight: 800; font-size: 14px; fill: #fdffff; }}
    .trophy-rank {{ font-family: 'Outfit', sans-serif; font-weight: 800; font-size: 13px; fill: #ff004d; }}
    .trophy-desc {{ font-family: 'Outfit', sans-serif; font-weight: 600; font-size: 11px; fill: #a0a0a0; }}
  </style>

  <g transform="translate(0, 0)">
    <!-- Trophy 1 -->
    <g transform="translate(10, 10)">
      <rect width="200" height="130" rx="12" fill="url(#trophy-bg)" stroke="#ff004d" stroke-width="1.5"/>
      <text x="100" y="38" font-size="28" text-anchor="middle">🤖</text>
      <text x="100" y="70" class="trophy-title" text-anchor="middle">AI ARCHITECT</text>
      <text x="100" y="90" class="trophy-rank" text-anchor="middle" filter="url(#trophy-glow)">RANK S</text>
      <text x="100" y="110" class="trophy-desc" text-anchor="middle">RAG &amp; AI Agents Expert</text>
    </g>

    <!-- Trophy 2 -->
    <g transform="translate(225, 10)">
      <rect width="200" height="130" rx="12" fill="url(#trophy-bg)" stroke="#ff004d" stroke-width="1.5"/>
      <text x="100" y="38" font-size="28" text-anchor="middle">⚡</text>
      <text x="100" y="70" class="trophy-title" text-anchor="middle">FASTAPI BUILDER</text>
      <text x="100" y="90" class="trophy-rank" text-anchor="middle" filter="url(#trophy-glow)">RANK S</text>
      <text x="100" y="110" class="trophy-desc" text-anchor="middle">High Performance APIs</text>
    </g>

    <!-- Trophy 3 -->
    <g transform="translate(440, 10)">
      <rect width="200" height="130" rx="12" fill="url(#trophy-bg)" stroke="#ff004d" stroke-width="1.5"/>
      <text x="100" y="38" font-size="28" text-anchor="middle">🚀</text>
      <text x="100" y="70" class="trophy-title" text-anchor="middle">FULL-STACK INNOVATOR</text>
      <text x="100" y="90" class="trophy-rank" text-anchor="middle" filter="url(#trophy-glow)">RANK A+</text>
      <text x="100" y="110" class="trophy-desc" text-anchor="middle">Next.js &amp; React Specialist</text>
    </g>

    <!-- Trophy 4 -->
    <g transform="translate(655, 10)">
      <rect width="200" height="130" rx="12" fill="url(#trophy-bg)" stroke="#ff004d" stroke-width="1.5"/>
      <text x="100" y="38" font-size="28" text-anchor="middle">⭐</text>
      <text x="100" y="70" class="trophy-title" text-anchor="middle">REPO CREATOR</text>
      <text x="100" y="90" class="trophy-rank" text-anchor="middle" filter="url(#trophy-glow)">RANK A+</text>
      <text x="100" y="110" class="trophy-desc" text-anchor="middle">Open Source Pioneer</text>
    </g>
  </g>
</svg>'''

with open(os.path.join(TARGET_DIR, "trophies.svg"), "w", encoding="utf-8") as f:
    f.write(trophies_svg)

print("Created trophies.svg")


# --- 7. README.md ---
readme_md = '''<div align="center">

<!-- ✨ Animated Hero Banner (Dark / Light Auto-Switch) ✨ -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./banner.svg?v=1">
  <source media="(prefers-color-scheme: light)" srcset="./banner-light.svg?v=1">
  <img src="./banner.svg?v=1" alt="Mr. Anonymous — Student & AI Engineer" width="100%"/>
</picture>

</div>

<br/>

<table align="center" border="0">
<tr>
<td width="36%" align="center" valign="middle">

<!-- 🪪 Swinging Lanyard ID Card (React Bits style, pure SVG) -->
<img src="./lanyard.svg?v=1" alt="Mr. Anonymous ID badge" width="330"/>

</td>
<td width="64%" valign="middle">

### 🤖 Featured AI & Full-Stack Projects

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

### 📊 GitHub Stats & Top Languages

<img src="./stats.svg?v=1" alt="GitHub Stats" height="185"/>
<img src="./langs.svg?v=1" alt="Top Languages" height="185"/>

<br/><br/>

### 🛩️ Real-Time Jet Contribution Heatmap

![GitHub jet heatmap](https://raw.githubusercontent.com/Mr-Anonymous-Guy/Mr-Anonymous-Guy/main/dist/github-jet.svg)

<br/><br/>

### 🏆 Developer Achievements & Trophies

<img src="./trophies.svg?v=1" alt="Developer Trophies" width="95%"/>

<br/><br/>

### 📫 Let's Connect & Collaborate

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

print("Created README.md")
print("All assets generated successfully!")
