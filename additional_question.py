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