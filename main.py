from Connector import connector_d
from HH import hh_vacancies
from JSONSAVER import json_saver
from Superjob import spjb_vacancies

json_saver.to_json_file(hh_vacancies, spjb_vacancies)

if __name__ == "__main__":
    intoduction = input(
        "Выберите возможные варианты:\n1. Показать все профессии\n2. Отобрать профессии по keyword\n3. Убрать профессии по типу\n4. Показать профессии по типу\n5. Отобрать профессии по зарплате\n6. Сортировка\n")

    if intoduction == '1':
        connector_d.input_text()
    elif intoduction == '2':
        connector_d.filter_text()
    elif intoduction == '3':
        connector_d.delete_type()
    elif intoduction == '4':
        connector_d.filter_type()
    elif intoduction == '5':
        connector_d.salary_asker()
    elif intoduction == '6':
        connector_d.sorted_value()
    else:
        print("Такого варианта нет")
