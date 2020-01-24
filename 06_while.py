# Get an Input from User and sum the numbers from 1 till the
# inputted number

number = int(raw_input("Enter the input number = "))
i = 1
sum = 0
while i <= number:
  sum = sum + i
  i = i + 1
print "Total Sum is = ", sum 
