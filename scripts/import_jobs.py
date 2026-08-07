from collectors.greenhouse_collector import GreenhouseCollector
from collectors.lever_collector import LeverCollector
from services.job_importer import JobImporter


def main():

    jobs = []

    collectors = [
        GreenhouseCollector("datadog"),
        LeverCollector("datadog"),
    ]

    for collector in collectors:

        try:
            collected_jobs = collector.collect()
            jobs.extend(collected_jobs)

            print(
                f"{collector.__class__.__name__}: "
                f"{len(collected_jobs)} jobs collected"
            )

        except Exception as e:  # noqa: BLE001
            # Continue importing from other sources if one collector fails.
            print(f"{collector.__class__.__name__} failed: {e}")

    importer = JobImporter()

    importer.import_jobs(jobs)


if __name__ == "__main__":
    main()
