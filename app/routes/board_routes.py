from flask import Blueprint, abort, make_response
# from app.models.board import boards

boards_bp = Blueprint("board_bp", __name__, url_prefix="/boards")

# @boards_bp.get("")
# def get_all_boards():
#     result_list = []

#     for board in boards:
#         result_list.append(dict(
#             id=board.id,
#             name=board.name,
#             owner=board.owner
#         )
#         )
    
#     return result_list

# @boards_bp.get("/<id>")
# def get_board_by_id(id):
#     pass