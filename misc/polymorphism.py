class List():
    def __init__(self, name):
        self.name = name

    def display(self):
        return f"-{self.name}"

class Todo():
    def __init__(self, name):
        self.name = name

    def display(self):
        return f"--{self.name}"

items = [
    List("Groceries"), Todo("Apples"), Todo("Bananas"),
    List("Movies"), Todo("The Godfather"), Todo("Casino"),
    ]

for i in items:
    print(i.display())
