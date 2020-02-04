# tuples

empty_tuple = ()

examp1 = ("a",)  # to make tuple with only one element you need to add comma at the end of the first element.

examp2 = ("a","b")

examp3 = ("a","b","c")

print(empty_tuple)
print(examp1)
print(examp2)
print(examp3)

test = 1,
test1 = 1,2

print(test)
print(test1)

print(type(test))
print(type(test1))

# tuple of age name and knows python

values = (18, "Laxmikant", True)

age = values[0]
name = values[1]
knows_python = values[2]

print("age == ", age) 
print("Name == ", name)
print("knows python", knows_python)

values2 = (18, "Harshal", False)
age, name, knows_python  = values2

print("age == ", age)
print("Name == ", name)
print("knows python", knows_python)


