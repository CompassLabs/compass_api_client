from enum import StrEnum
from typing import Union

from pydantic import BaseModel, Field


class AnswerType(StrEnum):
    TEXT = "text"
    IMAGE = "image"
    UNSIGNED_TRANSACTION = "unsigned_transaction"
    RAW_PIE_CHART = "raw_pie_chart"
    ERROR = "error"


class RawPieChartAnswer(BaseModel):
    labels: list[str]
    values: list[Union[int, float]]
    title: str


class ChatAnswer(BaseModel):
    type: AnswerType = Field(
        ...,
        description="The compass chatbot can return different types of answers."
        "Apart from text, it can also return images or unsigned transactions.",
    )
    content: Union[dict, str, RawPieChartAnswer] = Field(
        ..., description="The answer content."
    )
