#.1 ADD
#.2 SUBTRACT
#.3 MULTIPLY
#.4 DIVIDE
from ast import Add, Num, operator
from math import e


print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")

operator= input()
if operator == "1":
   Num1 = input("Enter first number:")
   Num2= input("Enter second number: ")
   print("The sum is " + str(int(Num1) + int(Num2)))


elif operator == "2":
    Num1 = input("Enter first number:")
    Num2= input("Enter second number: ")
    print("The sum is" + str(int(Num1) - int(Num2)))
      
elif operator =="3":
    Num1 = input("Enter the first number:")
    Num2 = input("Enter the second number:")
    print("The sum is" + str(int(Num1) * int(Num2)))

elif operator == "4":
    Num1 = input("Enter the first number:")
    Num2 = input("Enter the second number:")
    print("The sum is" + str(int(Num1) / int(Num2)))
                
else:
                    print("Invalid Entry")

