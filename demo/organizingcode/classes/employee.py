class Employee1:
    name = "Vera"

vera = Employee1()
print(vera.name)

class Employee2:
    def __init__(self, name):
        self.name = name

vera = Employee2("Vera")
chuck = Employee2("Chuck")
print(vera.name)
print(chuck.name)
