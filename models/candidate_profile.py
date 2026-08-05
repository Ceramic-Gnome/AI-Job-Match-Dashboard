from dataclasses import dataclass


@dataclass
class CandidateProfile:
    name: str
    summary: str
    skills: list[str]
    experience: list[str]
