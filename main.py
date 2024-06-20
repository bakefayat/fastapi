from enum import Enum
from fastapi import FastAPI, HTTPException
from schemas import AdsBaseModel, AdsCreateModel, AdsModel, WorkURLChoices, ads_list

app = FastAPI()


@app.get("/ads")
async def get_ads(
    work_title: WorkURLChoices = None,
    gender: str = None,
    ) -> list[AdsModel]:

    filterd_ads = [AdsModel(**a) for a in ads_list]
    if work_title:
        filterd_ads = [a for a in filterd_ads if a.work.value.lower() == work_title.value.lower()]
    if gender:
        filterd_ads = [a for a in filterd_ads if a.gender == gender]

    return filterd_ads

@app.post("/ads", status_code=201)
async def create_ad(ad:AdsCreateModel) -> AdsModel:
    id = ads_list[-1]["id"] + 1
    ad = AdsModel(id=id, **ad.model_dump()).model_dump()
    ads_list.append(ad)
    return ad

@app.get("/ads/{ad_id}")
async def get_add(ad_id: int) -> AdsModel:
    ad = next((ad for ad in ads_list if ad["id"] == ad_id), None)
    if ad is None:
        raise HTTPException(status_code=404, detail="No such ad")
    return ad


@app.delete("/ads/delete/{ad_id}", status_code=204)
async def delete_ad(ad_id: int):
    ad = next((a for a in ads_list if a["id"] == ad_id), None)
    if not ad:
        raise HTTPException(status_code=404, detail="not existed")

    ads_list.pop(ads_list.index(ad))
