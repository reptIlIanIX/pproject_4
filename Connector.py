from JSONSAVER import json_saver


class Connector:
    def __init__(self):
        pass

    @staticmethod
    def input_text():
        """список всех вакансий в строком виде класса Vacancy"""
        for item in json_saver.from_json_file():
            print(item)

    @staticmethod
    def filter_text():
        """вакансии по keyword в названии в строком виде класса Vacancy"""
        sort_input = input("Впишите название\n")
        for item in json_saver.from_json_file():
            if sort_input.lower() in item.name.lower():
                print(item)

    @staticmethod
    def delete_type():
        """убирает вакансии по типу и представляет в строком виде класса Vacancy"""

        type_input = input("Убрать профессии по типу\n")
        delete_data = json_saver.json_returner(json_saver.vacancy_deleter(type_input))
        for item in delete_data:
            print(item)

    @staticmethod
    def filter_type():
        """отбирает вакансии по типу и представляет в строком виде класса Vacancy"""

        type_input = input("Отобрать профессии по типу\n")
        filter_data = json_saver.json_returner(json_saver.vacancy_chooser(type_input))
        for item in filter_data:
            print(item)

    @staticmethod
    def salary_asker():
        """отбирает вакансии по предложенной пользователем зарплате (от и до) и представляет в строком виде класса
        Vacancy"""

        salary_input_from = int(input('Введите зарплату от '))
        salary_input_to = int(input('Введите зарплату до '))
        for item in json_saver.from_json_file():
            if item.salary_from is not None and item.salary_to is not None:
                if item.salary_from >= salary_input_from and item.salary_from <= salary_input_to and item.salary_to <= salary_input_to:
                    print(item)

    @staticmethod
    def sorted_value():
        """Сортирует вакансии по зарплате и по алфавиту"""

        type_input = input(
            "Сортировать профессии по\n1. Макс. зарплате\n2. Минимальной зарплате\n3. Первые пять по алфавиту\n")
        sorted_max = json_saver.json_returner(json_saver.top_salary())
        sorted_min = json_saver.json_returner(json_saver.min_salary())
        sorted_name = json_saver.json_returner(json_saver.sorted_by_name())
        if type_input == '1':
            for item in sorted_max:
                print(item)
        elif type_input == '2':
            for item in sorted_min:
                print(item)
        elif type_input == '3':
            for item in sorted_name:
                print(item)


connector_d = Connector()
