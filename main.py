from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from ads import ads

app = FastAPI()

class Ad(BaseModel):
    name: str
    work: str
    phone: int
    res_phone: int


@app.get("/")
def get_ads() -> dict:
    return {"ads": ads}

@app.get("/ad/{ad_id}")
def get_add(ad_id: int) -> dict:
    ad = ads.get(ad_id)
    if ad:
        return {"ad": ad}
    raise HTTPException(status_code=404, detail="No such ad")

@app.post("/ad/create/{ad_id}")
def create_ad(ad_id: int, ad:Ad) -> str:
    if ad_id in ads:
        raise HTTPException(status_code=400, detail="ad is alredy exists")
    
    ads[ad_id] = ad
    return ads[ad_id]

@app.delete("/ad/delete/{ad_id}")
def delete_ad(ad_id: int) -> dict:
    if ad_id not in ads:
        raise HTTPException(status_code=404, detail="not existed")
    
    ads.pop(ad_id)
    return {"msg": "success"}
