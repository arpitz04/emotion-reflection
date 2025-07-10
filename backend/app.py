from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# New route for root
@app.route('/')
def index():
    return "Emotion Reflection Tool backend is running!"

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text', '').lower()

    if "happy" in text or "excited" in text:
        emotion = "Happy"
        confidence = 0.92
    elif "sad" in text or "down" in text:
        emotion = "Sad"
        confidence = 0.88
    elif "nervous" in text or "worried" in text:
        emotion = "Anxious"
        confidence = 0.85
    elif "angry" in text or "frustrated" in text:
        emotion = "Angry"
        confidence = 0.87
    else:
        emotion = "Neutral"
        confidence = 0.70

    return jsonify({
        "emotion": emotion,
        "confidence": confidence
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
