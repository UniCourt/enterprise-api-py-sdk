"""SDK response object."""

from __future__ import annotations
from typing import Generic, TypeVar
from pydantic import Field, StrictInt, BaseModel

T = TypeVar("T")

class SdkResponse(BaseModel, Generic[T]):
    """
    SDK response object
    """

    data: tuple[T, StrictInt] = Field(description="Deserialized data given the data type and HTTP status code")

    model_config = {
        "arbitrary_types_allowed": True
    }
