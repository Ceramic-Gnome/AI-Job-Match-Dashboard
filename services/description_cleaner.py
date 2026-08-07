import re
from html import unescape


class DescriptionCleaner:

    def clean(self, description):

        if not description:
            return ""

        # Convert HTML entities
        description = unescape(description)

        # Replace common HTML breaks with new lines
        description = re.sub(
            r"<br\s*/?>",
            "\n",
            description,
            flags=re.IGNORECASE,
        )

        # Remove HTML tags
        description = re.sub(
            r"<[^>]+>",
            "",
            description,
        )

        # Clean extra whitespace
        description = re.sub(
            r"\n\s*\n+",
            "\n\n",
            description,
        )

        description = re.sub(
            r"[ \t]+",
            " ",
            description,
        )

        return description.strip()
