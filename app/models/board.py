from ..db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Board(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    owner: Mapped[str]
    cards: Mapped[list["Card"]] = relationship(back_populates="board")

    def to_dict(self):
        board_as_dict = {
            "id": self.id,
            "name": self.name,
            "owner": self.owner
        }
        return board_as_dict
    
    @classmethod
    def from_dict(cls, board_data):
        new_board = cls(name=board_data["name"], owner=board_data["owner"])
        return new_board