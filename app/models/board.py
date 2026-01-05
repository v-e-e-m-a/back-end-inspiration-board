from ..db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Board(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    owner: Mapped[str]
    cards: Mapped[list["Card"]] = relationship(back_populates="board")