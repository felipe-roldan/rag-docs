from pydantic import BaseModel, Field
from typing import Optional, Literal

class SearchVectorDataBaseRequest(BaseModel):
  query: Optional[str] = Field(
    default=None,
  )
  k_results: Optional[int] = Field(
    default=4,
  )