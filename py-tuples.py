#tuples are immutable in the python. We cannot change the value in the given tuples
#A tuple in Python is similar to a list.
# The difference between the two is that we cannot change the elements of a tuple once
# it is assigned whereas we can change the elements of a list.
numbers = (1, 2, 3, 3, 3)
print(type(numbers))
print(numbers.count(3))
print(numbers.index(3))