
# Emotion Reflection Tool

A simple full-stack web app that lets users enter short reflections (e.g., “I feel nervous about my interview”) and returns a mock emotion analysis like “Anxious” with confidence.

## Tech Stack
- Frontend: React + TypeScript
- Backend: Flask (Python)
- Communication: REST API via Axios

---

## How to Run the Project

1. **Clone the project** or unzip the folder.
2. **Open a terminal** and navigate to the root folder.

### Start the Backend (Flask)

```bash
cd backend
pip install -r requirements.txt
python app.py
```

> The backend runs on: `http://localhost:5000`

### Start the Frontend (React + TypeScript)

Open a new terminal tab/window:

```bash
cd frontend
npm install
npm start
```

> The frontend runs on: `http://localhost:3000`

---

## About `node_modules`

To keep the zipped project under 50 MB, the `node_modules` folder is excluded.  
After unzipping or cloning, simply run `npm install` inside the `frontend` folder to restore it.

---

## Example

**Input:**

```
I feel nervous about my first job interview
```

**Response:**

```json
{
  "emotion": "Anxious",
  "confidence": 0.85
}
```

---

##  Project Structure

```
emotion-reflection-tool/
├── backend/
│   ├── app.py
│   └── requirements.txt
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
└── README.md
```

---

## Contact

For any issues or questions, feel free to reach out!
