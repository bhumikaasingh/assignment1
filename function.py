# def login():
#     print("python")
# login()

# def python():
#     print("python")
# python()

# def add():
#     x= 10
#     y=20
#     c=x+y
#     print(c)
# add()

# def login(username,password):
#     print(f"your username is:{username} and your password is:{password}")
# login("sunil","battle")

# def mul(a,b):
#     print(a*b)
# mul(2,3)

# functional argument:

# def pw(x,y):
#     z=x**y
#     print(z)
# pw(5,2)

# keyword argument:

# def show(name,age):
#     print(f"name:{name} age:{age}")
# show(name="sunil",age=20)

# default argument:

# def add(name,age=20):
#     print(name,age)
# add('sunil',age=30)

# variable length argument:

# def show(*num):
#     z=num[0]+num[1]+num[2]
#     print(z)
# show(5,4,3)

# def show(**num):
#     z=num['a']+num['b']+num['c']
#     print(z)
# show(a=5,b=4,c=3)

# def mul(x,y):
#     c=x*y
#     return c
       
# a=int(input("enter a number"))
# b=int(input("enter a number"))

#     # c=a*b
#     # return c
# c=mul(a,b)
# print (c)

# def div1(x,y):
#     div=x/y
#     print(div)
#     return
# a=int(input("enter a number"))
# b=int(input("enter a number"))
# div1(a,b) 

# def bhumi(a,b):
#     sub=a-b
#     return sub
# x=int(input("enter a number"))
# y=int(input("enter a number"))
# c=bhumi(x,y)
# print(c)


# def add(a,b):
#     return a+b
# c=add(2,3)
# print(c)

# def add(a,b):
#     c=a+b
#     d=a-b
#     return c,d
# p=add(24,7)
# print(p)

    
    
# def bhumi(a,b):
#     sub=a-b
#     return sub
# x=int(input("enter a number"))
# y=int(input("enter a number"))
# c=bhumi(x,y)
# print(c)
 
# def disp():
#     def show():
#         print("show function")
#     show()
#     print("disp function")
# disp()

# def disp():
#     def show():
#         print("show function")
#     print("disp function")
#     show()
# disp()

# def disp():
#     def show():
#         return "show function"
#     result = show() + "disp function"
#     return result
# a= disp()
# print(a)

# def inner():
#     x=4
#     print(x)
# inner()

# y=10
# def outer():
#     z=4
#     def inner():
#         x=4
#         z=z+1
#         print(x)
#         print('inside the function y',y)
#     inner()
#     print('z',z)
# outer()

# sum=[8,2,3,0,7]
# def sum1(sum):
#     c=0
#     for number in sum:
#         c= c + number
#     print(c)

# sum1(sum)

# def bhumi():
#     a=int(input("enter a number"))
#     b=int(input("enter a number"))
#     c=int(input("enter a number"))
#     if a>b and a>c:
#         print(a)
#     elif b>c:
#         print(b)
#     else:
#         print(c)
# bhumi()

# def bhumi(a):
#     if a%3==0 and a%5==0:
#         print("fizzbuzz")
#     elif a%5==0:
#         print("buzz")
#     elif a%3==0:
#         print("fizz")
#     else:
#         return(a)
#     return
# b=15
# bhumi(b)
