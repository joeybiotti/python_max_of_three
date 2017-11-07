#asks the user to enter three numbers
a = input("Enter a number: ")
b = input("Enter another number: ")
c = input("Enter one more number: ")

#checks all three user inputs and says which one is the largest
if a > b and a > c:
    print("The first number is the largest")
elif b > a and b > c:
    print("The second number is the largest")
elif c > a and c > b:
    print("The third number is the largest")
else:
    print("These numbers are all the same...")