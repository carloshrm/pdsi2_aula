from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, Float
from sqlalchemy.sql import text
from database import Base

class Model_Mensagem(Base):
  __tablename__ = 'teste'

  id = Column(Integer, primary_key=True, nullable=False)
  titulo = Column(String, nullable=False)
  conteudo = Column(String, nullable=False)
  publicada = Column(Boolean, server_default="True", nullable=False)
  created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)

class Alimento(Base):
  __tablename__ = 'alimento'

  id = Column(Integer, primary_key=True, nullable=False)
  nome = Column(String, nullable=False)
  energia_kcal = Column(Float, default=0.0)
  proteina = Column(Float, default=0.0)
  colesterol = Column(String, nullable=False)
  carboidrato = Column(String, nullable=False)
  fibra_alimentar = Column(String, nullable=False)
  g_saturados = Column(String, nullable=False)
  g_mono_insat = Column(String, nullable=False)
  g_poly_insat = Column(String, nullable=False)