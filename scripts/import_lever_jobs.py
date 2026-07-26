from collectors.lever_collector import LeverCollector
from services.job_importer import JobImporter


def main():

    collector = LeverCollector("leverdemo")

    jobs = collector.collect()

    importer = JobImporter()

    importer.import_jobs(jobs)


if __name__ == "__main__":
    main()
