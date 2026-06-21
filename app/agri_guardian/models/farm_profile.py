from pydantic import BaseModel

class FarmProfile(BaseModel):
    state: str
    district: str
    village: str
    land_size_acres: float
    irrigation_type: str
    current_crop: str