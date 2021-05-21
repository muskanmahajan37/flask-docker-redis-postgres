import sqlalchemy as sa
from app.db.base_class import Base
from sqlalchemy.orm import backref, relationship


class Book(Base):
    __tablename__ = "books"
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String(50))
    author_id = sa.Column(sa.Integer, sa.ForeignKey("authors.id"))
    author = relationship("Author", backref=backref("books"))
