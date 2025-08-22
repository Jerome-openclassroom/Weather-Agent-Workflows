# Workflows d’Agents Météo 🌦️🤖

[![Made with n8n](https://img.shields.io/badge/Fabriqué%20avec-n8n-1abc9c?logo=n8n&logoColor=white)](https://n8n.io)  [![OpenAI](https://img.shields.io/badge/OpenAI-Assistant%20%26%20Code%20Interpreter-412991?logo=openai)](https://platform.openai.com/)  [![License: MIT](https://img.shields.io/badge/Licence-MIT-blue.svg)](LICENSE)  


🚀 Ce dépôt compare deux implémentations de chatbots météo dans **n8n** :  
- avec le **nœud Agent IA**  (implémentation agentique native de n8n)  
- avec un **Assistant OpenAI et Code Interpreter**  (Assistant OpenAI intégré via n8n)

Inclut des calculs déterministes d’**Humidex** et de **Windchill**, une **intégration Google Sheets**, et l’**envoi de bulletins météo par email**.  

Chaque section ci-dessous est rédigée comme un mini README autonome.
---

## 1. Workflow avec le nœud Agent IA

### Présentation
Ce workflow utilise le **nœud Agent IA** de n8n. L’agent a accès à plusieurs outils :
- **Weather API** (conditions météo en temps réel)  
- **Google Sheets** (ajout des données météo)  
- **Gmail** (envoi d’un bulletin météo par email)  
- **Interface HTML/JS** (chatbot simple dans un navigateur)  

L’agent est guidé par un **prompt système** et conserve une mémoire à court terme.

### Fonctionnalités
- Interaction utilisateur via un chatbot navigateur (`n8n.htm`).  
- L’agent récupère la météo en temps réel pour une ville donnée.  
- Les résultats sont enregistrés dans Google Sheets.  
- L’agent peut envoyer un rapport météo par email.  
- Les valeurs d’Humidex et de Windchill sont *estimées par le LLM* en utilisant ses poids.  

### Limites
- Le nœud Agent IA **ignore parfois les consignes** et calcule lui-même au lieu d’utiliser des formules déterministes.  
- Les sorties JSON peuvent être incohérentes et difficiles à mapper.  
- L’Humidex et le Windchill ne sont **pas garantis déterministes** dans ce workflow.  

### Fichiers (Workflow_Agent/)
- `browser_chatbot.png` → Capture d’écran du chatbot navigateur  
- `Google_Sheet.png` → Données enregistrées dans Google Sheets  
- `meteo_report.png` → Exemple de bulletin météo envoyé par email  
- `n8n.htm` → Interface HTML/JS du chatbot  
- `System_prompt.txt` → Prompt système du nœud Agent IA  
- `Workflow_agent.json` → Blueprint du workflow (pour reproduction dans n8n)  
- `Workflow.png` → Capture d’écran du workflow dans n8n  

---

## 2. Workflow avec Assistant + Code Interpreter

### Présentation
Ce workflow remplace le nœud Agent IA par un **nœud “Message an Assistant”**, relié à un **Assistant OpenAI**.  
L’assistant utilise l’outil **Code Interpreter** et des scripts Python déterministes pour les calculs météo.

### Fonctionnalités
- Calcul déterministe de l’**Humidex** et du **Windchill** via les formules officielles :
  - `humidex_calc_simple.py`  
  - `windchill_calc_simple.py`  
- L’assistant récupère les données depuis Google Sheets et Weather API.  
- Les réponses incluent **les étapes de calcul détaillées** avec les variables utilisées.  
- Sorties JSON stables, directement exploitables dans n8n.  
- Conversations de démonstration incluses (`Demo_calculs.md`).  

### Avantages
- **Déterminisme** : le LLM n’utilise pas ses poids pour estimer l’Humidex ou le Windchill mais exécute le code Python fourni.  
- **Explicabilité** : les réponses incluent variables et étapes intermédiaires.  
- **Reproductibilité** : les workflows peuvent être importés directement grâce aux blueprints JSON.  

### Fichiers (Workflow_Assistant/)
- `Demo_calculs.md` → Exemple de conversation (questions/réponses météo)  
- `System_prompt.txt` → Prompt système du nœud “Message an Assistant”  
- `Workflow_assistant.json` → Blueprint du workflow (pour reproduction dans n8n)  
- `Workflow.png` → Capture d’écran du workflow dans n8n  
- `humidex_calc_simple.py` → Calcul déterministe de l’humidex (Python)  
- `windchill_calc_simple.py` → Calcul déterministe du windchill (Python)  

---

## Arborescence du dépôt

```
.
├── README.md                # Version anglaise
├── README_fr.md             # Version française (ce fichier)
├── Workflow_Agent/
│   ├── browser_chatbot.png
│   ├── Google_Sheet.png
│   ├── meteo_report.png
│   ├── n8n.htm
│   ├── System_prompt.txt
│   ├── Workflow_agent.json
│   └── Workflow.png
└── Workflow_Assistant/
    ├── Demo_calculs.md
    ├── System_prompt.txt
    ├── Workflow_assistant.json
    ├── Workflow.png
    ├── humidex_calc_simple.py
    └── windchill_calc_simple.py
```

---

## Conclusion

Ce dépôt illustre la différence entre deux approches de conception d’agents dans n8n :  

- **Nœud Agent IA** → flexible mais instable et non déterministe.  
- **Assistant avec Code Interpreter** → déterministe, explicable, mieux adapté aux cas nécessitant une reproductibilité.  

Les deux sont **des agents par définition** (mémoire, outils, raisonnement), même si un seul est nommé explicitement “Agent” dans n8n.  

---

*Ce travail a été développé dans le cadre d’un exercice d’autoformation (TP/TD) en IA appliquée et automatisation de workflows.  
Il démontre des compétences avancées en orchestration d’agents, calcul déterministe et intégration d’n8n avec la plateforme OpenAI.*
