import classes
import model as model

from typing import List
from fastapi import FastAPI, status, Depends
from fastapi.middleware.cors import CORSMiddleware
from database import engine, get_db
from sqlalchemy.orm import Session
from scrape import scrape_ufu

model.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware, allow_origins=['*'],
    allow_credentials=True, allow_methods=['*'], allow_headers=['*'])

@app.get("/")
def read_root():
  return {"Hello": "World"}

@app.get("/msg", response_model=List[classes.Mensagem], status_code=status.HTTP_200_OK)
def get_all_msg(db: Session = Depends(get_db), skip: int = 0, limit: int=100):
  mensagens = db.query(model.Model_Mensagem).offset(skip).limit(limit).all();
  return mensagens;

@app.post("/msg/criar", status_code=status.HTTP_201_CREATED)
def criar_valores(nova_mensagem: classes.Mensagem, db: Session = Depends(get_db)):
  mensagem_criada = model.Model_Mensagem(**nova_mensagem.model_dump())
  db.add(mensagem_criada)
  db.commit()
  db.refresh(mensagem_criada)
  return {"mensagem": mensagem_criada}

@app.get("/quadrado/{num}")
def square(num: int):
  return num ** 2

@app.get("/scrape")
def runScrape():
  scrape_ufu()