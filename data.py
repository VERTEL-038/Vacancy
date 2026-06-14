from core import Vacancy

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
