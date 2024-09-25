from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class ProductListValidate(BaseModel):
    id: int
    product_name: str
    category: str
    price: float
    description: Optional[str] = None
    date: datetime
    active: bool
