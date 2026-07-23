from database.connection import SessionLocal
from database.models import Job
from utils.formatting import format_datetime

def main():
    session = SessionLocal()

    jobs = session.query(Job).all()

    if not jobs:
        print("No jobs found.")
    else:
        print(f"\nFound {len(jobs)} job(s):\n")

        for job in jobs:
            print(f"ID: {job.id}")
            print(f"Title: {job.title}")
            print(f"Company: {job.company}")
            print(f"Location: {job.location}")
            print(f"Posted: {format_datetime(job.date_posted)}")
            print("-" * 40)

    session.close()


if __name__ == "__main__":
    main()