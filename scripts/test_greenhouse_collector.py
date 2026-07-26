from collectors.greenhouse_collector import GreenhouseCollector


def main():

    collector = GreenhouseCollector("datadog")

    jobs = collector.collect()

    print(f"Found {len(jobs)} jobs")

    for job in jobs[:5]:
        print()
        print(f"Title: {job.title}")
        print(f"Company: {job.company}")
        print(f"Location: {job.location}")
        print(f"URL: {job.url}")
        print(f"Date Posted: {job.date_posted}")
        print(f"Description Length: {len(job.description)}")


if __name__ == "__main__":
    main()
