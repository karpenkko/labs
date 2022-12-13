from abc import ABC, abstractmethod


class ITeacher(ABC):
    @abstractmethod
    def name(self):
        pass


class Teacher(ITeacher):
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError
        self.__name = value

    def __str__(self):
        return f'Teacher`s name: {self.name}\n'


class ICourse(ABC):
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def topics(self):
        pass


class ILocalCourse(ABC):
    @abstractmethod
    def address(self):
        pass


class IOffsiteCourse(ABC):
    @abstractmethod
    def city(self):
        pass


class LocalCourse(ILocalCourse):
    def __init__(self, name, address, *topics):
        self.name = name
        self.topics = topics
        self.address = address

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError
        self.__name = value

    @property
    def topics(self):
        return self.__topics

    @topics.setter
    def topics(self, value):
        if not isinstance(value, tuple):
            raise TypeError
        self.__topics = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        if not isinstance(value, str):
            raise TypeError
        self.__address = value

    def __str__(self):
        return f'Course`s name: {self.name}\nTopics: {self.topics}\nAddress: {self.address}'


class OffsiteCourse(IOffsiteCourse):
    def __init__(self, name, city, *topics):
        self.name = name
        self.topics = topics
        self.city = city

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError
        self.__name = value

    @property
    def topics(self):
        return self.__topics

    @topics.setter
    def topics(self, value):
        if not isinstance(value, tuple):
            raise TypeError
        self.__topics = value

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        if not isinstance(value, str):
            raise TypeError
        self.__city = value

    def __str__(self):
        return f'Course`s name: {self.name}\nTopics: {self.topics}\nCity: {self.city}'


class ICourseFactory(ABC):
    @abstractmethod
    def add_teacher(self, name):
        pass

    @abstractmethod
    def add_localcourse(self, name, address, *topics):
        pass

    @abstractmethod
    def add_offsitecourse(self, name, city, *topics):
        pass


class CourseFactory(ICourseFactory):
    def add_teacher(self, name):
        return Teacher(name)

    def add_localcourse(self, name, address, *topics):
        return LocalCourse(name, address, *topics)

    def add_offsitecourse(self, name, city, *topics):
        return OffsiteCourse(name, city, *topics)


class Schedule:
    __lessons = {}

    def add_lesson(self, teacher, course):
        lesson = {course.name: teacher.name}
        self.__lessons.update(lesson)

    def get_lesson(self, course):
        return self.__lessons[course.name]

    def show(self):
        return self.__lessons


factory1 = CourseFactory()
teacher1 = factory1.add_teacher('Pinchuk Anton')
localCourse1 = factory1.add_localcourse('Python', 'Shevchenko str. 50', 'topic1', 'topic2', 'topic3')
teacher2 = factory1.add_teacher('Myronenko Olesya')
offsiteCourse1 = factory1.add_offsitecourse('Databases', 'Chernihiv', 'topic1', 'topic2', 'topic3')
print(localCourse1)
print(teacher1)
print(offsiteCourse1)
print(teacher2)

schedule1 = Schedule()
schedule1.add_lesson(teacher1, localCourse1)
schedule1.add_lesson(teacher2, offsiteCourse1)
print(schedule1.show())
lesson1 = schedule1.get_lesson(localCourse1)
print(lesson1)

