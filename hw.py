# 1. What is the output of ‘banana’ > ‘BANANA’?
# a = "banana"
# a = a.upper()
# print(a)



# 2. Check whether 5 is in list of first 5 natural numbers or not. Hint: List => [1,2,3,4,5]
# natnum = [1, 2, 3, 4, 5]
# for i in natnum:
#     i = i+1

# if i == 1:
#     print("5 is in the list of first five natural numbers")
# else:
#     print("5 is not in the list of first five natural numbers")


# 3. Given three integers, print the smallest one. (Three integers should be user input)
# a = int(input("enter integer"))
# b = int(input("enter integer"))
# c = int(input("enter integer"))


# if (a < b) and (a < c):
#     print(f"{a} is smallest among three numbers")
# elif (b < c) and (b < a):
#     print(f"{b} is smallest among three numbers")
# else:
#     print(f"{c} is smallest among three numbers")


# 4. Given a three-digit number. Find the sum of its digits.
# a = int(input("enter integer"))
# b = int(input("enter integer"))
# c = int(input("enter integer"))
# sum = (a+b+c)
# print(f"The sum of three numbers is{sum}")


# 5. Write a program that asks the user for a number in the range of 1 to 12. The program should display the corresponding month, where
# 1 = january, 2 = february, 3 = march, 4 = april, 5 = may, 6 = june, 7 = july, 8 = august, 9 = september, 10 = october, 11 = november, 12 = december.
# #The program should display an error message if the user enters a number that is out of range.


# a = int(input("enter a num(1-12)"))
# if (a == 1):
#     print("January")
# elif (a == 2):
#     print("febuararay")
# elif (a == 3):
#     print("march")
# elif (a == 4):
#     print("April")
# elif (a == 5):
#     print("May")
# elif (a == 6):
#     print("june")
# elif (a == 7):
#     print("julyy")
# elif (a == 8):
#     print("august")
# elif(a == 9):
#     print("september")
# elif(a == 10):
#     print("october")
# elif(a == 11):
#     print("november")
# elif(a == 12):
#     print("december")
# else:
#     print("your input is invalid")


# 6. Given x = 5, what will be the value of x after we run x+=3?
# the value will be 8 as it will be added to the value and final value will be 8
# it wil be taken as x=x+3


# 7. Write a Python Program to Check Prime Number.
# c = 0
# a = int(input("enter a number to check if it is prime or not "))
# for i in range(1, a+1):
#     b = a % i
#     if b == 0:
#         c = c+1
# if c < 3:
#     print("this is prime number")
# else:
#     print("this is composite number")


# 8. A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.

# a = int(input("enter marks in sub 1"))
# b = int(input("enter marks in sub 2"))
# c = int(input("enter marks in sub 3"))
# d = int(input("enter marks in sub 4"))

# total = a+b+c+d
# print(f"the total mraks is {total}")
# percentage = ((total/400)*100)
# print(f"total percentage is {percentage}%")
# if percentage > 80 :
#     print("A")
# elif percentage > 60:
#     print("B")
# elif percentage > 50:
#     print("C")
# elif percentage > 45:
#     print("D")
# elif percentage > 25:
#     print("E")
# else:
#     print("F")


# 9. Take input of age of 3 people by user and determine oldest and youngest among them
# a = int(input("enter age of person 1"))
# b = int(input("enter age of person 2"))
# c = int(input("enter age of person 3"))


# if (a < b) and (a < c):
#     print("person 1is smallest among three")
# elif (b < c) and (b < a):
#     print("person 2 is smallest among three")
# else:
#     print("person 3 is smallest among three")


# if (a > b) and (a > c):
#     print("person 1 is oldest among three")
# elif (b > c) and (b > a):
#     print("person 2 is oldest among three")
# else:
#     print("person 3 is oldest among three")


# 10.  Write a program to check whether a person is eligible for voting or not. (accept age from user)


# a = int(input("Enter your age"))
# if a>=18:
#     print("You are eligible to vote")
# else:
#     print("you are not eligible to vote")


# 11.  Write a program to check whether a number entered by user is even or odd.
# adarsh = int(input("enter a integer"))
# if (adarsh % 2 == 0):
#     print("even")
# else:
#     print("odd")


# 12. Write a program to check whether a number is divisible by 7 or not.
# adarsh = int(input("enter a integer"))
# if (adarsh % 7 == 0):
#   print(f"{adarsh} is divisible by 7")
# else:
# print(f"{adarsh} is not divisible by 7")


# 13. Write a program to display "Hello" if a number entered by user is a multiple of five ,
# otherwise print "Bye".
# adarsh = int(input("enter a integer"))
# if (adarsh % 5 == 0):
#     print(f"{adarsh} is multiple by 5")
# else:
#     print("bye")

"""
14. Write a program to accept percentage from the user and display the grade according to the following criteria:

    Marks                                    Grade
    > 90                                         A
    > 80 and <= 90                    B
    >= 60 and <= 80                  C
    below 60                                 D
"""
# a = int(input("enter marks in sub 1"))
# b = int(input("enter marks in sub 2"))
# c = int(input("enter marks in sub 3"))
# d = int(input("enter marks in sub 4"))

# total = a+b+c+d
# print(f"the total mraks is {total}")
# percentage = ((total/400)*100)
# print(f"total percentage is {percentage}%")
# if percentage > 90 :
#     print("A")
# elif percentage > 80:
#     print("B")
# elif percentage > 60:
#     print("C")
# else:
#     print("D")
"""
15. Accept any city from the user and display monument of that city.
City                                 Monument
Delhi                               Red Fort
Agra                                Taj Mahal
Jaipur                              Jal Mahal
"""

# place = int(input("enter a city number(1 for delhi/2 for Agra/3 for jaipur) "))
# if place == 1:
#     print("The monument for Delhi is Red Fort")
# elif place == 2:
#     print("The monument for Agra is Taj Mahal  ")
# elif place == 3:
#     print("The monument for Jaipur is Jal Mahal  ")


# """
# 16. Write the output of the following if a = 9
        
#     if (a > 5 and a <=10):    
#          print("Hello")    
#     else:    
#         print("Bye")/


# 18. Write a program to check a character is vowel or not.
# a = input("enter a alphabet character")

# if (a == "a") or (a == "e") or (a == "i") or (a == "u") or (a == "o"):
#     print(f"{a} is vowel letter")
# else:
#     print(f"{a} is consonant")


# """"
# 19. Write a program to accept two numbers and mathematical operators and perform operation accordingly.
# Like:
# Enter First Number: 7
# Enter Second Number : 9
# Enter operator : +
# Your Answer is : 16
# """

# num1 = int(input("enter first number"))
# num2 = int(input("enter second number"))
# op = input("enter the sign of rhe operator you want to do between two numbers")
# if op == "+":
#     print(f"The sum of two numbers is {num1+num2}")
# elif op == "-":
#     print(f"The difference of two numbers is {num1-num2}")
# elif op == "*":
#     print(f"The  product of two numbers is {num1*num2}")
# elif op == "/":
#     print(f"The divison of two numbers is {num1/num2}")
# elif op == "//":
#     print(f"The floor division of two numbers is {num1//num2}")
# elif op == "==":
#     num1 == num2
#     print(f"Value of two operators have been updated to same numbers")
# else:
#     print("your given operator is not in the file")
# for i in range(5):
#     print("python")
#  explain range function with example :
# for i in range(20):
#      print("hello world")
# for a in range (20):
#     print("bhumika")

# a="bhumika"
# for i in a:
#     print(i)



# a="bhumika"
# for i in range(7):
#     print(i,"=", a[i])


# for i in range(1,11):
#     print(f"2*{i}={2*i}")

# for i in range(10,0,-1):
#     print(f"2*{i}={2*i}")

# a= "bhumika"
# for i in range(len(a)):
#     print(f"{a[i]}={i}")
#     print(a)

# for i in range (100,0,-5):
#     print(i)


# a="an"
# for i in a:
#     print("a")

# a= [1,2,3] 
# for i in reversed(a):
#     print(i)

# a= "bhumika"
# b=[]
# for i in reversed(a):
#     print(i)
#     b.append(i)
#     print(b)

# original_list=[1,2,3,4]
# reversed_list=[]
# for i in reversed(original_list):
#     reversed_list.append(i)
#     print(reversed_list)


# a=[1,2,3,4]
# b=[5]
# for i in reversed(a):
#     b.append(i)
#     print(b)

# a=(1,2,3,4)
# s=1
# for i in a:
#     s=s+i
# print(s)



# a=(8,2,3,-1,7)
# s=1
# for i in a:
#     s=s*i
# print(s)

# c=0
# a=int(input("enter a num to check if it is prime or not"))
# for i in range(1, a+1):
#     b=a%i
#     if b==0:
#         c=c+1
# if c<3:
#     print(" prime num")
# else:
#     print("composite number")

# if 5>3:
#     print("five is greater than two!")

# for i in range(2):
#     print("outer loop",i)
#     for j in range(3):
#         print("inner loop",j)
# print("rest of code") 

# username=input("enter username:")
# password= input("enter password")
# for i in range(0,3):
#     print("enter your credentials")
#     username1=input("enter ur user name:")
#     password1=input("enter ur password:")
#     if username==username1 and password==password1:
#          print("you are successfully logged.")
#          break
#     else:
#         if(username!=username1 or password!=password1):
#             print("invalid credentials")   
# else:
#     print("3 attempt finished") 

from ast import keyword


# # # 1.
# for i in range(5):
#     for j in range(i):
#         print("*",end="")
#     print("")
    
# for i in range(5,0,-1):
#     for j in range(i):
#         print("*", end="")
#     print("")

for i in range(5):
    for j in range(5):
        print ("*",end="")
    print("") 

# import keyword
# print(keyword.kwlist)

# a=10
# b=30
# c=20
# d=a+c
# print(id(b))
# print(id(d))

# a="s"
# b="p"
# c="sp"
# d=a+b
# print(id(c))
# print(id(d))


# for i in range (1,9):
#     if i%2==0:
#         print(i)

 