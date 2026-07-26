from database.connection import SessionLocal
from database.models import Job
from models.job_data import JobData


class JobImporter:

    def _job_exists(self, session, job: JobData):

        return (
            session.query(Job)
            .filter(
                Job.company == job.company,
                Job.title == job.title,
                Job.location == job.location,
                Job.url == job.url,
            )
            .first()
            is not None
        )

    def import_jobs(self, jobs: list[JobData]):

        session = SessionLocal()

        try:

            added = 0
            skipped = 0

            for job in jobs:

                if self._job_exists(session, job):
                    skipped += 1
                    continue

                db_job = Job(
                    title=job.title,
                    company=job.company,
                    location=job.location,
                    description=job.description,
                    url=job.url,
                    date_posted=job.date_posted,
                    source=job.source,
                )

                session.add(db_job)
                added += 1

            session.commit()

            print(f"Added {added} new jobs.")
            print(f"Skipped {skipped} duplicate jobs.")

        finally:
            session.close()
