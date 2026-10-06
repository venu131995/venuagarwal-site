"""Builds the static site: python build.py  (writes the .html files next to this script)."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
NAV = [("Home", "index.html"), ("Research", "research/index.html"), ("Publications", "publications.html"),
       ("Skills", "skills.html"), ("CV", "cv.html"), ("Contact", "contact.html")]


def page(path, title, body, desc="Venu Gopal Agarwal — computational researcher in electrochemical energy conversion at EPFL."):
    depth = path.count("/")
    up = "../" * depth
    nav = "\n".join(
        f'      <a{" class=\"active\"" if href == path else ""} href="{up}{href}">{name}</a>' for name, href in NAV)
    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="stylesheet" href="{up}assets/css/style.css">
</head>
<body>
<header class="site">
  <div class="wrap">
    <a class="name" href="{up}index.html">Venu Gopal Agarwal</a>
    <nav>
{nav}
    </nav>
  </div>
</header>
<main>
  <div class="wrap">
{body.replace('{up}', up)}
  </div>
</main>
<footer>
  <div class="wrap">© 2026 Venu Gopal Agarwal · Laboratory of Renewable Energy Science and Engineering, EPFL</div>
</footer>
</body>
</html>
"""
    out = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write(html)


PROJECTS = [
    ("crutches.html", "Flooding and salt in zero-gap CO<sub>2</sub> electrolysers", "Postdoc, 2026 – present", "in progress",
     "Zero-gap membrane electrode assemblies reach industrial current densities, but their cathodes flood and fill with (bi)carbonate salt within hundreds of hours.",
     ["A full-cell, multiphysics model of a CO<sub>2</sub>-to-CO membrane electrode assembly: species, charge, water and heat transport across the gas diffusion layer, microporous layer, catalyst layer, membrane and anode.",
      "Liquid water in every porous layer with pore-size-based capillary curves and potential-dependent electrowetting.",
      "Precipitated salt treated as a solid phase that changes porosity, permeability, active area and wettability, followed in time.",
      "Calibrated on a Ag/Cs<sup>+</sup> cell; used to compare mitigation strategies such as pulsed operation and thermal gradients over the time scale on which they act."],
     "Supervisor: Prof. Sophia Haussener."),
    ("bicarbonate.html", "Bicarbonate-fed bipolar-membrane electrolysers", "PhD, 2021 – 2026", "manuscript in preparation",
     "Bicarbonate electrolysers convert captured carbon directly, without regenerating and compressing CO<sub>2</sub> gas: protons from a bipolar membrane release CO<sub>2</sub> in the catalyst layer, where it is reduced to CO.",
     ["Coupled the gas-diffusion-electrode and bipolar-membrane models into one integrated electrolyser model linking electrochemistry, ion transport and water management.",
      "Validated against measured CO faradaic efficiencies.",
      "Used the model to evaluate catalyst-layer, substrate and membrane designs."],
     "Supervisor: Prof. Sophia Haussener."),
    ("bpm.html", "Bipolar membrane modelling", "PhD, 2021 – 2026", "in preparation",
     "Bipolar membranes split water at the junction between a cation- and an anion-exchange layer, driven by strong local electric fields.",
     ["One-dimensional Poisson–Nernst–Planck model with electric-field-enhanced (second Wien effect) water dissociation.",
      "Hydration-dependent transport and membrane water balance.",
      "Parametric and sensitivity studies to isolate rate-limiting transport mechanisms and guide membrane design."],
     "Supervisor: Prof. Sophia Haussener."),
    ("microfluidic-gde.html", "Mass-transport limits in a microfluidic GDE electrolyser", "PhD", "Communications Chemistry, 2024",
     "Gas diffusion electrodes deliver CO<sub>2</sub> to the catalyst in the gas phase, but performance is still set by how fast reactants and products move through the porous layers and electrolyte.",
     ["Two-dimensional model of a gas-diffusion cathode in a microfluidic flow cell, resolving coupled charge, species and momentum transport.",
      "Validated against experimental data.",
      "Quantified which transport processes limit performance and where."],
     'V. G. Agarwal, S. Haussener, <a href="https://doi.org/10.1038/s42004-024-01122-5">Communications Chemistry 7, 47 (2024)</a>.'),
    ("buffer-dissociation.html", "Field-enhanced dissociation of buffer species", "Collaboration", "ACS Electrochemistry, 2025",
     "Strong interfacial electric fields can accelerate the dissociation of protonated buffer species, changing the local pH near electrodes and membranes.",
     ["Numerical analysis of field-enhanced homogeneous dissociation of protonated buffer species."],
     'M. Wada, K. Obata, V. G. Agarwal, F. Lorenzutti, S. Haussener, K. Takanabe, <a href="https://doi.org/10.1021/acselectrochem.5c00299">ACS Electrochemistry (2025)</a>.'),
    ("droplets-lbm.html", "Droplet formation in microfluidic T-junctions", "M.S. (R), IIT Delhi, 2018 – 2019", "Physical Review Fluids, 2020",
     "How droplets form and how the flow regime changes in a T-shaped microfluidic device.",
     ["Parallel (MPI) lattice Boltzmann solver written from scratch in C/C++.",
      "Validated against in-house experiments."],
     'V. G. Agarwal, R. Singh, S. S. Bagha, A. Gupta, <a href="https://doi.org/10.1103/PhysRevFluids.5.044203">Physical Review Fluids 5, 044203 (2020)</a>.'),
    ("battery-rom.html", "Real-time state of charge of Li-ion cells", "Research assistant, IIT Delhi, 2020", "",
     "Battery management systems need fast, accurate state-of-charge estimates.",
     ["Data-driven, control-oriented reduced-order model (discrete-time realisation algorithm) for a Li-ion cell.",
      "Accurate state-of-charge estimation across standard drive cycles."],
     "Thermofluids &amp; Energy Systems Lab, IIT Delhi."),
]

for fn, title, period, tag, intro, points, foot in PROJECTS:
    lis = "\n".join(f"      <li>{p}</li>" for p in points)
    tagh = f'<span class="tag">{tag}</span>' if tag else ""
    page("research/" + fn, f"{title.replace('<sub>2</sub>', '2')} | Venu Gopal Agarwal", f"""    <p class="kicker"><a href="index.html">Research</a> · {period}</p>
    <h1>{title}</h1>
    {tagh}
    <p class="lead">{intro}</p>
    <h2>What I did</h2>
    <ul>
{lis}
    </ul>
    <p class="muted">{foot}</p>""")

def card(fn, t, tag, intro):
    short = intro[:150].rsplit(" ", 1)[0] + "…"
    tagh = '<span class="tag">' + tag + '</span>' if tag else ""
    return (f'      <a class="card" href="{{up}}research/{fn}">\n        <h3>{t}</h3>\n        <p>{short}</p>\n'
            f'        {tagh}\n      </a>')


cards = "\n".join(card(fn, t, tag, intro) for fn, t, per, tag, intro, pts, foot in PROJECTS)

page("research/index.html", "Research | Venu Gopal Agarwal", f"""    <h1>Research</h1>
    <p class="lead">I develop physics-based models of electrochemical energy-conversion devices — coupled, nonlinear transport of charge, species, water, heat and momentum — and validate them against experiments to find what limits performance and lifetime.</p>
    <div class="cards">
{cards}
    </div>""")

HOME_CARDS = chr(10).join(card(fn, t, tag, intro) for fn, t, per, tag, intro, pts, foot in PROJECTS[:4])
IMG = '      <img src="{up}assets/img/profile.jpg" alt="Portrait of Venu Gopal Agarwal">' if os.path.exists(os.path.join(ROOT, "assets/img/profile.jpg")) else ""
page("index.html", "Venu Gopal Agarwal", f"""    <section class="hero">
{IMG}
      <div>
        <h1>Venu Gopal Agarwal</h1>
        <p class="role">Postdoctoral researcher · Laboratory of Renewable Energy Science and Engineering (LRESE), EPFL</p>
        <p>I build multiphysics models of electrochemical energy-conversion devices — CO<sub>2</sub> electrolysers, bipolar membranes and gas diffusion electrodes — that resolve coupled transport of charge, species, water, heat and momentum, and I validate them against experiments to find what limits efficiency and stability.</p>
        <p>PhD in Energy Sciences, EPFL (2026) · M.S. (R) Thermal Engineering, IIT Delhi (Gold Medal) · B.Tech. Mechanical Engineering, IIT Gandhinagar.</p>
        <p class="links">
          <a href="https://www.epfl.ch/labs/lrese/">LRESE, EPFL</a>
          <a href="{{up}}publications.html">Publications</a>
          <a href="{{up}}cv.html">CV</a>
        </p>
      </div>
    </section>
    <h2>Research highlights</h2>
    <div class="cards">
{HOME_CARDS}
    </div>""")

page("publications.html", "Publications | Venu Gopal Agarwal", """    <h1>Publications</h1>
    <ol class="pubs" reversed>
      <li>M. Wada, K. Obata, <b>V. G. Agarwal</b>, F. Lorenzutti, S. Haussener, K. Takanabe. Numerical analysis on field-enhanced homogeneous dissociation of protonated buffer species. <i>ACS Electrochemistry</i> (2025). <a href="https://doi.org/10.1021/acselectrochem.5c00299">doi:10.1021/acselectrochem.5c00299</a></li>
      <li><b>V. G. Agarwal</b>, S. Haussener. Quantifying mass transport limitations in a microfluidic CO<sub>2</sub> electrolyzer with a gas diffusion cathode. <i>Communications Chemistry</i> 7, 47 (2024). <a href="https://doi.org/10.1038/s42004-024-01122-5">doi:10.1038/s42004-024-01122-5</a></li>
      <li><b>V. G. Agarwal</b>, R. Singh, S. S. Bagha, A. Gupta. Dynamics of droplet formation and flow regime transition in a T-shaped microfluidic device. <i>Physical Review Fluids</i> 5, 044203 (2020). <a href="https://doi.org/10.1103/PhysRevFluids.5.044203">doi:10.1103/PhysRevFluids.5.044203</a></li>
    </ol>
    <h2>In preparation</h2>
    <ul>
      <li>Design and optimization of bicarbonate-fed CO<sub>2</sub>-to-CO electrolysers.</li>
      <li>Modelling of bipolar membranes with field-enhanced water dissociation.</li>
      <li>Mechanisms and mitigation of flooding- and salt-driven degradation in zero-gap CO<sub>2</sub> electrolysers.</li>
    </ul>
    <h2>Talks</h2>
    <p>Five conference presentations, including an invited talk at the 2024 meeting of the Electrochemical Society (ECS). Best poster award, IIT Kanpur, 2017.</p>""")

page("skills.html", "Skills | Venu Gopal Agarwal", """    <h1>Skills</h1>
    <div class="cards">
      <div class="card"><h3>Modelling</h3><p>Coupled nonlinear transport (charge, species, water, heat, momentum); porous electrodes; ion-exchange and bipolar membranes; transient and degradation models; parameter calibration against noisy data; sensitivity and scenario analysis.</p></div>
      <div class="card"><h3>Numerics &amp; programming</h3><p>Python, C/C++ (including a parallel MPI lattice Boltzmann solver written from scratch), Fortran, MATLAB.</p></div>
      <div class="card"><h3>Tools</h3><p>COMSOL Multiphysics, Ansys Fluent, AI-assisted research and coding workflows.</p></div>
    </div>""")

page("cv.html", "CV | Venu Gopal Agarwal", """    <h1>Curriculum vitae</h1>
    <h2>Research experience</h2>
    <dl class="cv">
      <dt>Sept 2026 – present</dt><dd><b>Postdoctoral researcher</b>, LRESE, EPFL — multiphysics modelling towards efficiency and stability improvement of gas-fed CO<sub>2</sub> electrolysis (Prof. Sophia Haussener).</dd>
      <dt>June 2021 – Aug 2026</dt><dd><b>Doctoral assistant</b>, LRESE, EPFL — quantitative assessment of transport limitations in CO<sub>2</sub> electrolyser systems (Prof. Sophia Haussener).</dd>
      <dt>Jan – June 2020</dt><dd><b>Research assistant</b>, Thermofluids &amp; Energy Systems Lab, IIT Delhi — reduced-order state-of-charge model for Li-ion cells.</dd>
      <dt>May 2018 – Nov 2019</dt><dd><b>M.S. research scholar</b>, Dept. of Mechanical Engineering, IIT Delhi — parallel lattice Boltzmann solver for microfluidic droplet flows.</dd>
    </dl>
    <h2>Education</h2>
    <dl class="cv">
      <dt>2021 – 2026</dt><dd><b>Ph.D. Energy Sciences</b>, EPFL, Lausanne</dd>
      <dt>2018 – 2019</dt><dd><b>M.S. (R) Thermal Engineering</b>, IIT Delhi — GPA 10/10, Gold Medal</dd>
      <dt>2013 – 2017</dt><dd><b>B.Tech. Mechanical Engineering</b>, IIT Gandhinagar — GPA 8.8/10</dd>
    </dl>
    <h2>Awards</h2>
    <ul>
      <li>EPFLglobaLeaders doctoral fellowship (Marie Skłodowska-Curie, Horizon 2020), 2021.</li>
      <li>Gold Medal, M.S. Thermal Engineering, IIT Delhi, 2020.</li>
      <li>Best poster award, IIT Kanpur, 2017.</li>
    </ul>""")

page("contact.html", "Contact | Venu Gopal Agarwal", """    <h1>Contact</h1>
    <p>Laboratory of Renewable Energy Science and Engineering (LRESE)<br>École Polytechnique Fédérale de Lausanne (EPFL)<br>1015 Lausanne, Switzerland</p>
    <p>Email: <a href="mailto:13agarwalvenu@gmail.com">13agarwalvenu@gmail.com</a></p>""")
print("built")
