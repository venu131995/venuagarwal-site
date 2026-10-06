"""Builds the static site: python build.py  (writes the .html files next to this script)."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
NAV = [("Home", "index.html"), ("Research", "research/index.html"), ("Publications", "publications.html"),
       ("CV", "cv.html"), ("Contact", "contact.html")]
DESC = "Venu Gopal Agarwal — computational researcher in electrochemical energy conversion at EPFL."


def page(path, title, body, desc=DESC, raw=False):
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
  <meta property="og:image" content="https://venuagarwal.com/assets/img/profile.jpg">
  <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%230e7490'/%3E%3Ctext x='32' y='42' font-family='Arial' font-size='26' font-weight='700' fill='white' text-anchor='middle'%3EVA%3C/text%3E%3C/svg%3E">
  <link rel="stylesheet" href="{up}assets/css/style.css">
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
  <div class="wrap"><span>© 2026 Venu Gopal Agarwal</span><span>LRESE · EPFL · Lausanne</span></div>
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
     "Supervisor: Prof. Sophia Haussener."),
    ("bpm.html", "⚡", "Bipolar membrane modelling", "PhD · 2021 – 2026", "in preparation",
     "Bipolar membranes split water at the junction between a cation- and an anion-exchange layer, driven by strong local electric fields.",
     ["One-dimensional Poisson–Nernst–Planck model with electric-field-enhanced (second Wien effect) water dissociation.",
      "Hydration-dependent transport and membrane water balance.",
      "Parametric and sensitivity studies to isolate rate-limiting transport mechanisms and guide membrane design."],
     "Supervisor: Prof. Sophia Haussener."),
    ("microfluidic-gde.html", "🔬", "Mass-transport limits in a microfluidic GDE electrolyser", "PhD", "Communications Chemistry · 2024",
     "Gas diffusion electrodes deliver CO<sub>2</sub> to the catalyst in the gas phase, but performance is still set by how fast reactants and products move through the porous layers and electrolyte.",
     ["Two-dimensional model of a gas-diffusion cathode in a microfluidic flow cell, resolving coupled charge, species and momentum transport.",
      "Validated against experimental data.",
      "Quantified which transport processes limit performance and where."],
     'V. G. Agarwal, S. Haussener, <a href="https://doi.org/10.1038/s42004-024-01122-5">Communications Chemistry 7, 47 (2024)</a> — open access.'),
    ("buffer-dissociation.html", "🧪", "Field-enhanced dissociation of buffer species", "Collaboration", "ACS Electrochemistry · 2025",
     "Strong interfacial electric fields can accelerate the dissociation of protonated buffer species, changing the local pH near electrodes and membranes.",
     ["Numerical analysis of field-enhanced homogeneous dissociation of protonated buffer species."],
     'M. Wada, K. Obata, V. G. Agarwal, F. Lorenzutti, S. Haussener, K. Takanabe, <a href="https://doi.org/10.1021/acselectrochem.5c00299">ACS Electrochemistry (2025)</a>.'),
    ("droplets-lbm.html", "💦", "Droplet formation in microfluidic T-junctions", "M.S. (R), IIT Delhi · 2018 – 2019", "Physical Review Fluids · 2020",
     "How droplets form and how the flow regime changes in a T-shaped microfluidic device.",
     ["Parallel (MPI) lattice Boltzmann solver written from scratch in C/C++.",
      "Validated against in-house experiments."],
     'V. G. Agarwal, R. Singh, S. S. Bagha, A. Gupta, <a href="https://doi.org/10.1103/PhysRevFluids.5.044203">Physical Review Fluids 5, 044203 (2020)</a>.'),
    ("battery-rom.html", "🔋", "Real-time state of charge of Li-ion cells", "Research assistant, IIT Delhi · 2020", "",
     "Battery management systems need fast, accurate state-of-charge estimates.",
     ["Data-driven, control-oriented reduced-order model (discrete-time realisation algorithm) for a Li-ion cell.",
      "Accurate state-of-charge estimation across standard drive cycles."],
     "Thermofluids &amp; Energy Systems Lab, IIT Delhi."),
]


def card(p):
    fn, icon, t, per, tag, intro, pts, foot = p
    short = intro if len(intro) < 160 else intro[:160].rsplit(" ", 1)[0] + "…"
    tagh = f'<span class="tag">{tag}</span>' if tag else '<span class="tag">' + per + '</span>'
    return (f'      <a class="card" href="{{up}}research/{fn}">\n        <div class="icon">{icon}</div>\n'
            f'        <h3>{t}</h3>\n        <p>{short}</p>\n        {tagh}\n      </a>')


for p in PROJECTS:
    fn, icon, title, period, tag, intro, points, foot = p
    lis = "\n".join(f"      <li>{x}</li>" for x in points)
    tagh = f'<span class="tag">{tag}</span>' if tag else ""
    page("research/" + fn, f"{title.replace('<sub>2</sub>', '2')} | Venu Gopal Agarwal", f"""    <div class="project-head">
      <p class="kicker"><a href="index.html">← Research</a> · {period}</p>
      <h1 class="page">{icon} {title}</h1>
      {tagh}
    </div>
    <div class="project-body">
      <p class="lead">{intro}</p>
      <h2>What I did</h2>
      <ul>
{lis}
      </ul>
      <div class="note">{foot}</div>
    </div>""")

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
            <a class="btn" href="{{up}}cv.html">CV</a>
          </div>
        </div>
        {portrait}
      </div>
      <div class="stats">
        <div class="stat"><b>PhD, EPFL</b><span>Energy Sciences, 2026</span></div>
        <div class="stat"><b>MSCA fellow</b><span>EPFLglobaLeaders, Horizon 2020</span></div>
        <div class="stat"><b>Gold Medal</b><span>M.S. (R), IIT Delhi</span></div>
        <div class="stat"><b>Invited talk</b><span>ECS meeting 2024</span></div>
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
     "<b>V. G. Agarwal</b>, R. Singh, S. S. Bagha, A. Gupta", "https://doi.org/10.1103/PhysRevFluids.5.044203"),
]
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
    <h2 style="margin-top:40px">Talks</h2>
    <p>Five conference presentations, including an invited talk at the 2024 meeting of the Electrochemical Society (ECS). Best poster award, IIT Kanpur, 2017.</p>""")

page("cv.html", "CV | Venu Gopal Agarwal", """    <h1 class="page">Curriculum vitae</h1>
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
      <div class="card"><div class="icon">✉️</div><h3>Email</h3><p><a href="mailto:13agarwalvenu@gmail.com">13agarwalvenu@gmail.com</a></p></div>
      <div class="card"><div class="icon">🏛️</div><h3>Office</h3><p>Laboratory of Renewable Energy Science and Engineering (LRESE)<br>EPFL, 1015 Lausanne, Switzerland</p></div>
      <div class="card"><div class="icon">🔗</div><h3>Profiles</h3><p><a href="https://people.epfl.ch/venu.agarwal">EPFL people page</a><br><a href="https://www.epfl.ch/labs/lrese/">LRESE lab</a></p></div>
    </div>""")

# the old Skills page is merged into the CV
old = os.path.join(ROOT, "skills.html")
if os.path.exists(old):
    os.remove(old)
print("built")
