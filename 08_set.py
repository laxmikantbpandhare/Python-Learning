example = set()

example.add(100)
example.add(True)
example.add(3.14)
example.add("Set add")

print(example)

print"length of a set =",len(example)

example.remove(100)

print(example)	


newexample = set([12, False, 1.99, "India"])

print(newexample)
print"length of a set =", len(newexample)
newexample.clear()
print"length after Clear = ", len(newexample)

odd = set([1, 3, 5, 7, 9])
even = set([2, 4, 6, 8, 10])
prime = set([2, 3, 5, 7])

print(odd.union(even))
print(even.union(odd))

print"odd numbers = ", odd
print"even numbers = ", even

print(odd.intersection(even))
print(prime.intersection(even))

print(2 in prime)
print(5 in odd)
print(9 not in even)

