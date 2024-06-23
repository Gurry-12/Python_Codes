
# 1. write a program to print a no is even or not

num = int(input("Enter a number: "))

match num:
    case x if x % 2 == 0:
        print("Even")
    case _:
        print("Odd")

# 2. write a program to print a no is positive or negative

num = int(input("Enter a number: "))
match num:
    case x if x > 0:
        print("Positive")
    case x if x < 0:
        print("Negative")
    case _:
        print("Zero")
    