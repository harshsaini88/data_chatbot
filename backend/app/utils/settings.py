from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Memory Improvement Chatbot"
    MODEL_PATH: str = "/path/to/trained/model"
    MAX_MEMORY_ENTRIES: int = 1000
    EMBEDDING_DIM: int = 768
    
    class Config:
        env_file = ".env"

settings = Settings()