import sqlalchemy as sa
from app.db.base_class import Base


class Author(Base):
    __tablename__ = "authors"
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(50), nullable=False)

    def __repr__(self):
        return "<Author(name={self.name!r})>".format(self=self)
