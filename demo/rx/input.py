from rx.subjects import Subject

names = []

def onInput(x):
    names.append(x)
    print(names)

subject = Subject()
subject.subscribe(onInput)

while len(names) < 5:
    subject.on_next(input("Enter name: "))
