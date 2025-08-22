# Weather Agent Workflows 🌦️🤖

[![Made with n8n](https://img.shields.io/badge/Made%20with-n8n-1abc9c?logo=n8n&logoColor=white)](https://n8n.io)  [![OpenAI](https://img.shields.io/badge/OpenAI-Assistant%20&%20Code%20Interpreter-412991?logo=openai)](https://platform.openai.com/)  [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)  


🚀 This repository compares two implementations of weather chatbots in **n8n**:  
- Using the **AI Agent Node**  
- Using an **OpenAI Assistant with Code Interpreter**  

Includes deterministic **Humidex** and **Windchill** calculations, **Google Sheets integration**, and **email reporting**.  


Each section below is structured as a standalone README-style description.

> ⚠️ API keys and webhook URLs have been removed for security reasons. Please replace them with your own values in order to reproduce the workflows.

---

## 1. Workflow with AI Agent Node

### Overview
This workflow uses the native **AI Agent node** in n8n. The Agent can access multiple tools:
- **Weather API** (current weather conditions)
- **Google Sheets** (append weather data)
- **Gmail** (send weather reports)
- **HTML/JS interface** (simple browser chatbot)

The Agent is guided with a **system prompt** and maintains a short-term memory.

### Features
- User interacts through a browser chatbot (`n8n.htm`).
- Agent retrieves real-time weather for a city.
- Agent records results into Google Sheets.
- Agent can send a weather report by email.
- Humidex and Windchill values are *estimated by the LLM* using its weights.

### Limitations
- The AI Agent node sometimes **ignores instructions** and performs calculations directly instead of using deterministic formulas.
- JSON outputs may be inconsistent and difficult to map.
- Windchill and Humidex are **not guaranteed deterministic** in this workflow.

### Files (Workflow_Agent/)
- `browser_chatbot.png` → Screenshot of the chatbot in browser
- `Google_Sheet.png` → Data recorded in Google Sheets
- `meteo_report.png` → Example weather report sent by email
- `n8n.htm` → HTML/JS interface for the chatbot
- `System_prompt.txt` → System prompt for the Agent node in n8n
- `Workflow_agent.json` → Blueprint of the workflow for import in n8n
- `Workflow.png` → Screenshot of the n8n workflow

---

## 2. Workflow with Assistant + Code Interpreter

### Overview
This workflow replaces the AI Agent node with a **Message an Assistant node**, linked to an OpenAI **Assistant**.  
The Assistant uses the **Code Interpreter tool** and deterministic Python scripts for meteorological calculations.

### Features
- Deterministic computation of **Humidex** and **Windchill** using official formulas:
  - `humidex_calc_simple.py`
  - `windchill_calc_simple.py`
- Assistant retrieves data from Google Sheets and Weather API.
- Responses can include **step-by-step calculations** with variables shown (on demand).
- Possibility of stable JSON outputs, directly usable in n8n (via Model configuration → Response format in the OpenAI Platform interface).
- Demo conversations included (`Demo_calculs.md`).

### Advantages
- **Deterministic**: The LLM does not compute humidex/windchill with its weights, but calls the provided Python code.  
- **Explainable**: Outputs include intermediate variables and formulas.  
- **Reproducible**: Workflows can be imported directly via JSON blueprints.

### Files (Workflow_Assistant/)
- `Demo_calculs.md` → Example chat (Q&A with weather calculations)
- `System_prompt.txt` → System prompt for the "Message an Assistant" node
- `Workflow_assistant.json` → Blueprint of the workflow for import in n8n
- `Workflow.png` → Screenshot of the n8n workflow
- `humidex_calc_simple.py` → Deterministic humidex calculator (Python)
- `windchill_calc_simple.py` → Deterministic windchill calculator (Python)

---

## Repository Structure

```
.
├── README.md # English version (this file)
├── README_fr.md # French version
├── Workflow_Agent/
│ ├── browser_chatbot.png # Screenshot of the chatbot in browser
│ ├── Google_Sheet.png # Data recorded in Google Sheets
│ ├── meteo_report.png # Example weather report sent by email
│ ├── n8n.htm # HTML/JS interface for the chatbot
│ ├── System_prompt.txt # System prompt for the Agent node in n8n
│ ├── Workflow_agent.json # Workflow blueprint (import into n8n)
│ └── Workflow.png # Screenshot of the n8n workflow
└── Workflow_Assistant/
├── Demo_calculs.md # Example chat (Q&A with weather calculations)
├── System_prompt.txt # System prompt for the "Message an Assistant" node
├── Workflow_assistant.json # Workflow blueprint (import into n8n)
├── Workflow.png # Screenshot of the n8n workflow
├── humidex_calc_simple.py # Deterministic humidex calculator (Python)
└── windchill_calc_simple.py # Deterministic windchill calculator (Python)

```

---

## Conclusion

This repository illustrates the difference between two approaches to agent design in n8n:

- **AI Agent Node** → flexible but can be unstable and non-deterministic in extreme use case.  
- **Assistant with Code Interpreter** → deterministic, explainable, and better suited for tasks requiring reproducibility.  

Both are *agents by definition* (they combine memory, tools, and reasoning), even if only one is explicitly called an "Agent" in n8n.

---

*This work was developed as part of a self-training exercise (TP/TD) in applied AI and workflow automation. 
It demonstrates advanced skills in agent orchestration, deterministic computation, and integration of n8n with OpenAI’s platform.*
