import "./App.css";

import { useEffect, useState } from "react";

import Mensagem from "./components/Mensagem";
import MensagemForm from "./components/MensagemForm";

export interface MsgModel {
    titulo: string;
    conteudo: string;
}

function App() {
    const [msg, setMsg] = useState<MsgModel[]>([]);

    async function getMessages() {
        fetch("http://localhost:8000/msg")
            .then((res) => res.json())
            .then((data) => setMsg(data));
    }

    useEffect(() => {
        getMessages();
    }, []);

    return (
        <div>
            <MensagemForm update={getMessages} />
            <div className="msg-container">
                {msg.map((m: MsgModel, i) => (
                    <Mensagem titulo={m.titulo} conteudo={m.conteudo} key={i} />
                ))}
            </div>
        </div>
    );
}

export default App;
