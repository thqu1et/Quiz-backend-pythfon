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

# def is_even(num):
#     if num % 2 == 0:
#         print(f"{num} is even")
#     else:
#         print(f"{num} is odd")
#
# num = int(input("Enter a number to check whether it's even or odd: "))
# is_even(num)

def remove_duplicates(lst):
    new_list = []
    for item in lst:
        if item not in new_list:
            new_list.append(item)
    return new_list

lst = input("Enter a list of elements separated by commas: ").split(",")
new_lst = remove_duplicates(lst)
print("List with duplicates removed:", new_lst)




