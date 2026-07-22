from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from database.connection import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)

    title = Column(String, nullable=False)

    company = Column(String, nullable=False)

    location = Column(String)

    description = Column(String)

    url = Column(String)

    date_posted = Column(DateTime)

    date_added = Column(
        DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):
        return f"<Job(title='{self.title}', company='{self.company}')>"