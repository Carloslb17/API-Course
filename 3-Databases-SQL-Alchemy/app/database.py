from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

### Connection with FastAPI and the database via SQLAlchemy (ORM)
## Connection to the database. 
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:admin@localhost/fastapi'
engine = create_engine(SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()