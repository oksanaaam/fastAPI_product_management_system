from datetime import datetime

from sqlalchemy import Column, Float, Integer, String

from db.engine import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True, unique=True)
    description = Column(String(511))
    price = Column(Float)
    created_at = Column(String(30), default=datetime.utcnow().isoformat())
