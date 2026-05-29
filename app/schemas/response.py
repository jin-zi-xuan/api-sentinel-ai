from typing import Generic, Optional, TypeVar

from pydantic import BaseModel


DataT = TypeVar("DataT")


class ApiResponse(BaseModel, Generic[DataT]):
    success: bool = True
    code: str = "OK"
    message: str = "Success"
    data: Optional[DataT] = None


def success_response(data: Optional[DataT] = None, message: str = "Success") -> ApiResponse[DataT]:
    return ApiResponse(data=data, message=message)
