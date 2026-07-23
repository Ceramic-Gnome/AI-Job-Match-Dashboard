from datetime import datetime

from database.connection import SessionLocal
from database.models import Job


def main():
    # Create a database session
    session = SessionLocal()

    # Create a sample job
    sample_job = Job(
        title="Data Analyst",
        company="CarMax",
        location="Richmond, VA",
        description="Analyze business data and build dashboards using SQL and Power BI.",
        url="https://careers.carmax.com/",
        date_posted=datetime.now()
    )

    # Save to the database
    session.add(sample_job)
    session.commit()

    print("Sample job added successfully!")

    session.close()


if __name__ == "__main__":
    main()