# result= lambda n1,n2,n3: n1 + n2 + n3
# print("sum of three valus:",result(10,20,25))

# add_sub= lambda x,y:(x+y,x-y)
# a,b=add_sub(5,2)
# print(a)
# print(b)

# li= [5,7,22,97,54,62,77,23,73,61]
# square_list= list(map(lambda x:x**2,li))
# print(square_list)

# a=[1,2,3]
# b=[3,4,5]
# abc=list(map(lambda x,y:x+y,a,b))
# print(abc)

# data=[1,2,3,4,5,5,6,6,7,9,10]
# var=list(filter(lambda x:x%2==0,data))
# print(var)

from functools import reduce


li=[5,8,10,20,50,100]
sum= reduce((lambda x,y : x+y),li)  
print(sum)