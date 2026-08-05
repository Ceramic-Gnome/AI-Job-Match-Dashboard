import re

from models.match_result import MatchResult
from services.skill_loader import SkillLoader


class KeywordMatcher:

    def __init__(self):

        skill_data = SkillLoader().load()

        self.known_skills = skill_data["skills"]

        self.skill_weights = skill_data["weights"]

    def _extract_required_skills(self, description):

        description = description.lower()

        required = []

        for skill in self.known_skills:

            pattern = rf"\b{re.escape(skill.lower())}\b"

            if re.search(pattern, description):
                required.append(skill)

        return required

    def calculate_match(self, profile, job):

        description = f"{job.title} {job.description or ''}"

        required_skills = self._extract_required_skills(description)

        matched_skills = [skill for skill in required_skills if skill in profile.skills]

        missing_skills = [
            skill for skill in required_skills if skill not in profile.skills
        ]

        if not required_skills:

            score = 0

        else:

            total_weight = sum(self.skill_weights[skill] for skill in required_skills)

            matched_weight = sum(self.skill_weights[skill] for skill in matched_skills)

            score = round(
                matched_weight / total_weight * 100,
                2,
            )

        return MatchResult(
            score=score,
            required_skills=required_skills,
            matched_skills=matched_skills,
            missing_skills=missing_skills,
            matched_count=len(matched_skills),
            required_count=len(required_skills),
        )
