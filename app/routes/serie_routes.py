from flask import Blueprint
from app.controllers import serie_controllers

bp =Blueprint("series", __name__, url_prefix="/series")

bp.get("")(serie_controllers.series)
bp.get("/<serie_id>")(serie_controllers.select_by_id)
bp.post("")(serie_controllers.create)




