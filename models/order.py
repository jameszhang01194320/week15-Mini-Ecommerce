
from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
import datetime
from typing import List


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    customer_id: Mapped[int] = mapped_column(db.ForeignKey('customers.id'))
    date: Mapped[datetime.date] = mapped_column(db.Date, nullable=False)



