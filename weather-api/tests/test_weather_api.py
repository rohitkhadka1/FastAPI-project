import pytest
from fastapi.testclient import TestClient

def test_health_check(client: TestClient):
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_get_weather(client: TestClient, mock_weather_service):
    """Test the get weather endpoint with mocked service."""
    # Mock the weather service response
    mock_instance = mock_weather_service.return_value
    mock_instance.get_current_weather.return_value = {
        "name": "London",
        "main": {"temp": 15.5, "humidity": 70},
        "weather": [{"description": "cloudy"}]
    }
    
    # Test the endpoint
    response = client.get("/api/weather?city=London")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "London"
    assert "temp" in data["main"]
    
    # Verify the service was called correctly
    mock_instance.get_current_weather.assert_called_once_with("London")

def test_get_forecast(client: TestClient, mock_weather_service):
    """Test the get forecast endpoint with mocked service."""
    # Mock the weather service response
    mock_instance = mock_weather_service.return_value
    mock_instance.get_forecast.return_value = {
        "city": "London",
        "country": "GB",
        "forecast": [
            {"dt": 1621346400, "main": {"temp": 15.5}, "weather": [{"description": "cloudy"}]},
            {"dt": 1621357200, "main": {"temp": 16.2}, "weather": [{"description": "partly cloudy"}]}
        ]
    }
    
    # Test the endpoint
    response = client.get("/api/forecast?city=London&days=2")
    assert response.status_code == 200
    data = response.json()
    assert data["city"] == "London"
    assert len(data["forecast"]) == 2
    
    # Verify the service was called correctly
    mock_instance.get_forecast.assert_called_once_with("London", 2)
