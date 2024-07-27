import math


def calculate():
    while True:
        requested_calculation = input("which calculation would you like to make (type exit to exit) ")

        if requested_calculation in ["+", "-", "*", "/"]:
            number1 = float(input("enter your first number "))
            number2 = float(input("enter your second number "))
            if requested_calculation == "+":
                print(number1 + number2)
            elif requested_calculation == "-":
                print(number1 - number2)
            elif requested_calculation == "*":
                print(number1 * number2)
            elif requested_calculation == "/":
                print(number1 / number2)



        elif requested_calculation in ["tan", "cot", "sin", "cos"]:
            number1 = float(input("enter your number "))
            if requested_calculation == "tan":
                print(math.tan(number1))
            elif requested_calculation == "cot":
                print(1 / math.tan(number1))
            elif requested_calculation == "sin":
                print(math.sin(number1))
            elif requested_calculation == "cos":
                print(math.cos(number1))

        elif requested_calculation == "^":
            number1 = float(input("enter your base number "))
            number2 = float(input("enter your exp number "))
            print(pow(number1, number2))
        elif requested_calculation == "%":
            number1 = float(input("enter your dividend number "))
            number2 = float(input("enter your divisor number "))
            print(number1 % number2)
        elif requested_calculation == "exit":
            break
        else:
            print("invalid calculation (only + - / * ^ sin cos tan cot %)"),


calculate()
