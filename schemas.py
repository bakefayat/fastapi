from enum import Enum
from pydantic import BaseModel, validator

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
    @validator('work', pre=True)
    def title_case_work(cls, value):
        return value.upper()


class AdsModel(AdsBaseModel):
    id: int


ads_list = [
    {
        "id": 1,
        "name": "ehsan",
        "work": "IT",
        "gender": "male",
        "phone": 9371304458,
        "res_phone": 9011259601
    },
    {
        "id": 2,
        "name": "oways",
        "work": "EMS",
        "gender": "male",
        "phone": 9156962252,
        "res_phone": 9379339007
    },
    {
        "id": 3,
        "name": "sahar",
        "work": "IT",
        "gender": "female",
        "phone": 9154879652,
        "res_phone": 9745312548
    }
]
