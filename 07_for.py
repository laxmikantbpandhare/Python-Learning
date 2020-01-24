# Calculate the square of the number from 1 till entered number

number = int(raw_input("Enter the input number = "))

square = 0
for i in range(0, number):
  square = i * i
  print "number = ", i, "Square = ", i, "*", i,"=", square  
