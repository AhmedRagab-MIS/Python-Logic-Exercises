# Task 4 : Continuous Calculator
# Created by : Ahmed Ragab
# Date : May 12 - 2026
while True :
    num1 =  float (input("Enter Number first : "))
    x = input("Enter operation ")
    num2 = float (input("Enter number second : "))
    if x == "+" :
        print(num1 + num2)
    elif x == "-" :
        print(num1 - num2)
    elif x == "*" :
        print(num1 * num2)
    elif x == "%" :
        print(num1 % num2)
    elif x == "/" :
        print(num1 / num2)
    choice = input("Do you want to continue? (y/n) : ")
    if choice == "n" :
        print("Goodbye!")
        break

