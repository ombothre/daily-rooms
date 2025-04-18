import React, { useState } from 'react';

function App() {
  const [formData, setFormData] = useState({
    selectedBot: 'default'
  });

  const [roomURL, setRoomURL] = useState('');

  const getAIName = (bot) => {
    switch (bot) {
      case 'bajaj':
        return 'Bajaj AI';
      case 'hdfc':
        return 'HDFC AI';
      default:
        return 'Default AI';
    }
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const body = {
      bot_model: {
        bot_profile: "natural_conversation_2024_11",
        tts: {
          service: "cartesia"
        },
        stt: {
          model: "deepgram",
          language: "en"
        },
        llm: {
          service: "anthropic",
          model: "gpt-4"
        }
      },
      max_duration: 300,
      customer_name: "John Doe",
      ai_name: getAIName(formData.selectedBot),
      total_due: 15000.0,
      emi_amount: 5000.0
    };

    try {
      const endpoint = `http://127.0.0.1:8000/api/createRoom/${formData.selectedBot}`;
      const response = await fetch(endpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body)
      });

      if (response.ok) {
        const data = await response.json();
        setRoomURL(data.roomURL);
      } else {
        setRoomURL('Error creating room');
      }
    } catch (error) {
      setRoomURL('Error: ' + error.message);
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100 p-6">
      <div className="bg-white shadow-lg rounded-lg p-8 w-full max-w-md">
        <h1 className="text-3xl text-black font-bold text-center mb-6">DailyBots Agent Room</h1>
        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label 
              htmlFor="selectedBot" 
              className="block text-gray-700 text-sm font-semibold mb-2"
            >
              Select Bot
            </label>
            <select
              id="selectedBot"
              name="selectedBot"
              value={formData.selectedBot}
              onChange={handleChange}
              className="w-full px-3 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400 text-black"
            >
              <option value="default">Default</option>
              <option value="bajaj">Bajaj</option>
              <option value="hdfc">HDFC</option>
            </select>
          </div>
          <button 
            type="submit" 
            className="w-full bg-blue-500 text-white py-2 rounded-md hover:bg-blue-600 transition-colors"
          >
            Create Room
          </button>
        </form>
        {roomURL && (
          <div className="mt-6 text-center">
            <h4 className="text-xl font-semibold mb-2 text-black">Room URL:</h4>
            <a 
              href={roomURL} 
              className="text-blue-500 hover:underline break-all"
              target="_blank"
              rel="noopener noreferrer"
            >
              Room Link
            </a>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
