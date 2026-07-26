from collectors.lever_collector import LeverCollector


def main():

    collector = LeverCollector("leverdemo")

    jobs = collector.collect()

    print(f"Found {len(jobs)} jobs")

    for job in jobs[:5]:
        print()
        print(f"Title: {job.title}")
        print(f"Company: {job.company}")
        print(f"Source: {job.source}")
        print(f"Location: {job.location}")
        print(f"Description Length: {len(job.description)}")
        print(f"URL: {job.url}")


if __name__ == "__main__":
    main()
