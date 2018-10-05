from itertools import chain

l = [["vera", "chuck"], ["dave"]]
print(list(chain(*l)))
# list compehension
print([name for names in l for name in names])

l2 = {
    '1': ["vera", "chuck"],
    '2': ["dave"]
}
print(list(chain(*l2.values())))
