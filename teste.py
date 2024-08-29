from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def teste_hello():
  response = client.get("/")
  assert response.status_code == 200
  assert response.json() == {"Hello" : "World"}

def teste_quadrado():
  num = 4
  response = client.get(f"/quadrado/{num}")
  assert response.status_code == 200
  assert response.text == str(num ** 2)

def teste_msg():
  msg = {"titulo": "teste", "conteudo": "cont"}

  response = client.post(f"/criar", json=msg)

  assert response.status_code == 201
  assert "mensagem" in response.json()

  resp_msg = response.json()["mensagem"]
  assert "titulo" in resp_msg;
  assert resp_msg["titulo"] == "teste";

  assert "conteudo" in resp_msg;
  assert resp_msg["conteudo"] == "cont";
  
  assert "publicada" in resp_msg;
  assert "created_at" in resp_msg;