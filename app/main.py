from fastapi import FastAPI

from app.api.v1.router import api_router
from app.core.config import settings
from app.core.exceptions import register_exception_handlers
from app.core.logging import setup_logging
from app.schemas.health import HealthResponse
from app.schemas.response import ApiResponse, success_response


setup_logging()

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="AI-driven API security testing and risk analysis platform.",
    version=settings.API_VERSION,
)
register_exception_handlers(app)


@app.get("/health", response_model=ApiResponse[HealthResponse], tags=["health"])
def health_check() -> ApiResponse[HealthResponse]:
    return success_response(
        HealthResponse(
            status="ok",
            service=settings.PROJECT_NAME,
            version=settings.API_VERSION,
        )
    )


app.include_router(api_router, prefix=settings.API_V1_PREFIX)
