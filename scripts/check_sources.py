from database.connection import SessionLocal
from database.models import Job


def main():

    session = SessionLocal()

    results = session.query(Job.source, Job.company).all()

    counts = {}

    for source, company in results:
        counts[source] = counts.get(source, 0) + 1

    for source, count in counts.items():
        print(f"{source}: {count}")

    session.close()


if __name__ == "__main__":
    main()
