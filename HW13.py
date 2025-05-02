class Employee:
    MIN_SALARY = 50000
    _id_counter = 1

    def __init__(self, name, salary):
        self.name = name
        self._id = Employee._id_counter
        Employee._id_counter += 1
        self._salary = None
        self.set_salary(salary)

    def get_salary(self):
        return self._salary

    def set_salary(self, value):
        if value >= self.MIN_SALARY:
            self._salary = value
        else:
            print(f"Salary must be at least {self.MIN_SALARY} KZT")

    def get_id(self):
        return self._id


class CurrencyAccount:
    USD_TO_KZT = 450

    def __init__(self, usd_balance):
        self._usd_balance = usd_balance

    @property
    def balance_usd(self):
        return self._usd_balance

    @balance_usd.setter
    def balance_usd(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._usd_balance = value

    @property
    def balance_kzt(self):
        return self._usd_balance * self.USD_TO_KZT

    @balance_kzt.setter
    def balance_kzt(self, value_kzt):
        if value_kzt < 0:
            raise ValueError("Balance cannot be negative")
        self._usd_balance = value_kzt / self.USD_TO_KZT


class Transport:
    def calculate_eta(self, distance_km):
        raise NotImplementedError("Subclasses must implement this method")

class Truck(Transport):
    def calculate_eta(self, distance_km):
        speed_kmph = 60
        return distance_km / speed_kmph

class Plane(Transport):
    def calculate_eta(self, distance_km):
        speed_kmph = 800
        return distance_km / speed_kmph

class Drone(Transport):
    def calculate_eta(self, distance_km):
        speed_kmph = 100
        return distance_km / speed_kmph


emp1 = Employee("Aigerim", 70000)
emp2 = Employee("Daniyar", 55000)

print(f"Employee 1: {emp1.name}, ID: {emp1.get_id()}, Salary: {emp1.get_salary()} KZT")
print(f"Employee 2: {emp2.name}, ID: {emp2.get_id()}, Salary: {emp2.get_salary()} KZT")


acc = CurrencyAccount(usd_balance=100)
print(f"Balance in USD: {acc.balance_usd}")
print(f"Balance in KZT: {acc.balance_kzt}")

acc.balance_kzt = 90000
print(f"New balance in USD (after setting KZT): {acc.balance_usd}")

distance = 300 

vehicles = [Truck(), Plane(), Drone()]
for vehicle in vehicles:
    eta = vehicle.calculate_eta(distance)
    print(f"{vehicle.__class__.__name__}  for {distance} km: {eta:.2f} hours")