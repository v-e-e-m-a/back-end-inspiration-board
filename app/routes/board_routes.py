from flask import Blueprint, abort, make_response, request
from ..db import db
from ..models.board import Board
from ..models.card import Card
from .route_utilities import validate_model

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
