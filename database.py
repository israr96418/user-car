from sqlmodel import create_engine, Session

# # sqlite_file_name = "database.db"
sqlite_url = "sqlite:///database.db"
# SQL_ALCHEMY_DATABASE_URL = "mysql+mysqldb://isrardawar:dawar96418@localhost:3306/sqlmodel"

engine = create_engine(sqlite_url, echo=True)

SessionLocal = Session(bind=engine)


def get_db():
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()