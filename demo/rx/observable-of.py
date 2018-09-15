from rx import Observable

names = []

def onInput(x):
    names.append(x)
    print(names)

def ObservableInput(amount):
    def inputGenerator():
        for i in range(amount):
            yield input("Enter a name: ")

    return Observable.from_(inputGenerator())

ObservableInput(4).subscribe(onInput)
print("done")
