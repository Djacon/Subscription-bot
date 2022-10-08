import json

DEFAULT = 'https://getcourse.ru/'


class COURSES:
    def __init__(self, filename: str):
        self.filename = filename
        self._courses = []
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                self._courses = json.load(f)
        except FileNotFoundError:
            with open(filename, 'w') as f:
                f.write('[]')

    def addCourse(self):
        index = len(self._courses) + 1
        self._courses.append([f'Курс {index}-й', 'Здесь будет расположено'
                              f' описание {index}-ого Курса', DEFAULT])
        self._save()

    def getCourses(self):
        return self._courses

    def getCourse(self, id: int):
        return self._courses[id]

    def editCourse(self, id: int, index: int, value: str):
        self._courses[id][index] = value
        self._save()

    def deleteCourse(self, index: int):
        self._courses.pop(index)
        self._save()

    def _save(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self._courses, f, ensure_ascii=False)


DB = COURSES('courses.json')
