from rx.subjects import Subject

subject = Subject()
subject.on_next("Vera")
subject.subscribe(lambda x: print(x))
subject.on_next("Chuck")
subject.on_next("Dave")
