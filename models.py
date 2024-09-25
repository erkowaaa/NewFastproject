from typing import Optional
from sqlalchemy import String, Integer, Float, Boolean, CheckConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import date
from database import Base


class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    product_name: Mapped[str] = mapped_column(String(16))
    category: Mapped[str] = mapped_column(String(16))
    price: Mapped[float] = mapped_column(Float, CheckConstraint('price > 0'), nullable=False)
    description: Mapped[Optional[str]]
    date: Mapped[date]
    active: Mapped[bool] = mapped_column(Boolean, default=False)