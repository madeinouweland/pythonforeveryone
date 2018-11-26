class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # shows name, salary instead of <__main__.Employee object at 0x10d98a6d8>
    def __str__(self):
        return f"{self.name}, {self.salary}"

e = Employee("Vera", 34254)
print(e)
