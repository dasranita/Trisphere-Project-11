from decimal import Decimal, ROUND_HALF_UP
from fastapi import FastAPI
from pydantic import BaseModel, Field
app=FastAPI(title='TripSphere pricing')
class Quote(BaseModel):
    nightly: Decimal=Field(gt=0)
    nights: int=Field(gt=0,le=30)
    seasonal: Decimal=Field(default=Decimal('1'),gt=0)
    discount: Decimal=Field(default=Decimal('0'),ge=0,le=1)
    tax: Decimal=Field(default=Decimal('0.12'),ge=0,le=1)
@app.post('/quote')
def quote(q:Quote):
    return {'total':str((q.nightly*q.nights*q.seasonal*(1-q.discount)*(1+q.tax)).quantize(Decimal('.01'),rounding=ROUND_HALF_UP))}
