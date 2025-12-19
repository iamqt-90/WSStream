"""
Configuration settings for WSStream
"""
import os
from pathlib import Path
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Database (Supabase)
    supabase_url: str = ""
    supabase_key: str = ""
    
    # LLM Service (Groq)
    groq_api_key: str = ""
    model_name: str = "llama-3.1-8b-instant"
    
    # WebSocket
    max_connections: int = 100
    
    # Server
    host: str = "0.0.0.0"
    port: int = 8000
    debug: bool = False
    env: str = "development"
    
    class Config:
        env_file = Path(__file__).parent.parent / ".env"
        extra = "ignore"

settings = Settings()