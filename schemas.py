from enum import Enum
from pydantic import BaseModel

class WorkURLChoices(Enum):
    EMS = "EMS"
    IT = "IT"


class AdModel(BaseModel):
    name: str
    work: WorkURLChoices
    phone: int
    res_phone: int


ads = {
    1: {
        "name": "ehsan",
        "work": "IT",
        "phone": 9371304458,
        "res_phone": 9011259601
        },
    2: {
        "name": "oways",
        "work": "EMS",
        "phone": 9156962252,
        "res_phone": 9379339007
    },
    3: {
        "name": "elyas",
        "work": "IT",
        "phone": 9154879652,
        "res_phone": 9745312548
    }
}