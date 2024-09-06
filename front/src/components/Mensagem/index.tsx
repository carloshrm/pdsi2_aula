export interface MsgProps {
  titulo: string;
  conteudo: string;
}

function Mensagem({ titulo, conteudo }: MsgProps) {
  return (
      <div className="msg">
          <p>{titulo}</p>
          <p>{conteudo}</p>
      </div>
  );
}

export default Mensagem;
