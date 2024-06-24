import React, { useState } from 'react';
import axios from 'axios';
import './Chat.css'; // Assuming you create a Chat.css file for styling

import twigaLogo from './images/twiga_logo.png'; // Import your Twiga Foods image

function Chat() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (input.trim() === '') return;

    const userMessage = { sender: 'user', text: input };
    setMessages([...messages, userMessage]);

    try {
      const response = await axios.post('http://127.0.0.1:5000/chat', { message: input });
      const botMessage = { sender: 'bot', text: response.data.response };
      setMessages([...messages, userMessage, botMessage]);
    } catch (error) {
      console.error('Error sending message to backend:', error);
    }

    setInput('');
  };

  return (
    <div className="chat-container">
      <div className="header">
        <img src={twigaLogo} alt="Twiga Foods Logo" className="logo" />
        <h1>Support ChatBot</h1>
      </div>
      <div className="chat-window">
        {messages.map((msg, index) => (
          <div key={index} className={`message ${msg.sender}`}>
            {msg.text}
          </div>
        ))}
      </div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type a message..."
        />
        <button type="submit">Send</button>
      </form>
    </div>
  );
}

export default Chat;
