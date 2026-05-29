from fastapi import APIRouter

from app.schemas.response import ApiResponse, success_response


api_router = APIRouter()


@api_router.get("/ping", response_model=ApiResponse[dict[str, str]], tags=["system"])
def ping() -> ApiResponse[dict[str, str]]:
    return success_response({"message": "pong"})
