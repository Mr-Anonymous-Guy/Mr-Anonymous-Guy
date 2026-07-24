import os
import base64
from PIL import Image
import io

TARGET_DIR = r"c:\Mr-Anonymous-Guy\Mr-Anonymous-Guy\Mr-Anonymous-Guy"

# Load cropped avatar base64
with open(os.path.join(TARGET_DIR, "scratch", "b64_avatar.txt"), "r") as f:
    B64_AVATAR = f.read().strip()

print("B64 Avatar length:", len(B64_AVATAR))


# ==========================================
# 1. trophies.svg (ViewBox 0 0 1092 168)
# ==========================================
trophies_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1092 168" width="1092" height="168" role="img" aria-label="GitHub trophies">
<defs><style><![CDATA[
text{font-family:'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace}
@keyframes popCell{0%{opacity:0;transform:translateY(16px) scale(.85)}70%{opacity:1;transform:translateY(-3px) scale(1.03)}100%{opacity:1;transform:translateY(0) scale(1)}}
@keyframes rankGlow{0%,100%{opacity:.75}50%{opacity:1}}
@keyframes shineX2{0%{transform:translateX(-200px) skewX(-15deg)}60%,100%{transform:translateX(1172px) skewX(-15deg)}}
.cell{opacity:0;animation:popCell .55s cubic-bezier(.2,.8,.3,1.2) forwards;transform-box:fill-box;transform-origin:center}
.rk{animation:rankGlow 2.2s ease-in-out infinite}
.sh2{animation:shineX2 5s ease-in-out 2s infinite}
]]></style>
<linearGradient id="shg2" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#fff" stop-opacity="0"/><stop offset="50%" stop-color="#fff" stop-opacity=".12"/><stop offset="100%" stop-color="#fff" stop-opacity="0"/></linearGradient>
<clipPath id="tc"><rect x="0" y="0" width="1092" height="168" rx="14"/></clipPath>
</defs>

  <!-- Cell 1: AI Architect -->
  <g class="cell" style="animation-delay:0.30s">
    <rect x="12" y="12" width="168" height="144" rx="14" fill="#170e28" stroke="#ff004d" stroke-opacity=".75" stroke-width="1.5"/>
    <text x="96.0" y="52" text-anchor="middle" font-size="30">🤖</text>
    <text class="rk" x="164" y="40" text-anchor="end" font-size="24" font-weight="bold" fill="#ff004d" style="animation-delay:0.70s">SSS</text>
    <text x="96.0" y="90" text-anchor="middle" font-size="14" font-weight="bold" fill="#fdffff">AI Architect</text>
    <text x="96.0" y="112" text-anchor="middle" font-size="11" fill="#fdffff" opacity="0.85">RAG &amp; AI Agents</text>
    <rect x="30" y="124" width="132" height="5" rx="2.5" fill="#280000"/>
    <rect x="30" y="124" width="0" height="5" rx="2.5" fill="#ff004d">
      <animate attributeName="width" from="0" to="132" dur="1s" begin="0.60s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>

  <!-- Cell 2: FastAPI Builder -->
  <g class="cell" style="animation-delay:0.48s">
    <rect x="192" y="12" width="168" height="144" rx="14" fill="#170e28" stroke="#ff004d" stroke-opacity=".75" stroke-width="1.5"/>
    <text x="276.0" y="52" text-anchor="middle" font-size="30">⚡</text>
    <text class="rk" x="344" y="40" text-anchor="end" font-size="30" font-weight="bold" fill="#ff004d" style="animation-delay:0.88s">S</text>
    <text x="276.0" y="90" text-anchor="middle" font-size="14" font-weight="bold" fill="#fdffff">FastAPI Builder</text>
    <text x="276.0" y="112" text-anchor="middle" font-size="11" fill="#fdffff" opacity="0.85">High Perf APIs</text>
    <rect x="210" y="124" width="132" height="5" rx="2.5" fill="#280000"/>
    <rect x="210" y="124" width="0" height="5" rx="2.5" fill="#ff004d">
      <animate attributeName="width" from="0" to="132" dur="1s" begin="0.78s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>

  <!-- Cell 3: Full-Stack Dev -->
  <g class="cell" style="animation-delay:0.66s">
    <rect x="372" y="12" width="168" height="144" rx="14" fill="#170e28" stroke="#ff004d" stroke-opacity=".75" stroke-width="1.5"/>
    <text x="456.0" y="52" text-anchor="middle" font-size="30">🚀</text>
    <text class="rk" x="524" y="40" text-anchor="end" font-size="30" font-weight="bold" fill="#ff004d" style="animation-delay:1.06s">A+</text>
    <text x="456.0" y="90" text-anchor="middle" font-size="14" font-weight="bold" fill="#fdffff">Full-Stack Dev</text>
    <text x="456.0" y="112" text-anchor="middle" font-size="11" fill="#fdffff" opacity="0.85">Next.js &amp; React</text>
    <rect x="390" y="124" width="132" height="5" rx="2.5" fill="#280000"/>
    <rect x="390" y="124" width="0" height="5" rx="2.5" fill="#ff004d">
      <animate attributeName="width" from="0" to="132" dur="1s" begin="0.96s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>

  <!-- Cell 4: LLM Specialist -->
  <g class="cell" style="animation-delay:0.84s">
    <rect x="552" y="12" width="168" height="144" rx="14" fill="#170e28" stroke="#ff004d" stroke-opacity=".75" stroke-width="1.5"/>
    <text x="636.0" y="52" text-anchor="middle" font-size="30">🧠</text>
    <text class="rk" x="704" y="40" text-anchor="end" font-size="30" font-weight="bold" fill="#ff004d" style="animation-delay:1.24s">A+</text>
    <text x="636.0" y="90" text-anchor="middle" font-size="14" font-weight="bold" fill="#fdffff">LLM Specialist</text>
    <text x="636.0" y="112" text-anchor="middle" font-size="11" fill="#fdffff" opacity="0.85">Prompt &amp; Chains</text>
    <rect x="570" y="124" width="132" height="5" rx="2.5" fill="#280000"/>
    <rect x="570" y="124" width="0" height="5" rx="2.5" fill="#ff004d">
      <animate attributeName="width" from="0" to="132" dur="1s" begin="1.14s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>

  <!-- Cell 5: Committer -->
  <g class="cell" style="animation-delay:1.02s">
    <rect x="732" y="12" width="168" height="144" rx="14" fill="#170e28" stroke="#ff004d" stroke-opacity=".75" stroke-width="1.5"/>
    <text x="816.0" y="52" text-anchor="middle" font-size="30">💻</text>
    <text class="rk" x="884" y="40" text-anchor="end" font-size="30" font-weight="bold" fill="#ff004d" style="animation-delay:1.42s">A</text>
    <text x="816.0" y="90" text-anchor="middle" font-size="14" font-weight="bold" fill="#fdffff">Committer</text>
    <text x="816.0" y="112" text-anchor="middle" font-size="11" fill="#fdffff" opacity="0.85">Commits 500+</text>
    <rect x="750" y="124" width="132" height="5" rx="2.5" fill="#280000"/>
    <rect x="750" y="124" width="0" height="5" rx="2.5" fill="#ff004d">
      <animate attributeName="width" from="0" to="132" dur="1s" begin="1.32s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>

  <!-- Cell 6: Repo Creator -->
  <g class="cell" style="animation-delay:1.20s">
    <rect x="912" y="12" width="168" height="144" rx="14" fill="#170e28" stroke="#ff004d" stroke-opacity=".75" stroke-width="1.5"/>
    <text x="996.0" y="52" text-anchor="middle" font-size="30">⭐</text>
    <text class="rk" x="1064" y="40" text-anchor="end" font-size="30" font-weight="bold" fill="#ff004d" style="animation-delay:1.60s">A</text>
    <text x="996.0" y="90" text-anchor="middle" font-size="14" font-weight="bold" fill="#fdffff">Repo Creator</text>
    <text x="996.0" y="112" text-anchor="middle" font-size="11" fill="#fdffff" opacity="0.85">Repos 28+</text>
    <rect x="930" y="124" width="132" height="5" rx="2.5" fill="#280000"/>
    <rect x="930" y="124" width="0" height="5" rx="2.5" fill="#ff004d">
      <animate attributeName="width" from="0" to="132" dur="1s" begin="1.50s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>

<g clip-path="url(#tc)"><rect class="sh2" x="0" y="0" width="140" height="168" fill="url(#shg2)"/></g>
</svg>'''

with open(os.path.join(TARGET_DIR, "trophies.svg"), "w", encoding="utf-8") as f:
    f.write(trophies_svg)

print("Created trophies.svg")


# ==========================================
# 2. stats.svg (ViewBox 0 0 500 232)
# ==========================================
stats_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 232" width="500" height="232" role="img" aria-label="Mr. Anonymous GitHub stats">
<defs><style><![CDATA[
text{font-family:'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace}
@keyframes fadeSlide{from{opacity:0;transform:translateX(-14px)}to{opacity:1;transform:translateX(0)}}
@keyframes fadeIn{from{opacity:0}to{opacity:1}}
@keyframes rankPulse{0%,100%{opacity:.85}50%{opacity:1}}
@keyframes shineX{0%{transform:translateX(-160px) skewX(-15deg)}60%,100%{transform:translateX(560px) skewX(-15deg)}}
.row{opacity:0;animation:fadeSlide .5s ease forwards}
.rk{animation:rankPulse 2.4s ease-in-out infinite}
.sh{animation:shineX 4.5s ease-in-out 2.4s infinite}
]]></style>
<linearGradient id="tg" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%"><animate attributeName="stop-color" values="#ff004d;#fdffff;#ff004d" dur="6s" repeatCount="indefinite"/></stop>
  <stop offset="100%"><animate attributeName="stop-color" values="#fdffff;#ff004d;#fdffff" dur="6s" repeatCount="indefinite"/></stop>
</linearGradient>
<linearGradient id="ringg" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#ff004d"/><stop offset="100%" stop-color="#fdffff"/>
</linearGradient>
<linearGradient id="shg" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#fff" stop-opacity="0"/><stop offset="50%" stop-color="#fff" stop-opacity=".1"/><stop offset="100%" stop-color="#fff" stop-opacity="0"/></linearGradient>
<clipPath id="cc"><rect x="1" y="1" width="498" height="230" rx="14"/></clipPath>
<filter id="g"><feGaussianBlur stdDeviation="2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<rect x="1" y="1" width="498" height="230" rx="14" fill="#170e28" stroke="url(#tg)" stroke-width="1.5"/>
<text x="24" y="38" font-size="16" font-weight="bold" fill="#fdffff">⚡ Mr. Anonymous's GitHub Stats</text>

  <g class="row" style="animation-delay:0.50s">
    <text x="24" y="74" font-size="14">⭐</text>
    <text x="52" y="74" font-size="13.5" fill="#fdffff">Total Stars Earned:</text>
    <text x="316" y="74" text-anchor="end" font-size="14" font-weight="bold" fill="#fdffff">120+</text>
  </g>
  <g class="row" style="animation-delay:0.72s">
    <text x="24" y="105" font-size="14">💻</text>
    <text x="52" y="105" font-size="13.5" fill="#fdffff">Total Commits:</text>
    <text x="316" y="105" text-anchor="end" font-size="14" font-weight="bold" fill="#fdffff">500+</text>
  </g>
  <g class="row" style="animation-delay:0.94s">
    <text x="24" y="136" font-size="14">📦</text>
    <text x="52" y="136" font-size="13.5" fill="#fdffff">Public Repos:</text>
    <text x="316" y="136" text-anchor="end" font-size="14" font-weight="bold" fill="#fdffff">28</text>
  </g>
  <g class="row" style="animation-delay:1.16s">
    <text x="24" y="167" font-size="14">👥</text>
    <text x="52" y="167" font-size="13.5" fill="#fdffff">Pull Requests:</text>
    <text x="316" y="167" text-anchor="end" font-size="14" font-weight="bold" fill="#fdffff">65+</text>
  </g>
  <g class="row" style="animation-delay:1.38s">
    <text x="24" y="198" font-size="14">🤖</text>
    <text x="52" y="198" font-size="13.5" fill="#fdffff">AI Projects Built:</text>
    <text x="316" y="198" text-anchor="end" font-size="14" font-weight="bold" fill="#ff004d">12</text>
  </g>

<!-- Rank ring -->
<g transform="translate(408,138)">
  <circle r="52" fill="none" stroke="#241740" stroke-width="9"/>
  <circle r="52" fill="none" stroke="url(#ringg)" stroke-width="9" stroke-linecap="round"
    stroke-dasharray="254.8 326.7" stroke-dashoffset="254.8" transform="rotate(-90)">
    <animate attributeName="stroke-dashoffset" from="254.8" to="0" dur="1.6s" begin=".6s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
  </circle>
  <text class="rk" y="14" text-anchor="middle" font-size="40" font-weight="bold" fill="#ff004d" filter="url(#g)">S</text>
  <text y="76" text-anchor="middle" font-size="10.5" fill="#fdffff" opacity="0.9" style="animation:fadeIn .5s ease 1.8s forwards">RANK</text>
</g>

<g clip-path="url(#cc)"><rect class="sh" x="0" y="0" width="120" height="232" fill="url(#shg)"/></g>
</svg>'''

with open(os.path.join(TARGET_DIR, "stats.svg"), "w", encoding="utf-8") as f:
    f.write(stats_svg)

print("Created stats.svg")


# ==========================================
# 3. langs.svg (ViewBox 0 0 420 282)
# ==========================================
langs_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 282" width="420" height="282" role="img" aria-label="Top languages">
<defs><style><![CDATA[
text{font-family:'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace}
@keyframes fadeUp{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}
@keyframes shineX{0%{transform:translateX(-140px)}60%,100%{transform:translateX(460px)}}
.row{opacity:0;animation:fadeUp .5s ease forwards}
.sh{animation:shineX 4s ease-in-out 2.2s infinite}
]]></style>
<linearGradient id="tg" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%"><animate attributeName="stop-color" values="#ff004d;#fdffff;#ff004d" dur="6s" repeatCount="indefinite"/></stop>
  <stop offset="100%"><animate attributeName="stop-color" values="#fdffff;#ff004d;#fdffff" dur="6s" repeatCount="indefinite"/></stop>
</linearGradient>
<linearGradient id="shg" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#fff" stop-opacity="0"/><stop offset="50%" stop-color="#fff" stop-opacity=".1"/><stop offset="100%" stop-color="#fff" stop-opacity="0"/></linearGradient>
<clipPath id="cardc"><rect x="1" y="1" width="418" height="280" rx="14"/></clipPath>
<clipPath id="stackc"><rect x="20" y="58" width="0" height="11" rx="5.5"><animate attributeName="width" from="0" to="380" dur="1.4s" begin=".4s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/></rect></clipPath>
</defs>
<rect x="1" y="1" width="418" height="280" rx="14" fill="#170e28" stroke="url(#tg)" stroke-width="1.5"/>
<text x="20" y="34" font-size="16" font-weight="bold" fill="#fdffff">📊 Top Languages</text>
<g clip-path="url(#stackc)"><rect x="20.0" y="58" width="159.6" height="11" fill="#ff004d"/><rect x="179.6" y="58" width="114.0" height="11" fill="#e81c5f"/><rect x="293.6" y="58" width="57.0" height="11" fill="#c70039"/><rect x="350.6" y="58" width="30.4" height="11" fill="#900028"/><rect x="381.0" y="58" width="19.0" height="11" fill="#fdffff"/></g>

  <g class="row" style="animation-delay:0.90s">
    <circle cx="26" cy="91" r="5" fill="#ff004d"/>
    <text x="40" y="96" font-size="13" fill="#fdffff" font-weight="bold">Python (AI / FastAPI)</text>
    <text x="396" y="96" text-anchor="end" font-size="13" fill="#fdffff" font-weight="bold">42.0%</text>
    <rect x="40" y="104" width="268" height="9" rx="4.5" fill="#241740"/>
    <rect class="bar" x="40" y="104" width="168" height="9" rx="4.5" fill="#ff004d" style="animation-delay:1.05s">
      <animate attributeName="width" from="0" to="168" dur="1.1s" begin="1.05s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>
  <g class="row" style="animation-delay:1.25s">
    <circle cx="26" cy="133" r="5" fill="#e81c5f"/>
    <text x="40" y="138" font-size="13" fill="#fdffff" font-weight="bold">TypeScript / Next.js</text>
    <text x="396" y="138" text-anchor="end" font-size="13" fill="#fdffff" font-weight="bold">30.0%</text>
    <rect x="40" y="146" width="268" height="9" rx="4.5" fill="#241740"/>
    <rect class="bar" x="40" y="146" width="120" height="9" rx="4.5" fill="#e81c5f" style="animation-delay:1.40s">
      <animate attributeName="width" from="0" to="120" dur="1.1s" begin="1.40s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>
  <g class="row" style="animation-delay:1.60s">
    <circle cx="26" cy="175" r="5" fill="#c70039"/>
    <text x="40" y="180" font-size="13" fill="#fdffff" font-weight="bold">HTML5 / CSS3 / Tailwind</text>
    <text x="396" y="180" text-anchor="end" font-size="13" fill="#fdffff" font-weight="bold">15.0%</text>
    <rect x="40" y="188" width="268" height="9" rx="4.5" fill="#241740"/>
    <rect class="bar" x="40" y="188" width="60" height="9" rx="4.5" fill="#c70039" style="animation-delay:1.75s">
      <animate attributeName="width" from="0" to="60" dur="1.1s" begin="1.75s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>
  <g class="row" style="animation-delay:1.95s">
    <circle cx="26" cy="217" r="5" fill="#900028"/>
    <text x="40" y="222" font-size="13" fill="#fdffff" font-weight="bold">SQL / PostgreSQL</text>
    <text x="396" y="222" text-anchor="end" font-size="13" fill="#fdffff" font-weight="bold">8.0%</text>
    <rect x="40" y="230" width="268" height="9" rx="4.5" fill="#241740"/>
    <rect class="bar" x="40" y="230" width="32" height="9" rx="4.5" fill="#900028" style="animation-delay:2.10s">
      <animate attributeName="width" from="0" to="32" dur="1.1s" begin="2.10s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>
<g clip-path="url(#cardc)"><rect class="sh" x="0" y="0" width="100" height="282" fill="url(#shg)" transform="skewX(-15)"/></g>
</svg>'''

with open(os.path.join(TARGET_DIR, "langs.svg"), "w", encoding="utf-8") as f:
    f.write(langs_svg)

print("Created langs.svg")


# ==========================================
# 4. lanyard.svg (ViewBox 0 0 420 660)
# ==========================================
lanyard_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 660" width="420" height="660" role="img" aria-label="Mr. Anonymous ID card lanyard">
<title>Mr. Anonymous — swinging ID badge</title>
<defs>
<style type="text/css"><![CDATA[
text{{font-family:'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace}}
@keyframes settle{{0%{{transform:rotate(0deg) translateY(-660px)}}18%{{transform:rotate(0deg) translateY(0)}}30%{{transform:rotate(13deg)}}46%{{transform:rotate(-9deg)}}62%{{transform:rotate(6deg)}}78%{{transform:rotate(-3.5deg)}}92%{{transform:rotate(1.5deg)}}100%{{transform:rotate(0deg)}}}}
@keyframes sway{{0%,100%{{transform:rotate(-3.2deg)}}50%{{transform:rotate(3.2deg)}}}}
@keyframes cardWobble{{0%,100%{{transform:rotate(1.6deg)}}50%{{transform:rotate(-1.6deg)}}}}
@keyframes shine{{0%{{transform:translateX(-340px) skewX(-18deg)}}55%,100%{{transform:translateX(420px) skewX(-18deg)}}}}
@keyframes twinkle{{0%,100%{{opacity:0;transform:scale(.4)}}50%{{opacity:1;transform:scale(1)}}}}
@keyframes heartBeat{{0%,100%{{transform:scale(1)}}12%{{transform:scale(1.25)}}24%{{transform:scale(1)}}36%{{transform:scale(1.15)}}48%{{transform:scale(1)}}}}
@keyframes fadeIn{{from{{opacity:0}}to{{opacity:1}}}}
.settle{{transform-origin:210px 6px;animation:settle 3.4s cubic-bezier(.34,1.1,.5,1) forwards}}
.sway{{transform-origin:210px 6px;animation:sway 4.2s ease-in-out 3.4s infinite}}
.wob{{transform-origin:210px 300px;animation:cardWobble 4.2s ease-in-out 3.4s infinite}}
.shine{{animation:shine 4.5s ease-in-out 3.6s infinite}}
.tw{{transform-box:fill-box;transform-origin:center;animation:twinkle 2.8s ease-in-out infinite}}
.hb{{transform-box:fill-box;transform-origin:center;animation:heartBeat 2.4s ease-in-out infinite}}
]]></style>
<linearGradient id="strapg" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%" stop-color="#280000"/><stop offset="50%" stop-color="#ff004d"/><stop offset="100%" stop-color="#280000"/>
</linearGradient>
<linearGradient id="cardg" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#1d1330"/><stop offset="100%" stop-color="#140d22"/>
</linearGradient>
<linearGradient id="cardborder" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%"><animate attributeName="stop-color" values="#ff004d;#fdffff;#570000;#ff004d" dur="6s" repeatCount="indefinite"/></stop>
  <stop offset="100%"><animate attributeName="stop-color" values="#570000;#ff004d;#fdffff;#570000" dur="6s" repeatCount="indefinite"/></stop>
</linearGradient>
<linearGradient id="metal" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0%" stop-color="#c8ccd6"/><stop offset="45%" stop-color="#8a90a0"/><stop offset="55%" stop-color="#6a7080"/><stop offset="100%" stop-color="#9aa0b0"/>
</linearGradient>
<linearGradient id="shineg" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%" stop-color="#fff" stop-opacity="0"/><stop offset="50%" stop-color="#fff" stop-opacity=".18"/><stop offset="100%" stop-color="#fff" stop-opacity="0"/>
</linearGradient>
<radialGradient id="lglow"><stop offset="0%" stop-color="#ff004d" stop-opacity=".2"/><stop offset="100%" stop-color="#ff004d" stop-opacity="0"/></radialGradient>
<filter id="glow2"><feGaussianBlur stdDeviation="2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="cardShadow" x="-30%" y="-30%" width="160%" height="160%"><feDropShadow dx="0" dy="10" stdDeviation="14" flood-color="#000" flood-opacity=".55"/></filter>
<clipPath id="cardclip"><rect x="82" y="298" width="256" height="330" rx="20"/></clipPath>
<clipPath id="avatarclip"><circle cx="210" cy="412" r="59"/></clipPath>
</defs>

<circle cx="210" cy="440" r="230" fill="url(#lglow)"><animate attributeName="r" values="230;250;230" dur="5s" repeatCount="indefinite"/></circle>

<g class="tw" style="animation-delay:.5s"><path d="M60 200l3 8 8 3-8 3-3 8-3-8-8-3 8-3z" fill="#ff004d"/></g>
<g class="tw" style="animation-delay:1.6s"><path d="M372 300l2.4 6.4 6.4 2.4-6.4 2.4-2.4 6.4-2.4-6.4-6.4-2.4 6.4-2.4z" fill="#fdffff"/></g>
<g class="tw" style="animation-delay:2.7s"><path d="M52 480l2.4 6.4 6.4 2.4-6.4 2.4-2.4 6.4-2.4-6.4-6.4-2.4 6.4-2.4z" fill="#ff004d"/></g>
<g class="hb" style="animation-delay:1s"><path d="M368 480 c-4-9-17-7-17 3 0 7 10 13 17 18 7-5 17-11 17-18 0-10-13-12-17-3z" fill="#ff004d" opacity=".85" filter="url(#glow2)"/></g>

<!-- pendulum: settle then sway -->
<g class="settle"><g class="sway">

  <!-- Strap -->
  <g>
    <path d="M191 -6 L229 -6 L226 236 L194 236 Z" fill="url(#strapg)"/>
    <line x1="196" y1="0" x2="198.5" y2="234" stroke="#fff" stroke-opacity=".55" stroke-width="1" stroke-dasharray="4 3"/>
    <line x1="224" y1="0" x2="221.5" y2="234" stroke="#fff" stroke-opacity=".55" stroke-width="1" stroke-dasharray="4 3"/>
    <text x="0" y="0" font-size="10.5" font-weight="bold" fill="#fff" opacity=".95" letter-spacing="2" transform="translate(214,18) rotate(90)">MR. ANONYMOUS ♥ CODE ♥ MR. ANONYMOUS</text>
  </g>

  <!-- Clasp + ring -->
  <rect x="188" y="232" width="44" height="26" rx="6" fill="url(#metal)" stroke="#4a4f5c" stroke-width="1"/>
  <rect x="199" y="238" width="22" height="7" rx="3.5" fill="#3c414e"/>
  <circle cx="210" cy="272" r="14" fill="none" stroke="url(#metal)" stroke-width="5.5"/>

  <!-- Card (secondary wobble) -->
  <g class="wob">
    <rect x="82" y="298" width="256" height="330" rx="20" fill="url(#cardg)" stroke="url(#cardborder)" stroke-width="2" filter="url(#cardShadow)"/>
    <!-- slot -->
    <rect x="180" y="310" width="60" height="10" rx="5" fill="#0a0714" stroke="#3b2a5c" stroke-width="1"/>

    <g clip-path="url(#cardclip)">
      <!-- header band -->
      <rect x="82" y="298" width="256" height="34" fill="#231541" opacity=".7"/>
      <text x="98" y="320" font-size="9" fill="#fdffff" opacity="0.9" letter-spacing="1.5">DEVELOPER ID</text>
      <text x="322" y="320" text-anchor="end" font-size="9" fill="#ff004d" font-weight="bold" letter-spacing="1.5">ID-071105</text>

      <!-- avatar -->
      <circle cx="210" cy="412" r="59" fill="none" stroke="url(#cardborder)" stroke-width="2.5"/>
      <image x="154" y="356" width="112" height="112" href="data:image/png;base64,{B64_AVATAR}" clip-path="url(#avatarclip)"/>

      <!-- name & details -->
      <text x="210" y="500" text-anchor="middle" font-size="18" font-weight="bold" fill="#fdffff" filter="url(#glow2)">Mr. Anonymous</text>
      <text x="210" y="522" text-anchor="middle" font-size="11" fill="#ff004d" font-weight="bold" letter-spacing="2.5">STUDENT // AI ENGINEER</text>
      <text x="210" y="540" text-anchor="middle" font-size="10.5" fill="#fdffff" opacity="0.9">@Mr-Anonymous-Guy</text>

      <line x1="100" y1="552" x2="320" y2="552" stroke="#2a1f3d" stroke-width="1"/>

      <!-- barcode + tag -->
      <g transform="translate(100,564)"><rect x="0" y="0" width="2.5" height="26" fill="#fdffff" opacity=".9"/><rect x="5.0" y="0" width="1.5" height="26" fill="#fdffff" opacity=".9"/><rect x="9.0" y="0" width="1.5" height="26" fill="#fdffff" opacity=".9"/><rect x="12.0" y="0" width="1.5" height="26" fill="#fdffff" opacity=".9"/><rect x="16.0" y="0" width="4" height="26" fill="#fdffff" opacity=".9"/><rect x="21.5" y="0" width="1.5" height="26" fill="#fdffff" opacity=".9"/><rect x="26.0" y="0" width="4" height="26" fill="#fdffff" opacity=".9"/><rect x="31.5" y="0" width="1.5" height="26" fill="#fdffff" opacity=".9"/><rect x="34.5" y="0" width="4" height="26" fill="#fdffff" opacity=".9"/><rect x="41.0" y="0" width="1.5" height="26" fill="#fdffff" opacity=".9"/><rect x="45.5" y="0" width="2.5" height="26" fill="#fdffff" opacity=".9"/><rect x="50.5" y="0" width="1.5" height="26" fill="#fdffff" opacity=".9"/><rect x="54.5" y="0" width="1.5" height="26" fill="#fdffff" opacity=".9"/><rect x="58.5" y="0" width="2.5" height="26" fill="#fdffff" opacity=".9"/><rect x="63.5" y="0" width="2.5" height="26" fill="#fdffff" opacity=".9"/><rect x="67.5" y="0" width="1.5" height="26" fill="#fdffff" opacity=".9"/><rect x="72.0" y="0" width="1.5" height="26" fill="#fdffff" opacity=".9"/><rect x="76.5" y="0" width="1.5" height="26" fill="#fdffff" opacity=".9"/><rect x="81.0" y="0" width="1.5" height="26" fill="#fdffff" opacity=".9"/><rect x="84.0" y="0" width="2.5" height="26" fill="#fdffff" opacity=".9"/><rect x="89.0" y="0" width="1.5" height="26" fill="#fdffff" opacity=".9"/><rect x="93.5" y="0" width="4" height="26" fill="#fdffff" opacity=".9"/></g>
      <text x="320" y="578" text-anchor="end" font-size="8.5" fill="#fdffff" opacity="0.9">PYTHON • FASTAPI</text>
      <text x="320" y="590" text-anchor="end" font-size="8.5" fill="#fdffff" opacity="0.9">LLMS • RAG</text>

      <!-- holo shine sweep -->
      <rect class="shine" x="82" y="288" width="120" height="360" fill="url(#shineg)"/>
    </g>
  </g>
</g></g>

<text x="210" y="652" text-anchor="middle" font-size="10" fill="#fdffff" opacity="0.8" style="animation:fadeIn .6s ease 3.6s forwards">— drag me… just kidding, I'm an SVG ♥ —</text>
</svg>'''

with open(os.path.join(TARGET_DIR, "lanyard.svg"), "w", encoding="utf-8") as f:
    f.write(lanyard_svg)

print("Created lanyard.svg")
print("All 4 SVGs updated successfully!")
