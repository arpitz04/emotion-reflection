import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [text, setText] = useState('');
  const [result, setResult] = useState<{ emotion: string; confidence: number } | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async () => {
  setLoading(true);
  setError('');
  setResult(null);

  try {
    const response = await axios.post('http://localhost:5000/analyze', { text });
    setResult(response.data as { emotion: string; confidence: number });
  } catch {
    setError('Error reaching the server');
  } finally {
    setLoading(false);
  }
};


  return (
    <div style={{ padding: 20, maxWidth: 500, margin: '0 auto' }}>
      <h1>Emotion Reflection Tool</h1>
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="How are you feeling?"
        style={{ width: '100%', height: 100, padding: 10 }}
      />
      <button onClick={handleSubmit} style={{ marginTop: 10, padding: '10px 20px' }}>
        Submit
      </button>

      {loading && <p>Analyzing...</p>}

      {result && (
        <div style={{ marginTop: 20, padding: 15, backgroundColor: '#f0f0f0', borderRadius: 8 }}>
          <p><strong>Emotion:</strong> {result.emotion}</p>
          <p><strong>Confidence:</strong> {(result.confidence * 100).toFixed(1)}%</p>
        </div>
      )}

      {error && <p style={{ color: 'red' }}>{error}</p>}
    </div>
  );
}

export default App;
