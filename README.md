# 🎮 Auracelle Charlie 3 — AI Governance War Gaming Simulation
### NATO Demonstration Build | Auracelle AI Governance Labs

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.35+-red.svg)](https://streamlit.io/)
[![E-AGPO-HT Framework](https://img.shields.io/badge/framework-E--AGPO--HT-purple.svg)](#framework)
[![License: Proprietary](https://img.shields.io/badge/license-Proprietary-orange.svg)](LICENSE)

---

## Overview

**Auracelle Charlie 3** is a multi-actor AI governance policy stress-testing war gaming simulation built on the proprietary **Evans AI Governance Policy Optimization — Hierarchical Theory (E-AGPO-HT)** framework. This build is configured for NATO demonstration and institutional stakeholder engagement.

The platform enables policymakers, researchers, and governance professionals to:
- **Stress-test** AI governance policies across 20+ country actors and international organizations
- **Visualize** multi-dimensional influence dynamics via a real-time 3D AlphaFold-style influence map
- **Adjudicate** multi-actor negotiations using an AI agentic referee with deception detection
- **Integrate** live real-world data (World Bank, US Export Controls / CSL, SIPRI) into simulation rounds
- **Red-team** actor cognition via belief-distortion stress moves (Narrative Entrenchment, Epistemic Distrust, Horizon Collapse, etc.)

---

## E-AGPO-HT Framework

This simulation operationalizes the **Evans AI Governance Policy Optimization — Hierarchical Theory**, a three-stratum wargaming intelligence architecture:

| Stratum | Construct | Description |
|---------|-----------|-------------|
| **III** | **g-GWC** | General Governance Wargaming Capacity — overall wargaming capability |
| **II** | **7 BGC** | Broad Governance Capabilities: STI, SAD, ESI, NDM, SRA, IIC, ASI |
| **II** | **4 ACC AI Factors** | AI-Acceleration Capacity factors |
| **I** | **~40 NOF** | Narrow Operational Factors — measurable sub-factors per BGC |

### BGC Definitions

| Code | Full Name | Key Sub-factors |
|------|-----------|-----------------|
| **STI** | Strategic Threat Intelligence | PIP, GRD, APM, TLA, PDI, AIP |
| **SAD** | Security Architecture Design | TPD, MPM, NBE, DCF, CNS |
| **ESI** | Exploratory Simulation Intelligence | DRS, CD, WIS, TRS, AGM, DBP |
| **NDM** | Negotiation Dynamics Modeling | ABN, MTD, TMA, CFD, CMD, MCC |
| **SRA** | Strategic Rationality Assessment | TAC, RLA, TPI, PRM, LTR |
| **IIC** | Institutional Implementation Capacity | BTA, AMD, CTM, ELC, NES |
| **ASI** | Adaptive Scalability Intelligence | CGA, RAC, VMD, KCS, FLI, CLP |

---

## Application Architecture

```
auracelle-charlie-3/
├── app.py                              # Login / entry point (Streamlit)
├── adjudicator.py                      # AI Agentic Adjudicator module
├── simulation_vertical.html            # Main war game simulation UI (HTML/JS)
│
├── pages/
│   ├── 2_Simulation.py                 # Simulation host page
│   ├── 3_Red_Team_Module.py            # Red Team belief-distortion module
│   ├── 20_3D_Influence_Map.py          # 3D AlphaFold-style influence map
│   ├── 21_Real_World_Data_Metrics.py   # World Bank + Export Controls dashboard
│   ├── 90_Agentic_AI_Demo.py           # Autonomous negotiation agent demo
│   └── 91_INSTRUCTIONS_and_COGNITIVE_SCIENCE_MECHANICS.py
│
├── agpo_data/
│   ├── __init__.py                     # Package init
│   ├── worldbank.py                    # World Bank API integration (wbgapi)
│   ├── exportcontrol.py                # US Consolidated Screening List (CSL)
│   ├── sipri.py                        # SIPRI military expenditure parser
│   └── actor_map.py                    # Actor → ISO3 / M49 / Comtrade mappings
│
├── auracelle_agent_adapter.py          # Agentic simulation adapter
├── auracelle_agentic_upgrades.py       # Autonomous negotiation agents (linear Q)
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## Pages & Modules

### 🔐 Login (`app.py`)
Secure entry point with session-state authentication. Displays platform capabilities before login.

### 🎮 Simulation (`pages/2_Simulation.py`)
Full war gaming interface served as a self-contained HTML/JS application:
- **Policy Scenario Selector**: EU AI Act, US Executive Order, UK Pro-Innovation, China CAC, OECD Principles, Bletchley Declaration
- **Country/Actor Selector**: 20 actors including US, EU, China, UK, Japan, India, Brazil, NATO, Dubai, and more
- **Role Assignment**: Governance, Military AI, Data Privacy, Export Control, Diplomacy, Standard Setting, Surveillance, Trade, Tech Alliance
- **Round Engine**: Configurable episode length (1–30 rounds), stochastic/deterministic mode
- **AI Agentic Adjudicator**: Tension index, confidence score, alignment tracking
- **Deception Detection**: Consistency scoring per actor
- **External Shock System**: Probabilistic injection of geopolitical shocks
- **Round History Timeline**: Narrative trace per round

### 🛡️ Red Team Module (`pages/3_Red_Team_Module.py`)
Foresight cognition and belief distortion stress-testing:

| Move | Effect |
|------|--------|
| Narrative Entrenchment | Increases Pi (narrative lock-in) |
| Epistemic Distrust | Reduces Omega (update openness) |
| Horizon Collapse | Reduces H (planning horizon depth) |
| Panic Amplification | Reduces Lambda (uncertainty tolerance) |
| Metric Spoofing | Distorts mu (expected outcome signal) |
| Frame Flip | Inverts Omega for one step |

Cognition state variables: **H** (horizon), **Omega** (openness), **Lambda** (uncertainty tolerance), **Pi** (narrative lock-in)
Derived metric: **USI** (Update Suppression Index) = 1 − alpha = 1 − (Omega × (1 − Pi))

### 🧬 3D Influence Map (`pages/20_3D_Influence_Map.py`)
Interactive Three.js 3D visualization:
- **25 country/organization nodes** positioned in 3D by GDP (X), influence score (Y), policy alignment (Z)
- **7 policy pressure arrow sets**: GDPR, US Export Controls, Belt & Road, AUKUS, UN Ethics, NATO Expansion, Conflict Zone
- **6 cultural force spheres**: Democratic Norms, Tech Nationalism, Post-Colonial Sovereignty, Energy Wealth, Military-Tech Integration, NeutralHub
- **Live stress-test overlay**: Real-time actor pulsing, tension/reward metrics, round ticker
- **Country Focus drill-down**: Full pressure/force breakdown per node
- **Controls**: Maximize/restore, sidebar collapse, rotate/zoom, animation playback

### 🌍 Real-World Data Metrics (`pages/21_Real_World_Data_Metrics.py`)
Live economic intelligence dashboard:
- **World Bank API**: GDP, military expenditure (% GDP), internet penetration — latest available year
- **US Export Controls / BIS Entity List**: Screening for major actors
- **Sanctions regimes**: Reference to OFAC, EU, UN, and UK FCDO APIs
- **Batch Evaluation**: Hook point for scenario comparison runs

### 🤖 Agentic AI Demo (`pages/90_Agentic_AI_Demo.py`)
Self-contained autonomous negotiation demonstration:
- Lightweight multi-actor environment (US, EU, China)
- Linear Q-approximator agents with opponent stance classification
- Conciliatory / Neutral / Hardline stance inference
- Step-by-step trace with systemic risk score

---

## Data Sources

| Source | Integration | Update Frequency |
|--------|-------------|------------------|
| World Bank (wbgapi) | Automatic API | Cached 1 hour (TTL=3600) |
| US Consolidated Screening List (trade.gov) | Automatic API | Cached 24 hours (TTL=86400) |
| SIPRI Military Expenditure | CSV upload (manual) | Annual |
| UN Comtrade | API key required | On-demand |

---

## Setup & Deployment

### Local Development

```bash
# 1. Clone repository
git clone https://github.com/[your-org]/auracelle-charlie-3.git
cd auracelle-charlie-3

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
cp .env.example .env
# Edit .env with your API keys

# 5. Run
streamlit run app.py
```

### Google Colab Deployment (ngrok)

Use the provided Jupyter notebook (`AURACELLE_CHARLIE_3.ipynb`). The notebook:
1. Installs all dependencies
2. Writes all application files to the Colab filesystem
3. Launches Streamlit on port 8501
4. Opens a public ngrok tunnel (reserved domain: `aiwargame.ngrok.app`)

**Access**: `https://aiwargame.ngrok.app` | **Password**: `charlie2025`

### Environment Variables

| Variable | Description |
|----------|-------------|
| `NGROK_AUTHTOKEN` | ngrok authentication token |
| `COMTRADE_SUBSCRIPTION_KEY` | UN Comtrade API subscription key |
| `TRADEGOV_API_KEY` | trade.gov API key for CSL |
| `X_BEARER_TOKEN` | Twitter/X API bearer token (optional) |

---

## Requirements

```
streamlit>=1.35.0
plotly>=5.18.0
networkx>=3.2
numpy>=1.26.0
pandas>=2.1.0
torch>=2.1.0
wbgapi>=1.0.12
requests>=2.31.0
scikit-learn>=1.3.0
pyngrok==7.2.1
pyvis>=0.3.2
geopandas>=0.14.0
folium>=0.15.0
shapely>=2.0.0
```

---

## Security Notes

- **Authentication**: Session-state password protection on all pages
- **API Keys**: Never commit keys to version control — use `.env` or Colab secrets
- **ngrok Token**: Rotate regularly; do not share publicly
- **Data**: No PII is collected or stored by the simulation

---

## Proprietary Notice

The **E-AGPO-HT framework**, **Bach/Mozart/Delphi simulation architecture**, and all associated mathematical formulations are the proprietary intellectual property of **Grace Evans / Auracelle AI Governance Labs**. See [LICENSE](LICENSE) for terms.

---

## Citation

> Evans, G. (2025). *Auracelle Charlie 3: AI Governance War Gaming Stress-Testing Policy Simulation*. Auracelle AI Governance Labs. PhD Candidate, AI Governance Policy Optimization, Bath Spa University.

---

## Contact

**Dr. Grace Evans**
Director & Principal Investigator, Auracelle AI Governance Labs
Non-Resident Senior Fellow, UC Berkeley Center for Long-Term Cybersecurity
PhD Candidate, AI Governance Policy Optimization, Bath Spa University

---

*Built for NATO demonstration | February 2026*
