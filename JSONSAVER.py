import json
import os
from abc import ABC, abstractmethod

from HH import hh_vacancies
from Superjob import spjb_vacancies
from Vacancy import Vacancy


class JSONABC(ABC):
    @abstractmethod
    def to_json_file(self, vacancies_1, vacancies_2):
        pass

    @abstractmethod
    def from_json_file(self):
        pass

    @abstractmethod
    def delete_full_json(self):
        pass


class JSONSaver(JSONABC):
    def to_json_file(self, vacancies_1, vacancies_2):
        """Записывает аргументы (2) в файл json"""
        finished_json = []
        with open("vacancies.json", "w", encoding='utf-8') as outfile:
            for item in vacancies_1:
                finished_json.append(item)
            for item in vacancies_2:
                finished_json.append(item)
            json.dump(finished_json, outfile, ensure_ascii=False, indent=4)

    def from_json_file(self):
        """возвращает файл vacancies.json в виде класса Vacancy"""
        with open("vacancies.json", "r", encoding='utf-8') as outfile:
            vacancies = json.load(outfile)
            return [Vacancy(x) for x in vacancies]

    def json_returner(self, vacancies):
        """возвращает аргумент в виде класса Vacancy"""
        return [Vacancy(x) for x in vacancies]

    def delete_full_json(self):
        """удаляет файл vacancies.json"""
        os.remove("vacancies.json")
        return "json удален"

    @staticmethod
    def vacancy_deleter(type):
        """удаляет из файл vacancies.json вакансии, тип которых представлен в аргументе"""

        new_vacancies = []
        with open("vacancies.json", "r", encoding='utf-8') as outfile:
            vacancies = json.load(outfile)
            for item in vacancies:
                if type not in item['Type']:
                    new_vacancies.append(item)
        return new_vacancies

    @staticmethod
    def vacancy_chooser(type):
        """отбирает из файла vacancies.json вакансии, тип которых представлен в аргументе"""
        new_vacancies = []
        with open("vacancies.json", "r", encoding='utf-8') as outfile:
            vacancies = json.load(outfile)
            for item in vacancies:
                if type in item['Type']:
                    new_vacancies.append(item)
        return new_vacancies

    def top_salary(self):
        """добавляет в новый список вакансии с указанием зп и сортирует их по убыванию зарплаты"""
        new_list = []
        with open("vacancies.json", "r", encoding='utf-8') as outfile:
            vacancies = json.load(outfile)
            for item in vacancies:
                if item['salary_from'] is not None and item['salary_to'] is not None:
                    new_list.append(item)
        new_list.sort(key=lambda x: x["salary_to"], reverse=True)
        return new_list

    def min_salary(self):
        """добавляет в новый список вакансии с указанием зп и сортирует их по возрастанию зарплаты"""

        new_list = []
        with open("vacancies.json", "r", encoding='utf-8') as outfile:
            vacancies = json.load(outfile)
            for item in vacancies:
                if item['salary_from'] is not None and item['salary_to'] is not None:
                    new_list.append(item)
        new_list.sort(key=lambda x: x["salary_from"])
        return new_list

    def sorted_by_name(self):
        """добавляет в новый список 5 вакансий в алфавитном порядке их названия"""

        sorted_vacancies = []
        with open("vacancies.json", "r", encoding='utf-8') as outfile:
            vacancies = json.load(outfile)
            vacancies.sort(key=lambda x: x["name"])
            for item in vacancies[0:5]:
                sorted_vacancies.append(item)
        return sorted_vacancies


json_saver = JSONSaver()
