from pydantic_settings import BaseSettings
from typing import Optional, List
import os

class Settings(BaseSettings):
    APP_NAME: str = "Weather API"
    APP_VERSION: str = "0.1.0"
    APP_DESCRIPTION: str = "A simple weather data microservice"
    
    # API Configuration
    API_PREFIX: str = "/api"
    DEBUG: bool = False
    
    # Weather API Configuration
    WEATHER_API_KEY: str
    WEATHER_API_URL: str = "https://api.openweathermap.org/data/2.5"
    
    # CORS Configuration
    CORS_ORIGINS: List[str] = ["*"]
    
    # Logging
    LOG_LEVEL: str = "INFO"
    
    class Config:
        env_file = ".env"
        case_sensitive = True
        env_file_encoding = "utf-8"

settings = Settings()
