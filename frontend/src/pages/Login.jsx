import { useNavigate } from "react-router-dom";
import "./Login.css";

export default function Login() {

    const navigate = useNavigate();

    return (

        <div className="login-page">

            <div className="login-card">

                <h1>🤖 Customer Support AI</h1>

                <p>

                    Multi-Agent AI Customer Support System

                </p>

                <button

                    className="login-btn"

                    onClick={() => navigate("/chat")}

                >

                    🚀 Start Chatting

                </button>

            </div>

        </div>

    );

}