#Calculator attempt
#ask user for number input and typecast:
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
#ask user for operator and error check
operator = input("Enter an operator: +,-,*,or / : ")
if operator == "+" or operator == "-" or operator == "*" or operator == "/":
    if operator == "+":
        answer = num1 + num2
    elif operator == "-":
        answer = num1 - num2
    elif operator == "*":
        answer = num1 * num2
    elif operator == "/":
        answer = num1 / num2
    print("{:.2f} {} {:.2f} = {:.2f}".format(num1,operator,num2,answer))
else:
    print("Invalid operator")
