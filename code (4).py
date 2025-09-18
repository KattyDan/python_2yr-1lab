class Student:
    def __init__(self, name, group, grades):
        self.name = name
        self.group = group
        self.grades = grades
    
    def average_grade(self):
        return sum(self.grades) / len(self.grades)
    
    def is_excellent(self):
        return self.average_grade() >= 4.5

students = []
try:
    with open('students.txt', 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(';')
            if len(parts) == 3:
                name = parts[0]
                group = parts[1]
               
                grades = list(map(int, parts[2].split(',')))
                students.append(Student(name, group, grades))

with open('excellent_students.txt', 'w', encoding='utf-8') as file:
    for student in students:
        if student.is_excellent():
            file.write(f"{student.name} - {student.group}\n")

group_averages = {}
for student in students:
    group_averages[student.group].append(student.average_grade())
    
    for group, grade in group_grade.items():
        print(f"Группа {group}: Средний балл = {sum(grades) / len(grades):.2f}")

