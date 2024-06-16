from enum import Enum
from fastapi import FastAPI, HTTPException
from schemas import AdModel, WorkURLChoices, ads

app = FastAPI()


@app.get("/ads")
async def get_ads() -> list[AdModel]:
    return [
        AdModel(**a) for a in ads
    ]

@app.get("/ads/{ad_id}")
async def get_add(ad_id: int) -> AdModel:
    ad = next((ad for ad in ads if ad["id"] == ad_id), None)
    if ad is None:
        raise HTTPException(status_code=404, detail="No such ad")
    return ad

@app.get("/ads/work/{work_title}")
async def get_works(work_title: WorkURLChoices) -> list[AdModel]:
    ads_based_on_work = [
        ad for ad in ads if ad["work"] == work_title.value
    ]

    if not ads_based_on_work:
        raise HTTPException(status_code=404, detail="No such ad")
    return ads_based_on_work

@app.post("/ads/create/{ad_id}", status_code=201)
async def create_ad(ad:AdModel) -> AdModel:
    existed_ad = next((a for a in ads if a["id"] == ad.id), None)
    if existed_ad is not None:
        raise HTTPException(status_code=400, detail="ad is alredy exists")
    
    ads.append(dict(ad))
    return ad

@app.delete("/ads/delete/{ad_id}", status_code=204)
async def delete_ad(ad_id: int):
    if ad_id not in ads:
        raise HTTPException(status_code=404, detail="not existed")
    
    ads.pop(ad_id)
