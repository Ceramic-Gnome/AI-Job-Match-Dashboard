import json
from pathlib import Path

from models.candidate_profile import CandidateProfile


class ProfileLoader:

    def load(self):

        profile_file = Path("data/candidate_profile.json")

        with open(profile_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        return CandidateProfile(
            name=data["name"],
            summary=data["summary"],
            skills=data["skills"],
            experience=data["experience"],
        )
