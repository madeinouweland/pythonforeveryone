class Item():
    def __init__(self, name):
        self.name = name

class List(Item):
    def display(self):
        return f"-{self.name}"
    bullet = "+-"

class Todo(Item):
    def display(self):
        return f"--{self.name}"
    bullet = "|+-"

items = [
    List("Groceries"), Todo("Apples"), Todo("Bananas"),
    List("Movies"), Todo("The Godfather"), Todo("Casino"),
    ]

for i in items:
    print(i.display())

print("or...")

for i in items:
    print(f"{i.bullet}{i.name}")
