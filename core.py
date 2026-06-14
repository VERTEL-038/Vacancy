class Vacancy:
    def __init__(self, title, salary, skills):
        self.title = title    #название вакансии
        self.salary = salary  #зарплата
        self.skills = skills  #требуемые навыки

    def __str__(self): #вывод вакансии
        skills_str = ", ".join(self.skills)
        return f"Вакансия: {self.title} | ЗП: {self.salary} | Навыки: {skills_str}"

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