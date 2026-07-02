import { useState, useEffect, useRef } from "react";
import api from "../services/api";
import "./Chat.css";

export default function Chat() {

    const [message, setMessage] = useState("");

    const [messages, setMessages] = useState([
        {
            sender: "bot",
            text: "👋 Hello! Welcome to Customer Support AI. How can I help you today?"
        }
    ]);

    const [loading, setLoading] = useState(false);
    const totalMessages = messages.length;
const aiReplies = messages.filter(
    m => m.sender === "bot"
).length;

    const messagesEndRef = useRef(null);

    useEffect(() => {
        messagesEndRef.current?.scrollIntoView({
            behavior: "smooth"
        });
    }, [messages, loading]);

    const sendMessage = async () => {

        if (message.trim() === "") return;

        const userMessage = message;

        // Add user message
        setMessages(prev => [
            ...prev,
            {
                sender: "user",
                text: userMessage
            }
        ]);

        setMessage("");

        setLoading(true);

        try {

            const res = await api.post("/chat", {
                message: userMessage
            });

            // Add AI response
            setMessages(prev => [
                ...prev,
                {
                    sender: "bot",
                    text: res.data.reply
                }
            ]);

        } catch (err) {

            setMessages(prev => [
                ...prev,
                {
                    sender: "bot",
                    text: "❌ Backend Error"
                }
            ]);

        }

        setLoading(false);

    };

    const clearChat = () => {

        setMessages([
            {
                sender: "bot",
                text: "👋 Hello! Welcome to Customer Support AI. How can I help you today?"
            }
        ]);

    };

    return (

        <div className="chat-page">

            <div className="chat-box">

                <div
                    className="header"
                    style={{
                        display: "flex",
                        justifyContent: "space-between",
                        alignItems: "center"
                    }}
                >

                    <div>

    <div style={{fontWeight:"bold"}}>

        🤖 Customer Support AI

    </div>

    <small style={{color:"#d4f8d4"}}>

        🟢 Online

    </small>

</div>

                    <button
                        onClick={clearChat}
                        style={{
                            background: "white",
                            color: "#075e54",
                            border: "none",
                            padding: "8px 12px",
                            borderRadius: "6px",
                            cursor: "pointer"
                        }}
                    >
                        Clear
                    </button>

                </div>

                <div className="messages">

                    <div
    style={{
        background:"#ffffff",
        padding:"10px",
        borderRadius:"10px",
        marginBottom:"20px",
        textAlign:"center",
        fontWeight:"bold"
    }}
>

    📊 Messages: {totalMessages} | 🤖 AI Replies: {aiReplies}

</div>
                    {messages.map((msg, index) => (

                        <div
    key={index}
    className={msg.sender === "user" ? "user" : "bot"}
>

    {
        msg.sender === "bot" &&
        <div className="avatar">🤖</div>
    }

    <span>{msg.text}</span>

    {
        msg.sender === "user" &&
        <div className="avatar">👤</div>
    }

</div>

                    ))}

                    {loading && (

                        <div className="bot">

                            <span>🤖 Thinking...</span>

                        </div>

                    )}

                    <div ref={messagesEndRef}></div>

                </div>

                <div className="input-area">

                    <input
                        value={message}
                        onChange={(e) => setMessage(e.target.value)}
                        onKeyDown={(e) => {
                            if (e.key === "Enter") {
                                sendMessage();
                            }
                        }}
                        placeholder="Ask your question..."
                    />

                    <button onClick={sendMessage}>
                        Send
                    </button>

                </div>

            </div>

        </div>

    );

}