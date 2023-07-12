class Vacancy:
    def __init__(self, vacancy):
        self.id = vacancy['id']
        self.name = vacancy['name']
        self.salary_from = vacancy['salary_from']
        self.salary_to = vacancy['salary_to']
        self.requirements = vacancy['requirements']

    def __repr__(self):
        return f'{self.__class__.__name__}({self.id})'

    def __str__(self):
        if self.salary_from is not None and self.salary_to is not None:
            return f'Работодатель: {self.name}\nЗарплата от {self.salary_from}\nЗарплата до: {self.salary_to}\nТребования: {self.requirements}\n'
        else:
            return f'Работодатель: {self.name}\nЗарплата неизвестна,\nТребования {self.requirements}\n'
