# Python If-Else Statements:

# conditional statements can also be done this way for easy understanding

n = int(input())
check = {True: "Not Weird", False: "Weird"}
print(check[(n % 2 == 0) and (n in range(2,6) or n > 20)])
