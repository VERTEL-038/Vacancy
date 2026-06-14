from core import Vacancy

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
