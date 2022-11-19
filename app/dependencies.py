from app.db.db_session import SessionLocal

# def _add_tables_to_db():
#     # This will bind our models to the created database
#     return database.Base.metadata.create_all(bind=database.engine)

# TODO add documentation on the importance of having this and of having it in separate script
# Dependency
def get_db():
    """
        This method creates a DB session
    :return: generator
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

