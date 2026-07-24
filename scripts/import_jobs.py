from collectors.sample_collector import SampleCollector
from services.job_importer import JobImporter


def main():

    collector = SampleCollector()

    jobs = collector.collect()

    importer = JobImporter()

    importer.import_jobs(jobs)


if __name__ == "__main__":
    main()