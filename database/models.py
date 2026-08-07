from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, Integer, String

from database.connection import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)

    title = Column(String, nullable=False)

    company = Column(String, nullable=False)

    source = Column(String)

    location = Column(String)

    work_type = Column(String)

    description = Column(String)

    url = Column(String)

    date_posted = Column(DateTime)

    date_added = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f"<Job(title='{self.title}', company='{self.company}')>"
