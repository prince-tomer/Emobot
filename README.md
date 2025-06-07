# 🤖 EmoBot - A Rule-Based Emotional Chatbot

EmoBot is a lightweight, rule-based chatbot built using **Python + Flask**. It mimics a conversational assistant that responds to emotional cues, motivational questions, and daily small talk — no AI or deep learning required.

> 💡 Perfect for learning Flask, chatbot logic, JSON dialog flow, and deploying Python web apps.

---

## 📌 Features

- 🎭 Emotion-aware responses (e.g., “I feel sad” → motivational quotes)
- 🤝 Friendly conversation triggers (e.g., “What should I do?”, “I’m bored”)
- 💬 Synonym matching (e.g., “I’m okay”, “I’m fine”, “meh” → same response)
- 🎨 Simple web interface (HTML + CSS, no JavaScript required)
- 🌐 Ready for deployment on Replit, Render, or any Flask-supporting server

---

## 📂 Project Structure

emobot/
├── app.py # Main Flask app
├── logic.json # Dialog logic (intents, responses)
├── requirements.txt # Python dependencies
├── templates/
│ └── index.html # Chatbot frontend
└── static/
└── style.css # Basic UI styling
## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/emobot.git
cd emobot
2. Set Up a Virtual Environment (optional)
bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
3. Install Dependencies
bash
pip install -r requirements.txt
4. Run the App
bash
python app.py
Visit http://127.0.0.1:5000 in your browser.
