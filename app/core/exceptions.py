from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.core.logging import get_logger
from app.schemas.response import ApiResponse

logger = get_logger(__name__)


class AppException(Exception):
    def __init__(
        self,
        message: str,
        *,
        code: str = "APP_ERROR",
        status_code: int = status.HTTP_400_BAD_REQUEST,
    ) -> None:
        self.message = message
        self.code = code
        self.status_code = status_code


def error_response(
    *,
    message: str,
    code: str,
    status_code: int,
    data: object = None,
) -> JSONResponse:
    return JSONResponse(
        status_code=status_code,
        content=ApiResponse(
            success=False,
            code=code,
            message=message,
            data=data,
        ).model_dump(),
    )


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(AppException)
    async def handle_app_exception(
        request: Request,
        exc: AppException,
    ) -> JSONResponse:
        logger.warning("%s %s failed: %s", request.method, request.url.path, exc.message)
        return error_response(
            message=exc.message,
            code=exc.code,
            status_code=exc.status_code,
        )

    @app.exception_handler(StarletteHTTPException)
    async def handle_http_exception(
        request: Request,
        exc: StarletteHTTPException,
    ) -> JSONResponse:
        logger.warning("%s %s failed: %s", request.method, request.url.path, exc.detail)
        return error_response(
            message=str(exc.detail),
            code="HTTP_ERROR",
            status_code=exc.status_code,
        )

    @app.exception_handler(RequestValidationError)
    async def handle_validation_exception(
        request: Request,
        exc: RequestValidationError,
    ) -> JSONResponse:
        logger.warning("%s %s validation failed: %s", request.method, request.url.path, exc.errors())
        return error_response(
            message="Request validation failed.",
            code="VALIDATION_ERROR",
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            data=exc.errors(),
        )

    @app.exception_handler(SQLAlchemyError)
    async def handle_database_exception(
        request: Request,
        exc: SQLAlchemyError,
    ) -> JSONResponse:
        logger.exception("%s %s database error: %s", request.method, request.url.path, exc)
        return error_response(
            message="Database operation failed.",
            code="DATABASE_ERROR",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    @app.exception_handler(Exception)
    async def handle_unexpected_exception(
        request: Request,
        exc: Exception,
    ) -> JSONResponse:
        logger.exception("%s %s unexpected error: %s", request.method, request.url.path, exc)
        return error_response(
            message="Internal server error.",
            code="INTERNAL_SERVER_ERROR",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
