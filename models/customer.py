from typing import List
from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

class Customer(Base):
    __tablename__ = 'customers'

    id: Mapped[int] = mapped_column(primary_key=True) #primary keys auto increment
    name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    email: Mapped[str] = mapped_column(db.String(255), nullable=False, unique=True)
    phone: Mapped[str] = mapped_column(db.String(25), nullable=False)
    username: Mapped[str] = mapped_column(db.String(30), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(db.String(255), nullable=False)
    #One-to-Many relationship: One customer can place many orders

    carts: Mapped[List['Cart']] = db.relationship(back_populates='customer')

