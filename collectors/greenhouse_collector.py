from datetime import datetime

import requests

from models.job_data import JobData
from services.description_cleaner import DescriptionCleaner
from services.work_type_detector import determine_work_type


class GreenhouseCollector:

    def __init__(self, company):
        self.company = company
        self.url = f"https://boards-api.greenhouse.io/v1/boards/" f"{company}/jobs"
        self.cleaner = DescriptionCleaner()

    @staticmethod
    def parse_greenhouse_date(date_string):

        if not date_string:
            return None

        return datetime.fromisoformat(date_string.replace("Z", "+00:00"))

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

            description = self.cleaner.clean(details.get("content", ""))

            collected_jobs.append(
                JobData(
                    title=job["title"],
                    company=self.company,
                    location=job.get("location", {}).get("name") or None,
                    work_type=determine_work_type(description),
                    description=description,
                    url=job["absolute_url"],
                    date_posted=self.parse_greenhouse_date(job.get("first_published"))
                    or self.parse_greenhouse_date(job.get("updated_at")),
                    source="Greenhouse",
                )
            )

        return collected_jobs
