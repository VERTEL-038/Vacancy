#1 Вакансии

class Vacancy:
    def __init__(self, title, salary, skills):
        self.title = title    #название вакансии
        self.salary = salary  #зарплата
        self.skills = skills  #требуемые навыки

    def __str__(self): #вывод вакансии
        skills_str = ", ".join(self.skills)
        return f"Вакансия: {self.title} | ЗП: {self.salary} | Навыки: {skills_str}"


#2 Двусвязный список

class DoublyLinkedNode: #узел двусвязного списка
    def __init__(self, vacancy):
        self.vacancy = vacancy
        self.prev = None
        self.next = None

class DoublyLinkedList: #двусвязный список для хранения всех вакансий
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, vacancy): #добавляет вакансию в конец списка
        new_node = DoublyLinkedNode(vacancy)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def to_list(self): #возвращает список вакансий в порядке от головы к хвосту
        result = []
        current = self.head
        while current:
            result.append(current.vacancy)
            current = current.next
        return result

    def __iter__(self):
        current = self.head
        while current:
            yield current.vacancy
            current = current.next


#3 Бинарное дерево поиска по зарплате

class BSTNode: #узел бинарного дерева поиска по зарплате
    def __init__(self, salary, vacancy):
        self.salary = salary         #зарплата (ключ)
        self.vacancies = [vacancy]   # список вакансий с одинаковой зарплатой
        self.left = None
        self.right = None

class BinarySearchTree: #бинарное дерево поиска по зарплате
    def __init__(self):
        self.root = None

    def insert(self, vacancy): #вставляет вакансию в дерево по ключу зарплата
        salary = vacancy.salary
        if self.root is None:
            self.root = BSTNode(salary, vacancy)
        else:
            self._insert_rec(self.root, vacancy, salary)

    def _insert_rec(self, node, vacancy, salary):
        if salary == node.salary:
            node.vacancies.append(vacancy)
        elif salary < node.salary:
            if node.left is None:
                node.left = BSTNode(salary, vacancy)
            else:
                self._insert_rec(node.left, vacancy, salary)
        else:  # salary > node.salary
            if node.right is None:
                node.right = BSTNode(salary, vacancy)
            else:
                self._insert_rec(node.right, vacancy, salary)

    def find_in_range(self, min_salary, max_salary): #возвращает список вакансий с зарплатой в диапазоне [min_salary, max_salary]
        result = []
        self._range_rec(self.root, min_salary, max_salary, result)
        return result

    def _range_rec(self, node, min_s, max_s, result):
        if node is None:
            return
        if node.salary < min_s:
            self._range_rec(node.right, min_s, max_s, result)
        elif node.salary > max_s:
            self._range_rec(node.left, min_s, max_s, result)
        else:
            result.extend(node.vacancies)
            self._range_rec(node.left, min_s, max_s, result)
            self._range_rec(node.right, min_s, max_s, result)

    def sum_and_count_salaries(self): #рекурсивно вычисляет сумму зарплат и количество вакансий во всем дереве
        return self._sum_count_rec(self.root)

    def _sum_count_rec(self, node):
        if node is None:
            return 0, 0
        sum_sal = node.salary * len(node.vacancies)
        count = len(node.vacancies)
        left_sum, left_cnt = self._sum_count_rec(node.left)
        right_sum, right_cnt = self._sum_count_rec(node.right)
        return sum_sal + left_sum + right_sum, count + left_cnt + right_cnt


#4 ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ

def quick_sort(arr): #быстрая сортировка для списка строк
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def binary_search(sorted_arr, target): #бинарный поиск элемента в отсортированном массиве (возвращает True, если найден)
    left, right = 0, len(sorted_arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_arr[mid] == target:
            return True
        elif sorted_arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

def count_frequencies_sorted(sorted_arr): #из отсортированного массива возвращает список пар (элемент, частота)
    if not sorted_arr:
        return []
    freq = []
    current = sorted_arr[0]
    count = 1
    for i in range(1, len(sorted_arr)):
        if sorted_arr[i] == current:
            count += 1
        else:
            freq.append((current, count))
            current = sorted_arr[i]
            count = 1
    freq.append((current, count))
    return freq

def get_top_skills(skills_list, top_n=5): #принимает список навыков и возвращает топ самых частых навыков
    if not skills_list:
        return []
    sorted_skills = quick_sort(skills_list)
    freq_pairs = count_frequencies_sorted(sorted_skills)
    freq_pairs.sort(key=lambda x: x[1], reverse=True)
    return freq_pairs[:top_n]


#5 ТЕСТОВЫЕ ДАННЫЕ

def generate_test_vacancies(): #возвращает список объектов Vacancy для тестирования
    vacancies_data = [
    ("Python разработчик", 120000, ["Python", "Django", "SQL", "Git"]),
    ("Java разработчик", 130000, ["Java", "Spring", "SQL", "Maven"]),
    ("Data Scientist", 150000, ["Python", "Pandas", "NumPy", "Machine Learning"]),
    ("Frontend разработчик", 110000, ["JavaScript", "React", "CSS", "HTML"]),
    ("DevOps инженер", 140000, ["Docker", "Kubernetes", "Linux", "CI/CD"]),
    ("Аналитик данных", 95000, ["SQL", "Python", "Excel", "Tableau"]),
    ("Python разработчик (Junior)", 80000, ["Python", "Git", "SQL"]),
    ("Backend разработчик", 135000, ["Python", "Django", "PostgreSQL", "REST API"]),
    ("Fullstack разработчик", 145000, ["JavaScript", "React", "Python", "Django"]),
    ("ML Engineer", 160000, ["Python", "TensorFlow", "PyTorch", "Machine Learning"]),
    ("C# разработчик", 125000, ["C#", ".NET", "SQL", "Azure"]),
    ("Android разработчик", 135000, ["Kotlin", "Java", "Android SDK", "Git"]),
    ("iOS разработчик", 140000, ["Swift", "UIKit", "SwiftUI", "REST API"]),
    ("QA Automation Engineer", 115000, ["Python", "Selenium", "TestNG", "Postman"]),
    ("Go разработчик", 155000, ["Go", "PostgreSQL", "Docker", "Microservices"]),
    ("Системный администратор", 100000, ["Linux", "Bash", "Nginx", "Zabbix"]),
    ("Product Manager", 160000, ["Roadmap", "A/B-тесты", "SQL", "Figma"]),
    ("UI/UX дизайнер", 105000, ["Figma", "Adobe XD", "Prototyping", "User Research"]),
    ("Data Engineer", 145000, ["Python", "Spark", "Airflow", "Kafka"]),
    ("Security Engineer", 150000, ["Cybersecurity", "SIEM", "Python", "Linux"])
    ]
    return [Vacancy(title, salary, skills) for title, salary, skills in vacancies_data]


#6 ПОЛЬЗОВАТЕЛЬСКИЙ ИНТЕРФЕЙС

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

def search_by_title(vacancy_list): #поиск точного названия вакансии (быстрая сортировка и бинарный поиск)
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


#7 ОСНОВНАЯ ПРОГРАММА

def main():
    print("Сборщик и анализатор вакансий")
    # Загружаем тестовые данные
    test_vacancies = generate_test_vacancies()
    vacancy_list = DoublyLinkedList()
    bst = BinarySearchTree()
    for vac in test_vacancies:
        vacancy_list.append(vac)
        bst.insert(vac)
    print(f"Загружено {vacancy_list.length} тестовых вакансий.\n")
    # Запускаем интерактивный режим
    interactive_mode(vacancy_list, bst)

if __name__ == "__main__":
    main()
