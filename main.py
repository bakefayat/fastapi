from fastapi import FastAPI
from pydantic import BaseModel
from ads import ads

app = FastAPI()

class Ad(BaseModel):
    name: str
    work: str
    phone: int
    res_phone: int


@app.get("/")
def get_ads():
    return {"ads": ads}

@app.get("/ad/{ad_id}")
def get_add(ad_id: int):
    ad = ads[ad_id]
    return {"ad": ad}

@app.post("/ad/create/{ad_id}")
def create_ad(ad_id: int, ad:Ad):
    if ad_id in ads:
        return {"msg": "ad exists"}
    
    ads[ad_id] = ad
    return ads[ad_id]

@app.delete("/ad/delete/{ad_id}")
def delete_ad(ad_id: int):
    if ad_id not in ads:
        return {"msg": "not existed"}
    
    ads.pop(ad_id)
    return {"msg": "success"}
