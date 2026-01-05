# class Card:
#     def __init__(self, id, message):
#         self.id = id
#         self.message = message
    
# cards = [
#     Card(1, "this is a test message")
# ]
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from ..db import db

class Card(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    message: Mapped[str]
    likes: Mapped[int]
    board_id: Mapped[int] = mapped_column(ForeignKey("board.id"))
    board: Mapped["Board"] = relationship(back_populates="cards")