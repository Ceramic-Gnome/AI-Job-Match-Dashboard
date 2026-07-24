from dataclasses import dataclass
from datetime import datetime


@dataclass
class JobData:
    title: str
    company: str
    location: str
    description: str
    url: str
    date_posted: datetime