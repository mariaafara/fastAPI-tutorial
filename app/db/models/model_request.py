# define our model

from sqlalchemy import Column, DateTime, Integer, String, Float
from sqlalchemy.sql import func

from app.db.base_class import Base


class UserRequest(Base):
    """
    Request Python class which inherits from the Base class. The inheritance allows SQLAlchemy to detect and map
    the class to a database table.
    """
    __tablename__ = 'requests'
    id = Column(Integer, primary_key=True, index=True)
    str_input = Column(String)
    str2_input = Column(String)
    opt_str_input = Column(String, nullable=True)
    float_input = Column(Float)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
