import requests
from flask import Blueprint, request, jsonify
from app.db.session import session
from app.models.author import Author
from app.schemas.author import AuthorSchema
from app.common.extensions import cache
from flask import current_app

router = Blueprint('authors', __name__)
author_schema = AuthorSchema()


@router.route("/")
def get_root():
    return jsonify({"message": "Hello world"})


@router.route("/authors", methods=["GET"])
def get_users():
    authors_schema = AuthorSchema(many=True)
    authors = session.query(Author).all()
    authors_json = authors_schema.dump(authors)
    return jsonify(authors_json)


@router.route("/authors", methods=["POST"])
def create_author():
    name = request.json["name"]
    new_author = Author(name=name)
    session.add(new_author)
    session.commit()
    author = author_schema.dump(new_author)
    return author


@router.route("/authors/<id>", methods=["GET"])
def get_author(id: int):
    author = session.query(Author).get(id)
    if not author:
        return {"message": "No author found"}
    return author_schema.dump(author)


@router.route("/jobs", methods=['GET'])
@cache.cached(timeout=15, query_string=True)
def get_jobs():
    search = request.args.get('search')
    r = requests.get(f"{current_app.config['GITHUB_JOBS_URL']}{search}")
    return jsonify(r.json())
