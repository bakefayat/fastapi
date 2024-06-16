from enum import Enum
from fastapi import FastAPI, HTTPException
from schemas import AdModel, WorkURLChoices, ads

app = FastAPI()


@app.get("/ads")
async def get_ads() -> dict:
    return {"ads": ads}

@app.get("/ads/{ad_id}")
async def get_add(ad_id: int) -> dict:
    ad = ads.get(ad_id)
    if ad:
        return {"ad": ad}
    raise HTTPException(status_code=404, detail="No such ad")

@app.get("/ads/work/{work_title}")
async def get_works(work_title: WorkURLChoices) -> dict:
    ads_based_on_work = [
        ad for ad in ads.values() if ad["work"] == work_title.value
    ]
    if not ads_based_on_work:
        raise HTTPException(status_code=404, detail="No such ad")
    return {"ads": ads_based_on_work}

@app.post("/ads/create/{ad_id}", status_code=201)
async def create_ad(ad_id: int, ad:AdModel) -> dict:
    if ad_id in ads:
        raise HTTPException(status_code=400, detail="ad is alredy exists")
    
    ads[ad_id] = ad
    return {"ad": ads[ad_id]}

@app.delete("/ads/delete/{ad_id}", status_code=204)
async def delete_ad(ad_id: int):
    if ad_id not in ads:
        raise HTTPException(status_code=404, detail="not existed")
    
    ads.pop(ad_id)
