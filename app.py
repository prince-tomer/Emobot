from flask import Flask, render_template, request
import json

app = Flask(__name__)
chat_log = []

# Load main logic
with open("logic.json", encoding="utf-8") as f:
    logic = json.load(f)


# Synonym groups
synonym_map = {
    "i feel low": ["i feel down", "feeling sad", "not feeling good", "i'm low"],
    "i'm okay": ["i'm fine", "meh", "so-so", "i guess i'm fine"],
    "hello": ["hi", "hey", "yo", "what's up"],
    "bye": ["goodbye", "see ya", "talk later", "bye bye"],
    "thank you": ["thanks", "thank u", "thx", "much appreciated"],
    "i'm anxious": ["i'm nervous", "i feel tense", "feeling anxious"],
    "i feel tired": ["i'm exhausted", "i feel sleepy", "so tired"],
    "i'm happy": ["i feel great", "i'm joyful", "feeling good"],
    "i'm angry": ["i'm mad", "i'm pissed", "i'm furious"]
}

def get_response(user_input):
    user_input = user_input.lower().strip()

    # Direct match
    if user_input in logic:
        return logic[user_input]

    # Synonym match
    for key, synonyms in synonym_map.items():
        for phrase in synonyms:
            if phrase in user_input:
                return logic.get(key)

    # Default fallback
    return logic.get("default", "🤝 I'm listening. Just type anything that's on your mind.")

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", chat_log=chat_log)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form["message"]
    bot_response = get_response(user_input)
    chat_log.append({"sender": "You", "message": user_input})
    chat_log.append({"sender": "EmoBot", "message": bot_response})
    return render_template("index.html", chat_log=chat_log)

if __name__ == "__main__":
    app.run(debug=True)
