from enum import Enum
from pydantic import BaseModel

class WorkURLChoices(Enum):
    EMS = "EMS"
    IT = "IT"


class AdsBaseModel(BaseModel):
    name: str
    work: WorkURLChoices
    gender: str
    phone: int
    res_phone: int

class AdsCreateModel(AdsBaseModel):
    pass


class AdsModel(AdsBaseModel):
    id: int


ads_list = [
    {
        "id": 0,
        "name": "ehsan",
        "work": "IT",
        "gender": "male",
        "phone": 9371304458,
        "res_phone": 9011259601
    },
    {
        "id": 1,
        "name": "oways",
        "work": "EMS",
        "gender": "male",
        "phone": 9156962252,
        "res_phone": 9379339007
    },
    {
        "id": 2,
        "name": "sahar",
        "work": "IT",
        "gender": "female",
        "phone": 9154879652,
        "res_phone": 9745312548
    }
]
