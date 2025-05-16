from app.services.weather_service import WeatherService
from app.core.config import settings

def get_weather_service() -> WeatherService:
    """
    Dependency to get a configured WeatherService instance.
    
    Returns:
        Configured WeatherService instance
    """
    return WeatherService(
        api_key=settings.WEATHER_API_KEY,
        base_url=settings.WEATHER_API_URL
    )
