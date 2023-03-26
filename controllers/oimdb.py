from flask import Blueprint, jsonify, request
from services.oimdb import OimDb

oimdb_controller = Blueprint('user', __name__, url_prefix='/oimdb')


@oimdb_controller.route('/search', methods=['GET'])
def search():
    title = request.args.get('title')
    films = OimDb.search(title)
    return jsonify(films)


@oimdb_controller.route('/filmInfo', methods=['GET'])
def film_info():
    film_id = request.args.get('id')
    film = OimDb.get_film(film_id)
    return jsonify(film)
