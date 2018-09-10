name = "Chuck"
age = 30
print(name + " is " + str(age)) # concatenate strings
print("%s is %d" % (name, age)) # string interpolation with %
print("{} is {:d}".format(name, age)) # string interpolation with format function
print(f"{name} is {age:d}") # f-string interpolation since python 3.6
