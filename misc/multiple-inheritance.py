class Base:
    def __init__(self, id):
        self.id = id

class A(Base):
    def __init__(self, id, width):
        super().__init__(id)
        self.width = width

class B(Base):
    def __init__(self, id, height):
        super().__init__(id)
        self.height = height

class D(A, B):
    def __init__(self, id, width, height):
        super().__init__(id, width=width, height=height)
        self.length = 300

print(D(123, 100, 200).__dict__)

https://stackoverflow.com/questions/9575409/calling-parent-class-init-with-multiple-inheritance-whats-the-right-way
