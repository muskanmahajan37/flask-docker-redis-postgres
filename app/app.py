from app.core.config import BaseConfig
from app.db.base_class import Base
from app.db.session import engine
from flask import Flask
from app.api.authors import router as author_router

from app.common.extensions import cache

app = Flask(__name__)
app.config.from_object(BaseConfig)
cache.init_app(app)

app.register_blueprint(author_router)
Base.metadata.create_all(engine)

