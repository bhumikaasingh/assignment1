# # 1. Create a function with variable length of arguments.

# def func1(*x):
#     for i in x:
#         print(i)

# func1(1, 2, 3, 4, 5)

# """
# 2. Create an inner function to calculate the addition in the following way
# Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return it.
# """

# def outer(a, b):
#     def inner(a, b):
#         return a+b
#     value = inner(a, b)
#     return value+5

# a = int(input("Enter first number"))
# b = int(input("Enter second number"))
# print(outer(a, b))

# """
# 3. Assign a different name to function and call it through the new name
# Below is the function display_student(name, age). Assign a new name show_tudent(name, age) to it and call it using the new name.
# """

# # def display_student(name, age):
# #     print(f"Your name is {name}")
# #     print(f"Your age is {age}")

# # a = input("Enter your name")
# # b = input("Enter your age")
# # show_tudents(name=a, age=b)
# # No idea for solutions
# # SIR LAI SODHNE HO

# # 4. Find the largest item from a given list.
# def largest():
#     lar = 0
#     x = [1, 2, 3, 4, 5, 6, 7, 8]
#     for i in x:
#         if i > lar:
#             lar = i
#     return(lar)

# print(f"Larget number is {largest()}")

# # 5. What is the difference between 10 / 3 and 10 // 3?
# """
# The difference between 10/3 and 10//3 is that 10/3 gives value in floating number or gives the exact 
# number that divides the number(3.33333) but 10//3 does the floor division and gives the value in int format 
# which only gives the value 3.

# """

# # 6. What about two asterisks (**)?
# """
# Two asterisks (**) are taken as power in python. for example:-
# 2**4 is equals to 2*2*2*2
# or is equals to 16 not equal to the value 8
# which is given by 2*4
# """

# # 7. What is the difference between local and global variables?
# """
# The difference between local and global variable is that global variable can be accessed even inside
# function but local variable can only be acessed inside local variable or say it cannot be accessed globally
# or outside the function .local variable is valid only inside the function in which it is kept
# """

# """"
# 8. Write a function called fizz_buzz that takes a number.
# If the number is divisible by 3, it should return “Fizz”.
# If it is divisible by 5, it should return “Buzz”.
# If it is divisible by both 3 and 5, it should return “FizzBuzz”.
# Otherwise, it should return the same number.
# """

# def fizz_buzz():
#     a = int(input("Enter a number"))
#     if a % 3 == 0 and a % 5 == 0:
#         return("FizzBuzz")
#     elif a % 3 == 0:
#         return("Fizz")
#     elif a % 5 == 0:
#         return("buzz")
#     else:
#         return(a)

# print(fizz_buzz())

# """"
# 9. Write a function for checking the speed of drivers. 
# If speed is less than 70, it should print “Ok”.
# if the speed is 80, it should print: “Warning”.
# """

# def speed(distance, time):
#     speed = distance/time
#     if speed < 70:
#         print("OK")
#     elif speed == 80:
#         print('Warning')

# distance = int(input("Enter the distance covered"))
# time = int(input("enter time in hours"))

# # 10. Write a program that prompts the user to input a positive integer.
# # It should then print the multiplication table of that number.

# a = -1
# while a < 0:
#     a = int(input("Enter the positive number you want the multiplicatiom table of :"))
# for i in range(1, 11):
#     print(f"{a} * {i} = {a*i}")

# # 11. Write a program that prompts the user to input an integer and
# # then outputs the number with the digits reversed.
# # For example, if the input is 12345, the output should be 54321.
# c = 0
# a = int(input("Enter a number You want to be reversed"))
# while a > 0:
#     b = a % 10
#     a = a//10
#     c = c*10+b
# print(f"Your reversed number is {c}")

# """"
# 12. Write a python program that return the number of characters in a string. 
# """
# myList = "Parameter"
# count = 0
# for i in myList:
#     count = count+1

# print(f"The length of your string is {count}")

# """
# 13. Write a Python program to multiply all the numbers in a list using while and for loop.
# """
# # while method
# Sample_list = [8, 2, 3, -1, 7]
# a = len(Sample_list)-1
# b = 1
# while a > -1:
#     b = b*Sample_list[a]
#     a = a-1
# print(b)

# # for method
# mult = 1
# for i in Sample_list:
#     mult = mult*i

# print(mult)

# """
# 14. Write a Python program to sum all the numbers in a list using for loop and while loop.
# """

# # while method
# Sample_list = [8, 2, 3, 0, 7]

# a = len(Sample_list)-1
# b = 0
# while a > -1:
#     b = b+Sample_list[a]
#     a = a-1
# print(b)

# # for method
# Sample_list = [8, 2, 3, 0, 7]

# total = 0
# for i in Sample_list:
#     total = total+i
# print(total)

# """"
# 15. Accept string from the user and display only those characters which are 
# present at an even index.
# """
# b = input("Enter a character")
# a = 0
# for i in b:
#     if a % 2 == 0:
#         print(i, end="")
#     a = a+1

# """
# 16. Accept string from the user and display only those characters which are 
# present at an odd index.
# """
# b = input("Enter a character")
# a = 0
# for i in b:
#     if a % 2 != 0:
#         print(i, end="")
#     a = a+1

# """
# 17. Sum : 1 to 10 (or any number) using while loop.
# """
# sum = 0
# a = 0
# while a < 11:
#     sum = sum+a
#     a = a+1
# print(sum)

# """
# 18. Write a Python program to print the even numbers from a given list. 
# """

# Sample_List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in Sample_List:
#     if i % 2 == 0:
#         print(i)

# """
# 19. Write a Python program to print the odd numbers from a given list. 
# """
# Sample_List = [12, 13, 14, 15, 16, 17, 18, 19]
# for i in Sample_List:
#     if i % 2 != 0:
#         print(i)

# """
# 20. Write a program to accept percentage and display the Category according to the  following criteria :
# Percentage  Category
# < 41                         Failed
# >=41 & <55  Fair
# >=55 & <65  Good
# >=65                         Excellent
# """
# per = int(input("Enter Your percentage"))
# if per >= 65:
#     print("Excellent")
# elif(per >= 55):
#     print("Good")
# elif(per >= 41):
#     print("Fair")
# else:
#     print("failed")
