# Weather API Service

A FastAPI-based microservice that provides weather information for cities using the OpenWeatherMap API.

## Features

- Get current weather data for any city
- RESTful API endpoints
- OpenAPI documentation
- Environment-based configuration
- Docker support
- Health check endpoint

## Prerequisites

- Python 3.8+
- Docker (optional)
- OpenWeatherMap API key

## Local Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/weather-api.git
cd weather-api
```

2. Create and activate virtual environment:
```bash
python -m venv venv
.\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file in the project root:
```env
WEATHER_API_KEY=your_openweathermap_api_key
WEATHER_API_URL=https://api.openweathermap.org/data/2.5
```

5. Run the application:
```bash
uvicorn app.main:app --reload
```

The API will be available at http://localhost:8000

## Docker Setup

1. Build the Docker image:
```bash
docker build -t weather-api .
```

2. Run the container:
```bash
docker run -d -p 8000:8000 --env-file .env weather-api
```

## API Endpoints

- `GET /health` - Health check endpoint
- `GET /api/v1/weather/{city}` - Get weather for a specific city
- `GET /docs` - OpenAPI documentation

## Example Request

```bash
curl http://localhost:8000/api/v1/weather/london
```

## Configuration

The application uses environment variables for configuration:

| Variable | Description | Default |
|----------|-------------|---------|
| WEATHER_API_KEY | OpenWeatherMap API key | Required |
| WEATHER_API_URL | OpenWeatherMap API URL | https://api.openweathermap.org/data/2.5 |

## Development

- Use pre-commit hooks for code quality
- Run tests with pytest
- CI/CD with GitHub Actions

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.# FastAPI-project