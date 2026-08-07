from services.description_cleaner import DescriptionCleaner


def main():

    html = """
    <p>Responsibilities</p>
    <ul>
        <li>Build dashboards</li>
        <li>Write SQL queries</li>
    </ul>
    """

    cleaner = DescriptionCleaner()

    print(cleaner.clean(html))


if __name__ == "__main__":
    main()
