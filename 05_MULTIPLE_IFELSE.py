# Equilateral Triangle - All sides are equal.
# Isosceles Triangle - Two sides havw the same length.
# Scalene Triangle - Two sides have the same length.

a = int(raw_input("Enter the length of side a = "))
b = int(raw_input("Enter the length of side b = "))
c = int(raw_input("Enter the length of side c = "))

if a != b and b != c and a != c:
  print("This is an  Scalene Triangle")
elif a == b and b == c:
  print("This is an Equilateral Triangle")
else:
  print("This is an Isosceles Triangle")

