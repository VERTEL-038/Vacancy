from core import DoublyLinkedList
from tree import BinarySearchTree
from data import generate_test_vacancies
from ui import interactive_mode

def main():
    print("Сборщик и анализатор вакансий")
    # Загружаем тестовые данные
    test_vacancies = generate_test_vacancies()
    vacancy_list = DoublyLinkedList()
    bst = BinarySearchTree()
    for vac in test_vacancies:
        vacancy_list.append(vac)
        bst.insert(vac)
    print(f"Загружено {vacancy_list.length} тестовых вакансий\n")
    # Запускаем интерактивный режим
    interactive_mode(vacancy_list, bst)

if __name__ == "__main__":
    main()