"""Builds the static site: python build.py  (writes the .html files next to this script)."""
import os, hashlib

ROOT = os.path.dirname(os.path.abspath(__file__))
NAV = [("Home", "index.html"), ("Research", "research/index.html"), ("Publications", "publications.html"),
       ("CV", "cv.html"), ("Contact", "contact.html")]
CSSV = hashlib.md5(open(os.path.join(ROOT, "assets/css/style.css"), "rb").read()).hexdigest()[:8]
DESC = "Venu Gopal Agarwal — computational researcher in electrochemical energy conversion at EPFL."


import math
EUSTARS = "".join(f'<circle cx="{15 + 6 * math.sin(2 * math.pi * k / 12):.2f}" cy="{10 - 6 * math.cos(2 * math.pi * k / 12):.2f}" r="0.9"/>' for k in range(12))


def page(path, title, body, desc=DESC, raw=False, img="assets/img/profile.jpg"):
    up = "../" * path.count("/")
    nav = "\n".join(
        f'      <a{" class=\"active\"" if href == path or (href.startswith("research/") and path.startswith("research/")) else ""} href="{up}{href}">{name}</a>'
        for name, href in NAV)
    inner = body if raw else f'  <div class="wrap section">\n{body}\n  </div>'
    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="https://venuagarwal.com/{img}">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="canonical" href="https://venuagarwal.com/{"" if path == "index.html" else path}">
  <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%230e7490'/%3E%3Ctext x='32' y='42' font-family='Arial' font-size='26' font-weight='700' fill='white' text-anchor='middle'%3EVA%3C/text%3E%3C/svg%3E">
  <link rel="stylesheet" href="{up}assets/css/style.css?v={CSSV}">
</head>
<body>
<header class="site">
  <div class="wrap">
    <a class="brand" href="{up}index.html"><span class="mono">VA</span>Venu Gopal Agarwal</a>
    <nav>
{nav}
    </nav>
  </div>
</header>
<main>
{inner.replace('{up}', up)}
</main>
<footer>
  <div class="wrap eu"><svg viewBox="0 0 30 20" width="36" height="24" aria-label="Flag of the European Union" role="img"><rect width="30" height="20" fill="#003399"/><g fill="#FFCC00">{EUSTARS}</g></svg><span>PhD research funded by the EPFLglobaLeaders programme, which received funding from the European Union’s Horizon 2020 research and innovation programme under the Marie Skłodowska-Curie grant agreement No 945363, and by the Swiss National Science Foundation (project <a href="https://data.snf.ch/grants/grant/197268">200021_197268</a>).</span></div>
  <div class="wrap"><span>© 2026 Venu Gopal Agarwal</span><span><a href="https://scholar.google.com/citations?user=9_OIf0YAAAAJ">Scholar</a> · <a href="https://orcid.org/0000-0003-2992-6539">ORCID</a> · <a href="https://www.linkedin.com/in/venu-agarwal-phd-08076a191/">LinkedIn</a> · LRESE, EPFL</span></div>
</footer>
</body>
</html>
"""
    out = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write(html)


# (file, icon, title, period, tag, intro, bullet points, footnote)
PROJECTS = [
    ("crutches.html", "💧", "Flooding and salt in zero-gap CO<sub>2</sub> electrolysers", "Postdoc · 2026 – present", "in progress",
     "Zero-gap membrane electrode assemblies reach industrial current densities, but their cathodes flood and fill with (bi)carbonate salt within hundreds of hours.",
     ["A full-cell, multiphysics model of a CO<sub>2</sub>-to-CO membrane electrode assembly: species, charge, water and heat transport across the gas diffusion layer, microporous layer, catalyst layer, membrane and anode.",
      "Liquid water in every porous layer with pore-size-based capillary curves and potential-dependent electrowetting.",
      "Precipitated salt treated as a solid phase that changes porosity, permeability, active area and wettability, followed in time.",
      "Calibrated on a Ag/Cs<sup>+</sup> cell; used to compare mitigation strategies such as pulsed operation and thermal gradients over the time scale on which they act."],
     "Supervisor: Prof. Sophia Haussener."),
    ("bicarbonate.html", "🫧", "Bicarbonate-fed bipolar-membrane electrolysers", "PhD · 2021 – 2026", "manuscript in preparation",
     "Bicarbonate electrolysers convert captured carbon directly, without regenerating and compressing CO<sub>2</sub> gas: protons from a bipolar membrane release CO<sub>2</sub> in the catalyst layer, where it is reduced to CO.",
     ["Coupled the gas-diffusion-electrode and bipolar-membrane models into one integrated electrolyser model linking electrochemistry, ion transport and water management.",
      "Validated against measured CO faradaic efficiencies.",
      "Used the model to evaluate catalyst-layer, substrate and membrane designs."],
     "Supervisor: Prof. Sophia Haussener.<br>Funded by the Swiss National Science Foundation, project <a href=\"https://data.snf.ch/grants/grant/197268\">200021_197268</a> “Overcoming fluid transport limitations in gas-fed CO<sub>2</sub> reduction devices with bipolar membranes” (PSI and EPFL, 2021–2026)."),
    ("bpm.html", "⚡", "Bipolar membrane modelling", "PhD · 2021 – 2026", "in preparation",
     "Bipolar membranes split water at the junction between a cation- and an anion-exchange layer, driven by strong local electric fields.",
     ["One-dimensional Poisson–Nernst–Planck model with electric-field-enhanced (second Wien effect) water dissociation.",
      "Hydration-dependent transport and membrane water balance.",
      "Parametric and sensitivity studies to isolate rate-limiting transport mechanisms and guide membrane design."],
     "Supervisor: Prof. Sophia Haussener.<br>Funded by the Swiss National Science Foundation, project <a href=\"https://data.snf.ch/grants/grant/197268\">200021_197268</a> “Overcoming fluid transport limitations in gas-fed CO<sub>2</sub> reduction devices with bipolar membranes” (PSI and EPFL, 2021–2026)."),
    ("microfluidic-gde.html", "🔬", "Mass-transport limits in a microfluidic GDE electrolyser", "PhD", "Communications Chemistry · 2024",
     "Gas diffusion electrodes deliver CO<sub>2</sub> to the catalyst in the gas phase, but performance is still set by how fast reactants and products move through the porous layers and electrolyte.",
     ["Two-dimensional model of a gas-diffusion cathode in a microfluidic flow cell, resolving coupled charge, species and momentum transport.",
      "Validated against experimental data.",
      "Quantified which transport processes limit performance and where.",
      "Interactive viewer and movie below: the model across the full potential sweep."],
     'V. G. Agarwal, S. Haussener, <a href="https://doi.org/10.1038/s42004-024-01122-5">Communications Chemistry 7, 47 (2024)</a> — open access.'),
    ("buffer-dissociation.html", "🧪", "Field-enhanced dissociation of buffer species", "Collaboration", "ACS Electrochemistry · 2025",
     "Strong interfacial electric fields can accelerate the dissociation of protonated buffer species, changing the local pH near electrodes and membranes.",
     ["Numerical analysis of field-enhanced homogeneous dissociation of protonated buffer species."],
     'M. Wada, K. Obata, V. G. Agarwal, F. Lorenzutti, S. Haussener, K. Takanabe, <a href="https://doi.org/10.1021/acselectrochem.5c00299">ACS Electrochemistry (2025)</a>.'),
    ("droplets-lbm.html", "💦", "Droplet formation in microfluidic T-junctions", "M.S. (R), IIT Delhi · 2018 – 2019", "Physical Review Fluids · 2020",
     "How droplets form and how the flow regime changes in a T-shaped microfluidic device.",
     ["Parallel (MPI) lattice Boltzmann solver written from scratch in C/C++.",
      "Validated against in-house experiments."],
     'V. G. Agarwal, R. Singh, S. S. Bahga, A. Gupta, <a href="https://doi.org/10.1103/PhysRevFluids.5.044203">Physical Review Fluids 5, 044203 (2020)</a>.'),
    ("battery-rom.html", "🔋", "Real-time state of charge of Li-ion cells", "Research assistant, IIT Delhi · 2020", "",
     "Battery management systems need fast, accurate state-of-charge estimates.",
     ["Data-driven, control-oriented reduced-order model (discrete-time realisation algorithm) for a Li-ion cell.",
      "Accurate state-of-charge estimation across standard drive cycles."],
     "Thermofluids &amp; Energy Systems Lab, IIT Delhi."),
]


THUMB = {"crutches.html": "assets/graphics/crutches.svg", "bicarbonate.html": "assets/graphics/bicarbonate.svg",
         "bpm.html": "assets/graphics/bpm.svg", "microfluidic-gde.html": "assets/media/gde_poster.jpg",
         "buffer-dissociation.html": "assets/graphics/buffer.svg", "droplets-lbm.html": "assets/media/lbm/exp_vs_lbm_poster.jpg",
         "battery-rom.html": "assets/graphics/battery.svg"}
OGIMG = {k: (v if v.endswith(".jpg") else "assets/img/profile.jpg") for k, v in THUMB.items()}


def card(p):
    fn, icon, t, per, tag, intro, pts, foot = p
    short = intro if len(intro) < 160 else intro[:160].rsplit(" ", 1)[0] + "…"
    tagh = f'<span class="tag">{tag}</span>' if tag else '<span class="tag">' + per + '</span>'
    top = f'<img class="thumb" src="{{up}}{THUMB[fn]}" alt="Illustration: {t.replace('<sub>', '').replace('</sub>', '')}" loading="lazy">' if fn in THUMB else f'<div class="icon">{icon}</div>'
    return (f'      <a class="card" href="{{up}}research/{fn}">\n        {top}\n'
            f'        <h3>{t}</h3>\n        <p>{short}</p>\n        {tagh}\n      </a>')


EXTRA = {
    "microfluidic-gde.html": """
    <section class="viewer narrow wide">
      <h2>Ideally wetted vs. fully flooded</h2>
      <p class="section-sub">Dissolved CO<sub>2</sub> (electrolyte channel, catalyst layer) and gaseous CO<sub>2</sub> (GDL, gas channel) during the potential sweep, with the CO and H<sub>2</sub> partial currents of the same models.</p>
      <video class="clip" autoplay loop muted playsinline preload="metadata" poster="{up}assets/media/gde_poster.jpg" src="{up}assets/media/gde_wetted_vs_flooded.mp4"></video>
      <p class="muted">2D model of the microfluidic flow cell; frames computed every 0.05 V and interpolated in between. Panels have separate x scales; dotted lines mark the electrode ends.</p>
      <p><a class="btn primary" href="gde-explorer.html">Open the interactive slider →</a></p>
    </section>""",
    "droplets-lbm.html": """
    <section class="viewer narrow">
      <h2>Experiment vs. simulation</h2>
      <p class="section-sub">High-speed movies of the T-junction experiments next to the lattice Boltzmann simulations for the three droplet flow regimes.</p>
      <video class="clip" autoplay loop muted playsinline preload="metadata" poster="{up}assets/media/lbm/exp_vs_lbm_poster.jpg" src="{up}assets/media/lbm/exp_vs_lbm.mp4"></video>
      <p class="muted">Experiment frames mirrored and cropped to the junction so that both columns flow left to right. Simulations: Cr = 100, 10 and 0.01 (top to bottom) at Ca = 0.5, n = 0.5.</p>
    </section>
    <section class="viewer narrow">
      <h2>Effect of shear thinning</h2>
      <p class="section-sub">A lower power-law index n (stronger shear thinning of the continuous phase) gives larger droplets; Ca = 0.1, Cr = 1.</p>
      <div class="sim-row">
        <figure><video autoplay loop muted playsinline src="{up}assets/media/lbm/sim_n10.mp4"></video><figcaption>n = 1.0 (Newtonian)</figcaption></figure>
        <figure><video autoplay loop muted playsinline src="{up}assets/media/lbm/sim_n07.mp4"></video><figcaption>n = 0.7</figcaption></figure>
        <figure><video autoplay loop muted playsinline src="{up}assets/media/lbm/sim_n03.mp4"></video><figcaption>n = 0.3</figcaption></figure>
      </div>
    </section>""",
}

# key results (published work only: quoted from the papers) or the approach (unpublished work)
KEY = {
    "microfluidic-gde.html": ("Key findings", [
        "Validated 2D model of the cathode side of a microfluidic CO<sub>2</sub>-to-CO flow cell with a gas diffusion electrode.",
        "With a fully flooded catalyst layer the CO partial current density peaks at <b>75 mA cm<sup>−2</sup> at −1.3 V vs RHE</b>, then falls as CO<sub>2</sub> near the catalyst runs out.",
        "A large part of the catalyst layer stays <b>underutilised</b>; graded porosity and anisotropic layers are proposed to improve mass transport.",
        "Higher CO<sub>2</sub> gas flow raises the CO current but lowers CO<sub>2</sub> conversion efficiency: a clear trade-off."]),
    "buffer-dissociation.html": ("Key findings", [
        "Generalised modified Poisson–Nernst–Planck model with electric-field-enhanced (second Wien effect) dissociation, for unbuffered KClO<sub>4</sub> and buffered carbonate and phosphate electrolytes.",
        "With buffers, field-enhanced protolysis lets <b>free protons act as HER reactants above several hundred mA cm<sup>−2</sup></b>.",
        "In the diffuse layer the effective proton concentration <b>exceeds the bulk value</b>.",
        "A strong field sensitivity can overestimate water dissociation, especially in unbuffered electrolytes."]),
    "droplets-lbm.html": ("Key findings", [
        "3D multicomponent lattice Boltzmann model with a Carreau–Yasuda continuous phase, validated against T-junction experiments.",
        "Stronger shear thinning of the continuous phase gives <b>larger droplets</b> and changes their shape <b>from spherical to plug-shaped</b>, behaviour usually seen only at low capillary number in Newtonian flows.",
        "Mapped the transitions between parallel flow, droplets in the channel and droplets at the junction as a function of the Carreau and capillary numbers."]),
    "crutches.html": ("Approach", [
        "Full-cell model of a zero-gap CO<sub>2</sub>-to-CO electrolyser, from the gas channel to the anolyte.",
        "Follows where liquid water and (bi)carbonate salt accumulate in the porous cathode, and how they change transport over time.",
        "Results are being prepared for publication."]),
    "bicarbonate.html": ("Approach", [
        "Integrated model of a bicarbonate-fed electrolyser: Ni-foam anode, bipolar membrane, Ag catalyst layer and porous cathode.",
        "Tracks in-situ CO<sub>2</sub> release from bicarbonate by membrane-generated protons and its reduction to CO.",
        "Results are in a manuscript in preparation."]),
    "bpm.html": ("Approach", [
        "Resolves the space-charge region at the junction, where fields of order 10<sup>8</sup> V m<sup>−1</sup> accelerate water dissociation.",
        "Results are in a manuscript in preparation."]),
}
FIG = {
    "crutches.html": ("assets/graphics/crutches.svg", "Schematic of the modelled zero-gap cell: CO<sub>2</sub> diffuses through the GDL and MPL to the Ag catalyst layer, while liquid water, (bi)carbonate salt and Cs<sup>+</sup> crossing the membrane accumulate in the cathode."),
    "bicarbonate.html": ("assets/graphics/bicarbonate.svg", "Protons from the bipolar membrane react with bicarbonate at the catalyst layer, releasing CO<sub>2</sub> where it is reduced to CO."),
    "bpm.html": ("assets/graphics/bpm.svg", "Water splits at the junction of the cation- and anion-exchange layers; protons move to the cathode side and hydroxide to the anode side."),
    "buffer-dissociation.html": ("assets/graphics/buffer.svg", "Near a hydrogen-evolving electrode the strong interfacial field dissociates buffer molecules, raising the local free-proton concentration above the bulk."),
    "battery-rom.html": ("assets/graphics/battery.svg", "Measured current and voltage drive a reduced-order model that estimates the state of charge in real time."),
}


def keybox(fn):
    if fn not in KEY:
        return ""
    h, items = KEY[fn]
    li = "\n".join(f"        <li>{x}</li>" for x in items)
    return f'\n      <div class="keybox"><h2>{h}</h2>\n      <ul>\n{li}\n      </ul></div>'


def figure(fn):
    if fn not in FIG:
        return ""
    src, cap = FIG[fn]
    return f'\n    <figure class="hero-fig"><img src="{{up}}{src}" alt="Schematic: {cap[:90]}"><figcaption>{cap}</figcaption></figure>'


for p in PROJECTS:
    fn, icon, title, period, tag, intro, points, foot = p
    lis = "\n".join(f"      <li>{x}</li>" for x in points)
    tagh = f'<span class="tag">{tag}</span>' if tag else ""
    plain = intro.replace('<sub>', '').replace('</sub>', '')
    page("research/" + fn, f"{title.replace('<sub>2</sub>', '2')} | Venu Gopal Agarwal", f"""    <div class="project-head">
      <p class="kicker"><a href="index.html">← Research</a> · {period}</p>
      <h1 class="page">{title}</h1>
      {tagh}
    </div>{figure(fn)}
    <div class="project-body">
      <p class="lead">{intro}</p>{keybox(fn)}
      <h2>What I did</h2>
      <ul>
{lis}
      </ul>
      <div class="note">{foot}</div>
    </div>{EXTRA.get(fn, "")}""", desc=plain, img=OGIMG.get(fn, "assets/img/profile.jpg"))

page("research/index.html", "Research | Venu Gopal Agarwal", f"""    <h1 class="page">Research</h1>
    <p class="section-sub lead">Physics-based models of electrochemical energy-conversion devices — coupled, nonlinear transport of charge, species, water, heat and momentum — validated against experiments to find what limits performance and lifetime.</p>
    <div class="cards">
{chr(10).join(card(p) for p in PROJECTS)}
    </div>""")

IMG = os.path.exists(os.path.join(ROOT, "assets/img/profile.jpg"))
portrait = '<div class="portrait"><img src="{up}assets/img/profile.jpg" alt="Portrait of Venu Gopal Agarwal"></div>' if IMG else ""
page("index.html", "Venu Gopal Agarwal — CO2 electrolysis modelling, EPFL", f"""  <section class="hero-band">
    <div class="wrap">
      <div class="hero">
        <div>
          <p class="eyebrow">Computational electrochemistry · EPFL</p>
          <h1>Venu Gopal Agarwal</h1>
          <p class="role">Postdoctoral researcher, Laboratory of Renewable Energy Science and Engineering (LRESE)</p>
          <p class="bio">I build multiphysics models of CO<sub>2</sub> electrolysers, bipolar membranes and gas diffusion electrodes — resolving the coupled transport of charge, species, water, heat and momentum — and validate them against experiments to find what limits their efficiency and lifetime.</p>
          <div class="buttons">
            <a class="btn primary" href="{{up}}research/index.html">Explore research →</a>
            <a class="btn" href="{{up}}publications.html">Publications</a>
            <a class="btn" href="{{up}}assets/cv/Venu_Gopal_Agarwal_CV.pdf">Download CV (PDF)</a>
          </div>
          <p class="profiles"><a href="https://scholar.google.com/citations?user=9_OIf0YAAAAJ">Google Scholar</a> · <a href="https://orcid.org/0000-0003-2992-6539">ORCID</a> · <a href="https://www.linkedin.com/in/venu-agarwal-phd-08076a191/">LinkedIn</a></p>
        </div>
        {portrait}
      </div>
      <div class="stats">
        <div class="stat"><b>PhD, EPFL</b><span>Energy Sciences, 2026</span></div>
        <div class="stat"><b>MSCA fellow</b><span>EPFLglobaLeaders, Horizon 2020</span></div>
        <div class="stat"><b>Gold Medal</b><span>M.S. (R), IIT Delhi</span></div>
        <div class="stat"><b>7 conference talks &amp; posters</b><span>ECS, ModVal, SCS, PSI</span></div>
      </div>
    </div>
  </section>
  <div class="wrap section">
    <h2>Research highlights</h2>
    <p class="section-sub">Current and recent projects — click a card for details.</p>
    <div class="cards two">
{chr(10).join(card(p) for p in PROJECTS[:4])}
    </div>
  </div>""", raw=True)

PUBS = [
    ("ACS Electrochemistry · 2025", "Numerical analysis on field-enhanced homogeneous dissociation of protonated buffer species",
     "M. Wada, K. Obata, <b>V. G. Agarwal</b>, F. Lorenzutti, S. Haussener, K. Takanabe", "https://doi.org/10.1021/acselectrochem.5c00299"),
    ("Communications Chemistry · 2024", "Quantifying mass transport limitations in a microfluidic CO<sub>2</sub> electrolyzer with a gas diffusion cathode",
     "<b>V. G. Agarwal</b>, S. Haussener", "https://doi.org/10.1038/s42004-024-01122-5"),
    ("Physical Review Fluids · 2020", "Dynamics of droplet formation and flow regime transition in a T-shaped microfluidic device",
     "<b>V. G. Agarwal</b>, R. Singh, S. S. Bahga, A. Gupta", "https://doi.org/10.1103/PhysRevFluids.5.044203"),
    ("Book chapter, Energy for Propulsion (Springer) · 2018", "Investigation of the role of chemical kinetics in controlling stabilization mechanism of the turbulent lifted jet flame using multi-flamelet generated manifold approach",
     "R. Saini, A. De, <b>V. Agarwal</b>, R. Yadav", "https://doi.org/10.1007/978-981-10-7473-8_12"),
]
TALKS = [  # (meeting, type, title, authors, link) - SNSF report, M.S. defence slides, official programmes/abstract books
    ("ModVal 2026, Lausanne, 10–11 Mar 2026", "Poster", "Model-based optimization of cathode architecture and bipolar membrane properties in bicarbonate-fed CO<sub>2</sub> electrolyzers",
     "<b>V. Agarwal</b>, N. Wanninayake, S. Shah, M. Shahar, A. Smeltz, S. Haussener", "https://doi.org/10.5281/zenodo.18980448"),
    ("SCS Spring Meeting “Electrocatalysis”, Bern, 24 Apr 2025", "Poster", "Performance comparison between forward- and reverse-biased bipolar membranes for CO<sub>2</sub> electrolysis",
     "<b>V. Agarwal</b>, P. Brimley, S. Haussener", "https://scg.ch/component/eventbooking/scs-spring-meeting-2025-electrocatalysis-current-challenges-and-future-perspectives"),
    ("ModVal 2025, Karlsruhe, 11–12 Mar 2025", "Poster", "Modelling water transport in bipolar membranes for CO<sub>2</sub> electrolysis application",
     "<b>V. G. Agarwal</b>, P. Brimley, S. Haussener", "https://events.hs-offenburg.de/event/471/attachments/76/359/ModVal%202025%20Book%20of%20Abstracts.pdf#page=76"),
    ("245th ECS Meeting, San Francisco, 28 May 2024", "Talk", "Water transport management in a bipolar membrane for CO<sub>2</sub> electrolysis application",
     "<b>V. Agarwal</b>, S. Haussener", "https://doi.org/10.1149/MA2024-01372167mtgabs"),
    ("39th Swiss Electrochemistry Symposium (PSI), Aarau, 26 Apr 2023", "Poster", "Modelling of a gas-diffusion electrode for CO<sub>2</sub> electroreduction",
     "<b>V. Agarwal</b>, S. Haussener", "https://indico.psi.ch/event/13425/"),
    ("28th DSFD, JNCASR Bangalore, 22–26 Jul 2019", "Talk", "Droplet formation at a T-junction microchannel using a shear-thinning continuous phase",
     "<b>V. G. Agarwal</b>, R. Singh, A. Gupta", ""),
    ("COMPFLU 2018, IIT Roorkee, 6–9 Dec 2018", "Talk", "Towards an understanding of electrohydrodynamic and non-Newtonian effects in T-junction microfluidic devices",
     "A. Gupta, R. Singh, <b>V. G. Agarwal</b>", "https://www.iitr.ac.in/compflu2018/docs/COMPFLU_2018_Detailed_Program_Schedule.pdf#page=4"),
]
LINKTXT = {"doi.org/10.5281": "Proceedings (Zenodo)", "doi.org/10.1149": "Abstract", "hs-offenburg": "Abstract", "scg.ch": "Meeting page", "iitr.ac.in": "Programme", "indico.psi.ch": "Programme"}


def talk(m, k, t, a, u):
    lt = next((v for key, v in LINKTXT.items() if key in u), "Link")
    link = f' · <a href="{u}">{lt} ↗</a>' if u else ""
    return (f'    <div class="pub"><span class="venue{" alt" if k == "Poster" else ""}">{k}</span> <span class="muted">{m}</span>'
            f'<p class="title">{t}</p><p class="authors">{a}{link}</p></div>')


talks = chr(10).join(talk(*x) for x in TALKS)

pubs = "\n".join(f'    <div class="pub"><span class="venue">{v}</span><p class="title"><a href="{u}">{t}</a></p><p class="authors">{a}</p></div>' for v, t, a, u in PUBS)
page("publications.html", "Publications | Venu Gopal Agarwal", f"""    <h1 class="page">Publications</h1>
    <p class="section-sub">Peer-reviewed articles.</p>
{pubs}
    <h2 style="margin-top:40px">In preparation</h2>
    <div class="cards">
      <div class="card"><h3>Bicarbonate-fed CO<sub>2</sub>-to-CO electrolysers</h3><p>Design and optimisation of bipolar-membrane bicarbonate electrolysers.</p><span class="tag">manuscript</span></div>
      <div class="card"><h3>Bipolar membrane modelling</h3><p>Field-enhanced water dissociation and ion transport.</p><span class="tag">manuscript</span></div>
      <div class="card"><h3>Flooding and salt in zero-gap electrolysers</h3><p>Mechanisms and mitigation of degradation over time.</p><span class="tag">manuscript</span></div>
    </div>
    <h2 style="margin-top:40px">Talks and posters</h2>
{talks}
    <p class="muted" style="margin-top:14px">Best poster award, IIT Kanpur, 2017.</p>""")

page("cv.html", "CV | Venu Gopal Agarwal", """    <h1 class="page">Curriculum vitae</h1>
    <p><a class="btn primary" href="assets/cv/Venu_Gopal_Agarwal_CV.pdf">Download CV (PDF)</a></p>
    <h2 style="margin-top:28px">Research experience</h2>
    <div class="timeline">
      <div class="item"><div class="when">Sept 2026 – present</div><div class="what">Postdoctoral researcher · LRESE, EPFL</div><div>Multiphysics modelling towards efficiency and stability improvement of gas-fed CO<sub>2</sub> electrolysis (Prof. Sophia Haussener).</div></div>
      <div class="item"><div class="when">June 2021 – Aug 2026</div><div class="what">Doctoral assistant · LRESE, EPFL</div><div>Quantitative assessment of transport limitations in CO<sub>2</sub> electrolyser systems (Prof. Sophia Haussener).</div></div>
      <div class="item"><div class="when">Jan – June 2020</div><div class="what">Research assistant · IIT Delhi</div><div>Reduced-order state-of-charge model for Li-ion cells, Thermofluids &amp; Energy Systems Lab.</div></div>
      <div class="item"><div class="when">May 2018 – Nov 2019</div><div class="what">M.S. research scholar · IIT Delhi</div><div>Parallel lattice Boltzmann solver for microfluidic droplet flows.</div></div>
    </div>
    <h2>Education</h2>
    <div class="timeline">
      <div class="item"><div class="when">2021 – 2026</div><div class="what">Ph.D. Energy Sciences · EPFL, Lausanne</div></div>
      <div class="item"><div class="when">2018 – 2019</div><div class="what">M.S. (R) Thermal Engineering · IIT Delhi</div><div>GPA 10/10, Gold Medal</div></div>
      <div class="item"><div class="when">2013 – 2017</div><div class="what">B.Tech. Mechanical Engineering · IIT Gandhinagar</div><div>GPA 8.8/10</div></div>
    </div>
    <h2>Awards</h2>
    <div class="timeline">
      <div class="item"><div class="when">2021</div><div class="what">EPFLglobaLeaders doctoral fellowship</div><div>Marie Skłodowska-Curie, Horizon 2020</div></div>
      <div class="item"><div class="when">2020</div><div class="what">Gold Medal, M.S. Thermal Engineering, IIT Delhi</div></div>
      <div class="item"><div class="when">2017</div><div class="what">Best poster award, IIT Kanpur</div></div>
    </div>
    <h2>Skills</h2>
    <p class="muted" style="margin:6px 0 0">Modelling</p>
    <div class="skill-list"><span>Coupled nonlinear transport</span><span>Porous electrodes</span><span>Ion-exchange &amp; bipolar membranes</span><span>Transient &amp; degradation models</span><span>Parameter calibration</span><span>Sensitivity analysis</span></div>
    <p class="muted" style="margin:16px 0 0">Programming &amp; tools</p>
    <div class="skill-list"><span>Python</span><span>C/C++ &amp; MPI</span><span>Fortran</span><span>MATLAB</span><span>COMSOL Multiphysics</span><span>Ansys Fluent</span></div>""")

page("contact.html", "Contact | Venu Gopal Agarwal", """    <h1 class="page">Contact</h1>
    <div class="cards" style="margin-top:24px">
      <div class="card"><div class="icon">✉️</div><h3>Email</h3><p><a href="mailto:venu.agarwal@epfl.ch">venu.agarwal@epfl.ch</a> (EPFL)<br><a href="mailto:13agarwalvenu@gmail.com">13agarwalvenu@gmail.com</a></p></div>
      <div class="card"><div class="icon">🏛️</div><h3>Office</h3><p>Laboratory of Renewable Energy Science and Engineering (LRESE)<br>EPFL, 1015 Lausanne, Switzerland</p></div>
      <div class="card"><div class="icon">🔗</div><h3>Profiles</h3><p><a href="https://scholar.google.com/citations?user=9_OIf0YAAAAJ">Google Scholar</a><br><a href="https://orcid.org/0000-0003-2992-6539">ORCID 0000-0003-2992-6539</a><br><a href="https://www.linkedin.com/in/venu-agarwal-phd-08076a191/">LinkedIn</a><br><a href="https://people.epfl.ch/venu.agarwal">EPFL people page</a></p></div>
    </div>""")

page("404.html", "Page not found | Venu Gopal Agarwal", """    <h1 class="page">Page not found</h1>
    <p class="lead">That page doesn't exist (or has moved).</p>
    <p><a class="btn primary" href="/index.html">Home</a> <a class="btn" href="/research/index.html">Research</a></p>""")

PAGES = ["", "research/index.html"] + ["research/" + p[0] for p in PROJECTS] + ["research/gde-explorer.html", "publications.html", "cv.html", "contact.html"]
NL = chr(10)
open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(
    '<?xml version="1.0" encoding="UTF-8"?>' + NL + '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + NL
    + "".join(f"  <url><loc>https://venuagarwal.com/{p}</loc></url>" + NL for p in PAGES) + "</urlset>" + NL)
open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8").write(
    "User-agent: *" + NL + "Allow: /" + NL + "Sitemap: https://venuagarwal.com/sitemap.xml" + NL)

# the old Skills page is merged into the CV
old = os.path.join(ROOT, "skills.html")
if os.path.exists(old):
    os.remove(old)
print("built")
