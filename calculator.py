try:
    num1 = int(input("Enter the 1st number: "))
    num2 = int(input("Enter the 2nd number: "))
    operator = input("Enter the operator you want to work with (+, -, *, /, //): ")
    if operator == "+":
        print(num1+num2)
    elif operator == "-":
        print(num1-num2)
    elif operator == "*":
        print(num1*num2)
    elif operator == "/":
        print(num1/num2)
    elif operator == "//":
        print(num1//num2)
    else:
        print("It is a wrong operator or out of my reach! ")
except ValueError:
    print("There is an error, you need to provide a number.")
except ZeroDivisionError:
    print("You cannot have a denominator of 0.")
except Exception as t:
    print("Error is :- ", t)
