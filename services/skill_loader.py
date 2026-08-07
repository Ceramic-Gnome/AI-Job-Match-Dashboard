import json


class SkillLoader:

    def load(self):

        with open("data/known_skills.json") as f:
            data = json.load(f)

        skills = []
        weights = {}

        for info in data.values():

            weight = info["weight"]

            for skill in info["skills"]:
                skills.append(skill)
                weights[skill] = weight

        return {
            "skills": skills,
            "weights": weights,
        }
