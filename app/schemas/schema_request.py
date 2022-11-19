from pydantic import BaseModel
from typing import List, Sequence, Optional


# build a schema using pydantic
class RequestModel(BaseModel):
    str_input: str
    list_str_input: List[str]
    opt_str_input: Optional[str] = None
    float_input: Optional[float] = 0


class RequestSearchResultsModel(BaseModel):
    results: Sequence[RequestModel]

# class RequestModelINDBBase(RequestModel):
# b3t2ed lzm 23mel hek shi b7al bde 23mel filter 3ala id le heye priamry key wmana mawjoude bel schema
#     id: Optional[int] = None
#
#     class Config:
#         orm_mode = True
