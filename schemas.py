from pydantic import BaseModel, Field, validator
from typing import List, Union

class HeartData(BaseModel):
    age: float
    sex: float
    cp: float
    trtbps: float
    chol: float
    fbs: float
    restecg: float
    thalachh: float
    exng: float
    oldpeak: float
    slp: float
    caa: float
    thall: float

    @validator("*", pre=True)
    def parse_float(cls, v):
        return float(v)
