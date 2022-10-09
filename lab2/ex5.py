from statistics import mean


class Student:

    def __init__(self, name, surname, number, grades):
        self.name = name
        self.surname = surname
        self.number = number
        self.grades = grades

    def average(self):
        return mean(self.grades)

    def __str__(self):
        return f"{self.name} {self.surname}: {self.average()}"


class Group:
    def __init__(self, max_student=20):
        self.__group = []
        self.max_student = max_student

    def add_student(self, student):
        if isinstance(student, Student) and len(self.__group) < self.max_student:
            for item in self.__group:
                if str(item) == str(student):
                    return item
            self.__group.append(student)

    def five_best(self):
        self.__group.sort(key=lambda x: x.average(), reverse=True)
        return self.__group[:5]


student1 = Student("Kiril", "Slaston", 4, (90, 90, 90, 90))
student2 = Student("Anastasia", "Lepikh", 1, (60, 60, 60, 60))
student3 = Student("Anton", "Mironenko", 2, (80, 80, 80, 80))
student4 = Student("Ilya", "Khurtak", 3, (85, 85, 85, 85))
student5 = Student("Pavlo", "Mogula", 5, (100, 100, 100, 100))
student6 = Student("Pavlo", "Mogula", 6, (100, 100, 100, 100))

group1 = Group()
group1.add_student(student1)
group1.add_student(student2)
group1.add_student(student3)
group1.add_student(student4)
group1.add_student(student5)
group1.add_student(student6)
print("\n".join(map(str, group1.five_best())))
