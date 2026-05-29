from fastapi import APIRouter


api_router = APIRouter()


@api_router.get("/ping", tags=["system"])
def ping() -> dict[str, str]:
    return {"message": "pong"}
