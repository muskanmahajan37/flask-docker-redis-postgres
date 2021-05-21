from app.models.book import Book
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field


class BookSchema(SQLAlchemySchema):
    class Meta:
        model = Book
        load_instance = True

    id = auto_field()
    title = auto_field()
    author_id = auto_field()
