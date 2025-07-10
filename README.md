Welcome to the "Emotion Reflection Tool" – a simple and intuitive web app where you can write how you feel and get a quick "emotional reflection" in return. Whether you're feeling excited, nervous, or neutral, this tool gives a playful insight into your emotions.

This project is a lightweight full-stack application with:

  Frontend: Built using React + TypeScript
  Backend:  Flask 

emotion-reflection-tool/
├── backend/     # Flask API - your emotion engine
│   ├── app.py
│   └── requirements.txt
├── frontend/    # React UI - clean & mobile-first
│   ├── src/
│   └── package.json


>>Backend (Flask)

1. Open a terminal and run:

cd backend
pip install -r requirements.txt
python app.py

2. The API will be live at:  
    'http://localhost:5000/analyze'


>>Frontend (React + TypeScript)

1. Open a new terminal tab/window:

cd frontend
npm install
npm start

2. Your frontend will open at:  
    'http://localhost:3000'


>>How It Works

1. You type a short reflection like:  
   “I feel nervous about my job interview.”
2. The frontend sends it to the backend via `/analyze`
3. The backend returns something like:  
   {
     "emotion": "Anxious",
     "confidence": 0.85
   }
4. The frontend displays it beautifully.
