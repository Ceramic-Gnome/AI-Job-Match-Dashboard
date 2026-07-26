from collectors.greenhouse_collector import GreenhouseCollector
from services.job_importer import JobImporter


def main():

    collector = GreenhouseCollector("datadog")

    jobs = collector.collect()

    importer = JobImporter()

    importer.import_jobs(jobs)


if __name__ == "__main__":
    main()
