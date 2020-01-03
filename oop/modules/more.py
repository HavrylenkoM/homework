class Candidate:

    def __init__(self, name, mail, technologies, main_skill, main_skill_grade):
        self.name = name
        self.mail = mail
        self.technologies = technologies
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade


class Vacancy:

    def __init__(self, title, main_skill, main_skill_level):
        self.title = title
        self.main_skill = main_skill
        self.main_skill_level = main_skill_level

