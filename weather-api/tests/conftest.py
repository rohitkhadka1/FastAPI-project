import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch

from app.main import app

@pytest.fixture
def client():
    """
    Test client fixture for FastAPI application.
    
    Returns:
        TestClient: A test client for the FastAPI app
    """
    with TestClient(app) as test_client:
        yield test_client

@pytest.fixture
def mock_weather_service():
    """
    Mock for the WeatherService to avoid actual API calls during tests.
    
    Returns:
        Mock: A mock of the WeatherService
    """
    with patch("app.api.dependencies.WeatherService") as mock_service:
        yield mock_service
