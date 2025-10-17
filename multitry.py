
try:
    num1, num2 = eval(input("enter the two comma seperated numbers: "))
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("division by zero in not allowed")
except SyntaxError:
    print("the numbers should be seperated by comma!")
except:
    print("invalid input")
finally:
    print("don't ask me this will run no matter what")
