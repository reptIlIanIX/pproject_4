import requests
from abc import ABC, abstractmethod


class HH(ABC):
    @abstractmethod
    def get_vacancies(self, v):
        pass



class HeadHunterAPI(HH):
    vacancies = []

    def get_vacancies(self, vacancy):
        """исходные данные запроса собирает в формат json"""

        response = requests.get(f"https://api.hh.ru/vacancies?text={vacancy}")
        r = response.json()['items']
        for item in r:
            if item['salary'] is None:
                dict = {
                    'id': item['id'],
                    "name": item['name'],
                    "salary_from": None,
                    'salary_to': None,
                    "requirements": item['snippet']['requirement'],
                    "URL": item['alternate_url'],
                    "Type": 'HH'}
            else:
                dict = {
                    'id': item['id'],
                    "name": item['name'],
                    "salary_from": item['salary']['from'],
                    'salary_to': item['salary']['to'],
                    "requirements": item['snippet']['requirement'],
                    "URL": item['alternate_url'],
                    "Type": 'HH'}
            self.vacancies.append(dict)
        return self.vacancies


hh_api = HeadHunterAPI()
hh_vacancies = hh_api.get_vacancies("Python")
