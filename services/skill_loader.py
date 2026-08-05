import json


class SkillLoader:

    def load(self):

        with open("data/known_skills.json") as f:
            data = json.load(f)

        skills = []
        weights = {}

        for category, info in data.items():

            weight = info["weight"]

            for skill in info["skills"]:
                skills.append(skill)
                weights[skill] = weight

        return {
            "skills": skills,
            "weights": weights,
        }
