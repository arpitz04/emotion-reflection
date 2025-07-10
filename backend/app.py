from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

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
    app.run(port=5000)
