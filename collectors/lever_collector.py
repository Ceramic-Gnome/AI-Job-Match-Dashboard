import requests

from models.job_data import JobData


class LeverCollector:

    def __init__(self, company):
        self.company = company
        self.url = f"https://api.lever.co/v0/postings/{company}"

    def collect(self):

        response = requests.get(self.url)

        response.raise_for_status()

        jobs = response.json()

        collected_jobs = []

        for job in jobs:

            categories = job.get("categories", {})

            collected_jobs.append(
                JobData(
                    title=job.get("text"),
                    company=self.company,
                    location=categories.get("location") or None,
                    description=job.get("descriptionPlain", ""),
                    url=job.get("hostedUrl"),
                    date_posted=None,
                    source="Lever",
                )
            )

        return collected_jobs
