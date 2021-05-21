from app.models.author import Author
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field


class AuthorSchema(SQLAlchemySchema):
    class Meta:
        model = Author
        load_instance = True  # Optional: deserialize to model instances

    id = auto_field()
    name = auto_field()
