import requests

from models.job_data import JobData
from services.description_cleaner import DescriptionCleaner


class GreenhouseCollector:

    def __init__(self, company):
        self.company = company
        self.url = f"https://boards-api.greenhouse.io/v1/boards/" f"{company}/jobs"
        self.cleaner = DescriptionCleaner()

    def _get_job_details(self, job_id):

        url = (
            f"https://boards-api.greenhouse.io/v1/boards/"
            f"{self.company}/jobs/{job_id}"
        )

        response = requests.get(url)

        response.raise_for_status()

        return response.json()

    def collect(self):

        response = requests.get(self.url)

        response.raise_for_status()

        data = response.json()

        collected_jobs = []

        for job in data["jobs"]:

            details = self._get_job_details(job["id"])

            collected_jobs.append(
                JobData(
                    title=job["title"],
                    company=self.company,
                    location=job.get("location", {}).get("name") or None,
                    description=self.cleaner.clean(details.get("content", "")),
                    url=job["absolute_url"],
                    date_posted=None,
                    source="Greenhouse",
                )
            )

        return collected_jobs
