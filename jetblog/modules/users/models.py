from sqlalchemy import Column, Integer, String, DateTime, Table, ForeignKey

from jetblog.database import dt, Model

class User(Model):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=dt.utcnow)

    def __init__(self):
        Model.__init__(self)

    