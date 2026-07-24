from collectors.sample_collector import SampleCollector


def main():

    collector = SampleCollector()

    jobs = collector.collect()

    print(f"\nCollected {len(jobs)} jobs:\n")

    for job in jobs:
        print(job)


if __name__ == "__main__":
    main()