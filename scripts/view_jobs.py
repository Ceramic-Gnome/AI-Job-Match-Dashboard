from collections import Counter

from repositories.job_repository import JobRepository
from utils.formatting import format_datetime


def main():

    repository = JobRepository()

    jobs = repository.get_all_jobs()

    if not jobs:
        print("No jobs found.")
        return

    print("\nWork Arrangement Summary:")
    print(Counter(job.work_type for job in jobs))

    print(f"\nFound {len(jobs)} job(s):\n")

    for job in jobs:
        print(f"ID: {job.id}")
        print(f"Title: {job.title}")
        print(f"Company: {job.company}")
        print(f"Location: {job.location}")
        print(f"Work Type: {job.work_type}")
        print(f"Source: {job.source}")
        print(f"Posted: {format_datetime(job.date_posted)}")
        print("-" * 40)


if __name__ == "__main__":
    main()
