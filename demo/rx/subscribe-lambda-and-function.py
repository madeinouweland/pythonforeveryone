from rx.subjects import Subject

def onNext(name):
    print(name)

subject = Subject()

subject.subscribe(onNext) # subscribe using a function
subject.subscribe(lambda x: print(x)) # subscribe using a lambda

subject.on_next("Vera")
subject.on_next("Chuck")
subject.on_next("Dave")
