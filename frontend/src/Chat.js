import React, { useState } from "react";
import { sendMessage } from "./api";

function Chat() {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState("");

    const handleSend = async () => {
        const userMessage = { role: "user", text: input };
        setMessages([...messages, userMessage]);

        const res = await sendMessage(input);

        const botMessage = { role: "bot", text: res.response };
        setMessages(prev => [...prev, botMessage]);

        setInput("");
    };

    return (
        <div>
            <h2>Chat</h2>

            <div>
                {messages.map((msg, i) => (
                    <div key={i}>
                        <strong>{msg.role}: </strong>{msg.text}
                    </div>
                ))}
            </div>

            <input
                value={input}
                onChange={(e) => setInput(e.target.value)}
            />
            <button onClick={handleSend}>Send</button>
        </div>
    );
}

export default Chat;