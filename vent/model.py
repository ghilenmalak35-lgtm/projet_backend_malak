from sqlalchemy import Column, Integer, Boolean, DateTime, Float
from sqlalchemy.sql import func
from database import Base

class Vent(Base):
    __tablename__ = "vents"

    id_vent = Column(Integer, primary_key=True, index=True)

    date_vent = Column(DateTime, server_default=func.now())

    quantite = Column(Integer, nullable=False)

    prix_total = Column(Float, nullable=False)

    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime, server_default=func.now())

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )

    deleted_at = Column(DateTime, nullable=True)