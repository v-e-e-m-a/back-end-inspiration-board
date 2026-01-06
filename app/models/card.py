from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from ..db import db

class Card(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    message: Mapped[str]
    likes: Mapped[int]
    board_id: Mapped[int] = mapped_column(ForeignKey("board.id"))
    board: Mapped["Board"] = relationship(back_populates="cards")

    def to_dict(self):
        card_as_dict = {
            "id": self.id,
            "message": self.message,
            "likes": self.likes,
            "board_id": self.board_id,
            "board": self.board
        }
        return card_as_dict
    
    @classmethod
    def from_dict(cls, card_data):
        new_card = cls(
            message=card_data["message"],
            likes=0,
            board_id=card_data["board_id"],
            board=card_data["board"]
            )
        return new_card