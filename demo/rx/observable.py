from rx import Observable

source = Observable.of("Vera", "Chuck", "Dave")
source.subscribe(lambda x: print(x)) # call by need. data is pushed when subscribed to it
