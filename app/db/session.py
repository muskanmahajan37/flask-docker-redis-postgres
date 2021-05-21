import os

import sqlalchemy as sa
from sqlalchemy.orm import scoped_session, sessionmaker

pg_url = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_SERVER')}/{os.getenv('POSTGRES_DB')}"
engine = sa.create_engine(pg_url)
session = scoped_session(sessionmaker(bind=engine))
