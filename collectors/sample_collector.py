import json
from datetime import datetime
from pathlib import Path

from models.job_data import JobData


class SampleCollector:

    def collect(self):

        local_tz = datetime.now().astimezone().tzinfo

        json_file = Path("data/sample_jobs.json")

        with open(json_file, "r", encoding="utf-8") as f:
            jobs = json.load(f)

        collected_jobs = []

        for job in jobs:

            collected_jobs.append(
                JobData(
                    title=job["title"],
                    company=job["company"],
                    location=job["location"],
                    description=job["description"],
                    url=job["url"],
                    date_posted=datetime.strptime(
                        job["date_posted"], "%Y-%m-%d"
                    ).replace(tzinfo=local_tz),
                    source="Sample",
                )
            )

        return collected_jobs
