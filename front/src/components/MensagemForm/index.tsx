import { MsgModel } from "../../App";
import { useState } from "react";

export interface MensagemFormProps {
    update: () => void;
}

function MensagemForm({ update }: MensagemFormProps) {
    const [msgInput, setMsgInput] = useState<MsgModel>({ conteudo: "", titulo: "" });

    async function addMessageHandler() {
        await fetch("http://localhost:8000/msg/criar", {
            method: "POST",
            body: JSON.stringify(msgInput),
            headers: new Headers({ "Content-Type": "application/json" }),
        });
        update();
    }

    return (
        <div className="form-container">
            <div>
                <label htmlFor="titulo">Título: </label>
                <input
                    type="text"
                    name="titulo"
                    id="titulo"
                    value={msgInput.titulo}
                    onChange={(e) => {
                        setMsgInput((m) => ({ ...m, titulo: e.target.value }));
                    }}
                />
            </div>
            <div>
                <label htmlFor="titulo">Conteudo: </label>
                <input
                    type="text"
                    name="conteudo"
                    id="conteudo"
                    value={msgInput.conteudo}
                    onChange={(e) => {
                        setMsgInput((m) => ({ ...m, conteudo: e.target.value }));
                    }}
                />
            </div>
            <button onClick={addMessageHandler}>Post</button>
        </div>
    );
}

export default MensagemForm;
