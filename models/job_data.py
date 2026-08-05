from dataclasses import dataclass
from datetime import datetime

from models.match_result import MatchResult


@dataclass
class JobData:
    title: str
    company: str
    location: str | None
    description: str
    url: str
    date_posted: datetime | None
    source: str

    # Optional until the matcher runs
    match: MatchResult | None = None
