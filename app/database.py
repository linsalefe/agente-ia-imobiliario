from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

# Engine do SQLAlchemy
engine = create_engine(settings.DATABASE_URL)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para models
Base = declarative_base()


def get_db():
    """
    Dependency para obter sessão do banco
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def test_connection():
    """
    Testa conexão com banco de dados
    """
    try:
        conn = engine.connect()
        conn.close()
        print("✅ Conexão com banco estabelecida com sucesso!")
        return True
    except Exception as e:
        print(f"❌ Erro ao conectar com banco: {e}")
        return False