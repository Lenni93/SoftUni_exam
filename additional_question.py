# rows = int(input("Enter the number of rows: "))
#
# for i in range(1, rows + 1):
#     print("*" * i)
# Pattern 1: Right-angled Triangle
# Write a Python program that prints a right-angled triangle pattern. The number
# of rows should be specified by the user. For example, if the user enters 5, the output should look like this:

# size = int(input("Enter the size of the square: "))
#
# for i in range(size):
#     if i == 0 or i == size - 1:
#         print("*" * size)
#     else:
#         print("*" + " " * (size - 2) + "*")
# Pattern 2: Square with Hollow Center
# Write a Python program that prints a square pattern with a hollow center. The program should take the size of the
# square as input from the user. For example, if the user enters 5, the output should look like this:
height = int(input("Enter the height of the diamond: "))

for i in range(1, height + 1):
    if i <= height // 2 + 1:
        print(" "*(height//2+1-i) + "*"*(2*i-1))
    else:
        print(" "*(i-height//2-1) + "*"*(2*(height-i)+1))
# #Pattern 3: Diamond
# Write a Python program that prints a diamond pattern. The program should take the number of rows (height)
# for the diamond from the user. For example, if the user enters 5, the output should look like this:
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
#
#
# print(factorial(5))
#
# # 120 is factorial number of 5
# # 720 is factorial number of 6
# # The factorial of 6 is calculated as below:
# # n = 6
# # 6! = 6 × 5 × 4 × 3 × 2 × 1
# # 6! = 720
#   1*2*3*4*5 = 120
# def func(a, b):
#     return a ** b
#
#
# result = func(2, func(2, 2))
# print(result)
# # output 16

# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# result = fibonacci(2)
# print(result)
# # 5
# # fibonacci table
# # F0	F1	F2	F3	F4	F5	F6	F7	F8	F9	F10	F11	F12	F13	F14	F15	F16	F17	F18	F19
# # 0	1	1	2	3	5	8	13	21	34	55	89	144	233	377	610	987	1597	2584	4181