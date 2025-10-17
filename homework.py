age = None

try:
    age = int(input("enter your age: "))
except ValueError:
    print("the age should be integer")
else:
    if age < 18:
        print("the age is not valid")
    else:
        print("age is valid")
finally:
    if age is None:
        print("no valid age to check even/odd")
    else:
        if age % 2 == 0:
            print("the age is even")
        else:
            print("the age is odd")