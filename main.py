import json
from abc import ABC, abstractmethod

import requests


class API(ABC):
    @abstractmethod
    def get_vacancies(self, vacancy):
        pass

    def format_vacancies(self):
        pass


class HeadHunterAPI(API):
    vacancies = []

    def get_vacancies(self, vacancy):
        response = requests.get(f"https://api.hh.ru/vacancies?text={vacancy}")
        r = response.json()['items']
        for item in r:
            if item['salary'] is None:
                dict = {
                    "name": item['name'],
                    "salary": item['salary'],
                    "requirements": item['snippet']['requirement'],
                    "URL": item['alternate_url']}
            else:
                dict = {
                    "name": item['name'],
                    "salary": {"salary_from": item['salary']['from'], 'salary_to': item['salary']['to']},
                    "requirements": item['snippet']['requirement'],
                    "URL": item['alternate_url']}
            self.vacancies.append(dict)
        return self.vacancies


class SuperJobAPI(API):
    def get_vacancies(self, vacancy):
        pass


response = requests.get(f"https://api.hh.ru/vacancies?text=Python")
r = response.json()['items']

hh_api = HeadHunterAPI()
hh_vacancies = hh_api.get_vacancies("Python")


class Vacancy:
    def __init__(self, vacancy):
        self.vacancy = vacancy
        for item in self.vacancy:
            if item['salary'] is None:
                self.name = item['name']
                self.salary = item['salary']
                self.requirements = item['requirements']
            else:
                self.name = item['name']
                self.salary_from = item['salary']['salary_from']
                self.salary_to = item['salary']['salary_to']
                self.requirements = item['requirements']

    def __repr__(self):
        print(f"{self.__class__.__name__}('{self.name}')")


vac = Vacancy(hh_vacancies)


class JSONABC(ABC):
    @abstractmethod
    def to_json_file(self, vacancies):
        pass


class JSONSaver(JSONABC):
    def to_json_file(self, vacancies):
        with open("vacancies.json", "w", encoding='utf-8') as outfile:
            json.dump(vacancies, outfile, ensure_ascii=False, indent=4)


json_saver = JSONSaver()

json_saver.to_json_file(hh_vacancies)
