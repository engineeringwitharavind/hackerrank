# Python If - Else:
n = int(input())
check = {True: "Not Weird", False: "Weird"}
print(check[n % 2 == 0 and (n in range(2,5) or n > 20)])
