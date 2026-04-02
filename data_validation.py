import pydantic

class DataModel(pydantic.BaseModel):
    id: int
    value: float