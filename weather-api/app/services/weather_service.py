import httpx
from typing import Dict, Any, Optional
import logging
from app.core.config import settings
logger = logging.getLogger(__name__)

class WeatherService:
    def __init__(self, api_key: str, base_url: str):
        self.api_key = settings.WEATHER_API_KEY
        self.base_url = settings.WEATHER_API_URL
        
    async def get_current_weather(self, city: str) -> Dict[str, Any]:
        """
        Get current weather data for a specified city.
        
        Args:
            city: Name of the city to get weather data for
            
        Returns:
            Dictionary containing weather data
        """
        logger.info(f"Fetching current weather for {city}")
        async with httpx.AsyncClient() as client:
            params = {
                "q": city,
                "appid": self.api_key,
                "units": "metric"
            }
            response = await client.get(f"{self.base_url}/weather", params=params)
            response.raise_for_status()
            return response.json()
    
    async def get_forecast(self, city: str, days: int = 5) -> Dict[str, Any]:
        """
        Get weather forecast for a specified city.
        
        Args:
            city: Name of the city to get forecast for
            days: Number of days for forecast (1-7)
            
        Returns:
            Dictionary containing forecast data
        """
        logger.info(f"Fetching {days}-day forecast for {city}")
        async with httpx.AsyncClient() as client:
            params = {
                "q": city,
                "appid": self.api_key,
                "units": "metric",
                "cnt": days * 8  # API returns data in 3-hour steps
            }
            response = await client.get(f"{self.base_url}/forecast", params=params)
            response.raise_for_status()
            
            # Process the response to group by days
            data = response.json()
            return self._process_forecast_data(data)
    
    def _process_forecast_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process the raw forecast data to group by days.
        
        Args:
            data: Raw forecast data from API
            
        Returns:
            Processed forecast data
        """
        # This is a simplified implementation
        return {
            "city": data.get("city", {}).get("name", ""),
            "country": data.get("city", {}).get("country", ""),
            "forecast": data.get("list", [])
        }
