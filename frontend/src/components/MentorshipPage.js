import React, { useState, useEffect } from 'react';
import { getContent, postContent } from '../api';

function MentorshipPage() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  useEffect(() => {
    getContent().then(response => {
      setMessages(response.data);
    });
  }, []);

  const sendMessage = () => {
    postContent({ title: 'User Query', content: input }).then(response => {
      setMessages([...messages, response.data]);
      setInput('');
    });
  };

  return (
    <div>
      <h2>AI Mentor Chat</h2>
      <div>
        {messages.map((msg, index) => (
          <p key={index}><strong>{msg.title}:</strong> {msg.content}</p>
        ))}
      </div>
      <input 
        type="text" 
        value={input} 
        onChange={(e) => setInput(e.target.value)} 
        placeholder="Ask your mentor..." 
      />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
}

export default MentorshipPage;
