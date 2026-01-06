from flask import Blueprint, abort, make_response, request, Response
from ..db import db
from ..models.board import Board
from ..models.card import Card
from .route_utilities import validate_model
cards_bp = Blueprint("card_bp", __name__, url_prefix="/cards")

@cards_bp.delete("/<card_id>")
def delete_card_from_board(card_id):
    card = validate_model(Card, card_id)

    db.session.delete(card)
    db.session.commit()

    return Response(status=204, mimetype="application/json")

@cards_bp.patch("/<card_id>")
def increase_like_by_one_card(card_id):
    card = validate_model(Card, card_id)

    card.likes += 1

    db.session.commit()

    return card.to_dict(), 200