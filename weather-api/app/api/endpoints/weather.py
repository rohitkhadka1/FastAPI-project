from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Dict, Any

from app.services.weather_service import WeatherService
from app.api.dependencies import get_weather_service

router = APIRouter()

@router.get("/weather", summary="Get current weather data")
async def get_weather(
    city: str = Query(..., description="City name"),
    weather_service: WeatherService = Depends(get_weather_service)
) -> Dict[str, Any]:
    """
    Get current weather data for a specified city.
    
    Parameters:
    - **city**: Name of the city to get weather data for
    
    Returns:
    - Weather data including temperature, humidity, and conditions
    """
    try:
        weather_data = await weather_service.get_current_weather(city)
        return weather_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/forecast", summary="Get weather forecast")
async def get_forecast(
    city: str = Query(..., description="City name"),
    days: int = Query(5, description="Number of days for forecast", ge=1, le=7),
    weather_service: WeatherService = Depends(get_weather_service)
) -> Dict[str, Any]:
    """
    Get weather forecast for a specified city.
    
    Parameters:
    - **city**: Name of the city to get forecast for
    - **days**: Number of days for forecast (1-7)
    
    Returns:
    - Forecast data including temperature, humidity, and conditions for each day
    """
    try:
        forecast_data = await weather_service.get_forecast(city, days)
        return forecast_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
