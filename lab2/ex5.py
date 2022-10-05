from statistics import mean


class Student:

    def __init__(self, name, surname, number, grades):
        self.name = name
        self.surname = surname
        self.number = number
        self.grades = grades
        self.aver = self.average()

    def average(self):
        return mean(self.grades)

    def __str__(self):
        return f"{self.name} {self.surname}: {self.aver}"


class Group:
    def __init__(self, *students):
        self.students = []
        for student in students:
            self.students.append(student)

    def five_best(self):
        self.students.sort(key=lambda x: x.aver, reverse=True)
        return self.students


student1 = Student("Kiril", "Slaston", 4, (90, 90, 90, 90))
student2 = Student("Anastasia", "Lepikh", 1, (60, 60, 60, 60))
student3 = Student("Anton", "Mironenko", 2, (80, 80, 80, 80))
student4 = Student("Ilya", "Khurtak", 3, (85, 85, 85, 85))
student5 = Student("Pavlo", "Mogula", 5, (100, 100, 100, 100))

group1 = Group(student1, student2, student3, student4, student5)
print("".join(map(str, group1.five_best())))



