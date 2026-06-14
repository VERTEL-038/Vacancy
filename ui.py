from core import DoublyLinkedList, Vacancy
from tree import BSTNode
from utils import get_top_skills, quick_sort, binary_search

def print_menu():
    print("Анализатор вакансий - Меню")
    print("1. Показать все вакансии")
    print("2. Поиск вакансий по диапазону зарплат")
    print("3. Поиск вакансии по точному названию")
    print("4. Топ самых частых навыков")
    print("5. Средняя зарплата по всем вакансиям")
    print("6. Добавить новую вакансию")
    print("0. Выход")

def show_all_vacancies(vacancy_list): #выводит все вакансии из двусвязного списка
    vacancies = vacancy_list.to_list()
    if not vacancies:
        print("Нет вакансий.")
        return
    print("\nСписок всех вакансий:")
    for i, v in enumerate(vacancies, 1):
        print(f"{i}. {v.title} | Зарплата: {v.salary} | Навыки: {', '.join(v.skills)}")

def search_salary_range(bst): #поиск вакансий по диапазону зарплат
    try:
        min_s = int(input("Введите минимальную зарплату: "))
        max_s = int(input("Введите максимальную зарплату: "))
        if min_s > max_s:
            print("Ошибка: минимальная зарплата не может быть больше максимальной.")
            return
        result = bst.find_in_range(min_s, max_s)
        if result:
            print(f"\nВакансии с зарплатой от {min_s} до {max_s}:")
            for v in result:
                print(f"  {v.title} — {v.salary}")
        else:
            print("Вакансии не найдены.")
    except ValueError:
        print("Ошибка: введите целые числа.")

def search_by_title(vacancy_list): #поиск вакансии по точному названию (быстрая сортировка и бинарный поиск)
    keyword = input("Введите точное название вакансии для поиска: ").strip()
    if not keyword:
        print("Название не может быть пустым.")
        return
    # Собираем все названия и сортируем
    all_titles = [vac.title for vac in vacancy_list.to_list()]
    sorted_titles = quick_sort(all_titles)
    found = binary_search(sorted_titles, keyword)
    if found:
        print(f"✓ Вакансия '{keyword}' найдена.")
        # Найдём и покажем полную информацию
        for vac in vacancy_list.to_list():
            if vac.title == keyword:
                print(f"  Зарплата: {vac.salary}, Навыки: {', '.join(vac.skills)}")
                break
    else:
        print(f"✗ Вакансия '{keyword}' не найдена.")

def show_top_skills(vacancy_list, top_n=5): #выводит топ самых частых навыков
    all_skills = []
    for vac in vacancy_list:
        all_skills.extend(vac.skills)
    if not all_skills:
        print("Нет навыков для анализа.")
        return
    top = get_top_skills(all_skills, top_n)
    print(f"\nТоп-{top_n} самых частых навыков:")
    for skill, freq in top:
        print(f"  {skill}: {freq} раз(а)")

def show_average_salary(bst): #вычисляет и выводит среднюю зарплату
    total_salary, total_count = bst.sum_and_count_salaries()
    if total_count == 0:
        print("Нет вакансий для расчёта средней зарплаты.")
        return
    avg = total_salary / total_count
    print(f"Средняя зарплата по всем {total_count} вакансиям: {avg:.2f}")

def add_new_vacancy(vacancy_list, bst): #добавляет новую вакансию в список и дерево
    print("Добавление новой вакансии:")
    title = input("Название: ").strip()
    if not title:
        print("Название не может быть пустым.")
        return
    try:
        salary = int(input("Зарплата (число): "))
    except ValueError:
        print("Ошибка: зарплата должна быть целым числом.")
        return
    skills_input = input("Навыки (через запятую): ").strip()
    if skills_input:
        skills = [s.strip() for s in skills_input.split(",") if s.strip()]
    else:
        skills = []
    new_vac = Vacancy(title, salary, skills)
    vacancy_list.append(new_vac)
    bst.insert(new_vac)
    print(f"Вакансия '{title}' успешно добавлена.")

def interactive_mode(vacancy_list, bst): #главный цикл взаимодействия с пользователем
    while True:
        print_menu()
        choice = input("Выберите действие: ").strip()
        if choice == "1":
            show_all_vacancies(vacancy_list)
        elif choice == "2":
            search_salary_range(bst)
        elif choice == "3":
            search_by_title(vacancy_list)
        elif choice == "4":
            show_top_skills(vacancy_list)
        elif choice == "5":
            show_average_salary(bst)
        elif choice == "6":
            add_new_vacancy(vacancy_list, bst)
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")
