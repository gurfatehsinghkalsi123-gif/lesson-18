try:
    num = int(input("enter a number: "))
    print(num)
except ValueError as ex:
    print("an exception occured ", ex)