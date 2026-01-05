from flask import Blueprint

cards_bp = Blueprint("card_bp", __name__, url_prefix="/cards")

@cards_bp.get("")
def get_all_cards():
    pass