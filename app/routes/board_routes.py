from flask import Blueprint, abort, make_response, request
from ..db import db
from ..models.board import Board
from ..models.card import Card
from .route_utilities import validate_model, send_slack_notification

boards_bp = Blueprint("board_bp", __name__, url_prefix="/boards")

@boards_bp.get("")
def get_all_boards():
    query = db.select(Board)
    boards = db.session.scalars(query)
    boards_response = [board.to_dict() for board in boards]
    return boards_response

@boards_bp.get("/<board_id>")
def get_one_board(board_id):
    board = validate_model(Board, board_id)
    return {"board": board.to_dict()}

@boards_bp.post("")
def create_board():
    request_body = request.get_json()

    try:
        new_board = Board.from_dict(request_body)

    except KeyError as error:
        response = {"details": f"Invalid data"}
        abort(make_response(response, 400))

    db.session.add(new_board)
    db.session.commit()

    return {"board": new_board.to_dict()}, 201

@boards_bp.post("/<board_id>/cards")
def create_card_with_board_id(board_id):
    board = validate_model(Board, board_id)

    request_body = request.get_json()
    request_body["board_id"] = board.id

    try:
        new_card = Card.from_dict(request_body)
    except KeyError as error:
        return {"error": f"this is what you requested: {request_body}"}, 400
    
    board.cards.append(new_card)
    
    db.session.add(new_card)
    db.session.commit()

    send_slack_notification(f"New card posted: {new_card.message}")

    return new_card.to_dict(), 201

@boards_bp.get("/<board_id>/cards")
def get_all_cards_from_board_id(board_id):
    board = validate_model(Board, board_id)
    
    return board.to_dict(), 200


