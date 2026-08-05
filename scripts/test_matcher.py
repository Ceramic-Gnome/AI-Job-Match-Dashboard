from collectors.greenhouse_collector import GreenhouseCollector
from matcher.keyword_matcher import KeywordMatcher
from services.profile_loader import ProfileLoader


def main():

    profile = ProfileLoader().load()

    collector = GreenhouseCollector("datadog")

    jobs = collector.collect()

    matcher = KeywordMatcher()

    for job in jobs:

        result = matcher.calculate_match(
            profile,
            job,
        )

        if result.required_skills:

            print("=" * 60)
            print(f"Job: {job.title}")
            print(f"Company: {job.company}")
            print(f"Source: {job.source}")
            print(f"Match Score: {result.score}%")
            print(f"Matched: {result.matched_count}/{result.required_count} skills")

            print("\nRequired Skills:")
            for skill in result.required_skills:
                print(f"- {skill}")

            print("\nMatched Skills:")
            for skill in result.matched_skills:
                print(f"- {skill}")

            print("\nMissing Skills:")
            for skill in result.missing_skills:
                print(f"- {skill}")


if __name__ == "__main__":
    main()
