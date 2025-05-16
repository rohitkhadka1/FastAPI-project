import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.services.weather_service import WeatherService
from app.api.endpoints import weather
from app.core.config import settings
from app.core.logging import setup_logging
import httpx

logger = setup_logging()

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(f"Starting {settings.APP_NAME} v{settings.APP_VERSION}")
    yield
    logger.info(f"Shutting down {settings.APP_NAME}")

app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
    lifespan=lifespan
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include weather router
app.include_router(
    weather.router,
    prefix=settings.API_PREFIX,
    tags=["weather"]
)

@app.get("/", tags=["root"])
async def root():
    return {"message": "Welcome to Weather API! Go to /docs for documentation."}

@app.get("/health", tags=["health"])
async def health_check():
    logger.info("Health check requested")
    return {"status": "healthy"}
@app.get("/api/v1/weather/{city}")
async def get_weather(city: str):
    try:
        return await weather_service.get_weather(city)
    except httpx.HTTPError as exc:
        raise HTTPException(
            status_code=exc.response.status_code,
            detail=f"Error fetching weather data: {str(exc)}"
        )

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
