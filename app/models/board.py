from ..db import db
from sqlalchemy.orm import Mapped, mapped_column

class Board(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    owner: Mapped[str]