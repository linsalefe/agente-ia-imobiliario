from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # Environment
    ENVIRONMENT: str = "development"
    
    # Server
    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = 8000
    
    # Database
    DATABASE_URL: str
    
    # Redis
    REDIS_URL: str
    
    # Evolution API
    EVOLUTION_API_URL: str
    EVOLUTION_INSTANCE: str
    EVOLUTION_INSTANCE_TOKEN: str
    EVOLUTION_API_KEY: str
    
    # Jetimob
    JETIMOB_WEBSERVICE_KEY: str
    JETIMOB_PUBLIC_KEY: str
    JETIMOB_PRIVATE_KEY: str
    
    # OpenAI
    OPENAI_API_KEY: str
    
    # Follow-up
    FOLLOWUP_D1_HOURS: int = 24
    FOLLOWUP_D3_HOURS: int = 72
    
    # Log
    LOG_LEVEL: str = "INFO"
    
    class Config:
        env_file = ".env"


settings = Settings()