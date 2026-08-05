from dataclasses import dataclass


@dataclass
class MatchResult:
    score: float
    required_skills: list[str]
    matched_skills: list[str]
    missing_skills: list[str]
    matched_count: int
    required_count: int

    @property
    def color(self):
        if self.score >= 80:
            return "green"
        elif self.score >= 50:
            return "orange"
        return "red"
