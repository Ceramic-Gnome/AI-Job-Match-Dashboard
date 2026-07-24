from database.connection import SessionLocal
from database.models import Job


class JobRepository:

    def get_all_jobs(self):

        session = SessionLocal()

        try:
            return (
                session.query(Job)
                .order_by(Job.date_posted.desc())
                .all()
            )

        finally:
            session.close()