# def factorial(n):
#
#     fact = 1
#
#     for i in range(1, n + 1):
#         fact = fact * i
#
#     print(f"The factorial of {n} is {fact}")
#
# n = int(input("Enter a number to find its factorial: "))
# factorial(n)

def is_even(num):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

num = int(input("Enter a number to check whether it's even or odd: "))
is_even(num)




