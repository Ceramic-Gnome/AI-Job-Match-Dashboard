from services.profile_loader import ProfileLoader


def main():

    loader = ProfileLoader()

    profile = loader.load()

    print(f"Name: {profile.name}")
    print()
    print("Skills:")

    for skill in profile.skills:
        print(f"- {skill}")

    print()
    print("Experience:")

    for item in profile.experience:
        print(f"- {item}")


if __name__ == "__main__":
    main()
