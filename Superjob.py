import os
from abc import ABC, abstractmethod

import requests


class SJ(ABC):
    @abstractmethod
    def get_vacancies(self):
        pass


class SuperJobAPI:
    """исходные данные запроса собирает в формат json"""

    url = "https://api.superjob.ru/2.0/vacancies/"
    vacancies = []
    api_key: str = os.getenv('X-Api-App-Id')

    def __init__(self, keyword):
        self.headers = {
            "X-Api-App-Id": "v3.h.4486396.98d0a7c326f07c7086640cb3000be0031312cd89"
                            ".967a8499507c217c08e0ba857c56ca68e7cb0729"
        }

        self.params = {"keyword": keyword}

    def get_vacancies(self):
        response = requests.get(url=self.url, headers=self.headers, params=self.params)
        r = response.json()['objects']
        for item in r:
            dict = {
                'id': item['id'],
                "name": item['profession'],
                "salary_from": item["payment_from"],
                'salary_to': item['payment_to'],
                "requirements": item['work'],
                "URL": item['link'],
                "Type": 'SJ'}

            self.vacancies.append(dict)
        return self.vacancies


spjb = SuperJobAPI('Python')
spjb_vacancies = spjb.get_vacancies()
