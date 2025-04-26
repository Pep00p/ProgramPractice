class Epmloyee:  # Базовый класс для сотрудника (опечатка в названии: должно быть Employee)
    def __init__(self, name: str, salary: int):  # Конструктор принимает имя и зарплату
        self.name = name  # Сохраняем имя
        self.salary = salary  # Сохраняем зарплату

    def GetInfo(self):  # Метод возвращает информацию о сотруднике
        return f"Имя сотрудника: {self.name}, зарплата: {self.salary}"

    def CalculateAnnualSalary(self):  # Метод возвращает годовую зарплату
        return self.salary * 12


class Manager(Epmloyee):  # Класс Manager наследуется от Epmloyee
    def __init__(self, name, salary, team_size: int):  # Конструктор принимает имя, зарплату и размер команды
        super().__init__(name, salary)  # Вызов конструктора родителя
        self.team_size = team_size  # Сохраняем размер команды

    def GetInfo(self):  # Переопределённый метод, добавляет информацию о команде
        return f"Имя сотрудника: {self.name}, зарплата: {self.salary}, размер команды: {self.team_size}"


employee = Epmloyee("FDGDFGD", 120000)  # Создаём экземпляр сотрудника
print(employee.GetInfo())  # Выводим информацию о сотруднике
print(employee.CalculateAnnualSalary())  # Выводим годовую зарплату

manager = Manager("fdgdregtr", 200000, 124)  # Создаём экземпляр менеджера
print(manager.GetInfo())  # Выводим информацию о менеджере
print(manager.CalculateAnnualSalary())  # Выводим годовую зарплату


class Shape():  # Базовый класс для геометрической фигуры
    def GetArea(self):  # Абстрактный метод для площади
        raise NotImplementedError("Метод GetArea должен быть переопределён в подклассе.")

    def GetInfo(self):  # Метод возвращает тип фигуры
        return f"тип фигуры: {self.__class__.__name__}"


class Rectangle(Shape):  # Класс прямоугольника, наследуется от Shape
    def __init__(self, width, height):  # Конструктор принимает ширину и высоту
        self.width = width  # Сохраняем ширину
        self.height = height  # Сохраняем высоту

    def GetArea(self):  # Метод возвращает площадь прямоугольника
        return self.width * self.height

    def GetInfo(self):  # Метод возвращает тип фигуры и её параметры
        return f"{super().GetInfo()}, ширина: {self.width}, высота: {self.height}"


class Circle(Shape):  # Класс круга, наследуется от Shape
    def __init__(self, radius):  # Конструктор принимает радиус
        self.radius = radius  # Сохраняем радиус

    def GetArea(self):  # Метод возвращает площадь круга
        return 3.14 * (self.radius ** 2)

    def GetInfo(self):  # Метод возвращает тип фигуры и её параметры
        return f"{super().GetInfo()}, радиус: {self.radius}"


treyg = Rectangle(4, 5)  # Создаём прямоугольник
print(treyg.GetInfo())  # Выводим информацию о прямоугольнике
print(treyg.GetArea())  # Выводим площадь прямоугольника

circle = Circle(3)  # Создаём круг
print(circle.GetInfo())  # Выводим информацию о круге
print(circle.GetArea())  # Выводим площадь круга
