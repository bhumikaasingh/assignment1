# a=int(input("enter a year")) 
# if a%4==0:
#     print("leap year")
# else:
#     print("not leap year")
 
# a=int(input("enter a number"))
# b=0
# while a!=0:
#     c= a%10
#     b=b*10+c
#     a=a//10
# print(b)

# n=int(input("enter a number"))

# if n%2==0:
#     print("even")
# else:
#     print("not even")




# for i in range(1,51):
#     if i%2==0:
#         print(i)
# for i in range(50,1,-2):
#     if i%2==0:
#         print(i)

# for i in range(1,51):
#     if i%2!=0:
#         print(i)

# for i in range(1,6):
#     for j in range(i):
#         print(i,end="")
#     print()

# for i in range(0,25):
#     print(i*2+1)

# for i in range(1,51,2):
    # print(i)

# for i in range(1,6):
#     for j in range(i-1):
#         if i==i*1:
#                print(0,end=" ")   
#     print(i)

# for i in range(1,6):
#     i=i*1
#     for j in range(i-1):
#         print(0,end=" ")
#     print(i)

# for i in range(1,6):
#     p= i*8
#     for j in range(i):
#         if (i%2==0):
#             if(j%2==0):
#                 print("0",end=" ")
#             else:
#                 print(p,end=" ")
#         elif(i%2!=0):
#             if(j%2!=0):
#                 print("0",end=" ")
#             else:
#                 print(p,end=" ")
#     print("")

# for i in range(1,6):
#     for j in range(1,i+1):
#         if ((i+j)%2==0):
#             print(8*i,end=" ")
#         else:
#             print(0,end=" ")
#     print() 




# z=input('enter a number')
# if z//2==0:
#     print("it is palindrome")
# else:
# for i in range(-3):
#     print(i)

# data=["sunil","roshan",29]
# for i in data:
#     print(i)
# data=["sunil","roshan",29]
# print(data[0:2])



# data= list(range(0,10,1))
# print(data)
# data=["sunil","roshan",29]
# print(data)
# data.append(9)
# data.append("programming")
# print(data)

# data=["sunil","roshan",29]
# print(data)
# data.insert(2,"battle")
# print(data)
# mixed_list=[{1,2},[5,6,7],{"a":"r"}]
# # number tuple
# number_tuple=(3,4)

# data= ["sunil","roshan",29]
# print(data)
# data[0]=8
# data[1]=10
# print(data)

# delete garna
# data= ["sunil","roshan",29]
# print(data)
# del data[1]
# print(data)

# data=["sunil","roshan",29]
# print(data)
# data.remove(29)
# print(data)
# data=["sunil","roshan"]
# print(data)
# data.pop()
# print(data)
# pop lye last ko data delete garxa 
# data=["sunil","roshan",29]
# data2=["a","b",12]
# print(data+data2)

# data=["sunil","roshan",29]
# data2=[]
# data2=data.copy()
# print(data)
# print(data2)

# data=["sunil","roshan",29]
# data2=["a","b",12]
# data2.extend(data)
# print(data2)

# data=["sunil","roshan",29]
# data.clear()
# print(data)
# data=["sunil","roshan",29]
# print(data)

# a="python"
# b=a.count("p")
# print(b)

# data=("sunil","roshan",29,["sunil","akash",29])
# print(data)
# print(len(data))
# data[3].pop()
# print(data)
# data[3].append("master")
# print(data)
# data[3].remove("akash")
# print(data)
# min and max
# print("maximum is:",max(1,3,2,5,4)) 
# print("maximum is:",min(1,3,2,5,4))

# data=("sunil","roshan"29)
# data2=("sunil","roshan"29)
# print(data+data2)

# write a python to add an item in a tuple.

# a=(1,23,3)
# b=list(a)

# a=(1,2,3)
# print("original tuple",a)
# list1=list(a)
# print("original list",list1)

# data={1,2,3,4,5}
# data.remove(1)

# data= {1,2,3,4,5,6,7,'danish',3.14}
# if 'danish'in data:
#     print('present')
# else:
#     print('not present')


# data={1,2,3,4,5,6}
# data.clear()
# print(data)

# data1={1,2,3,4,5,6}
# print(data1)
# data2=data1.copy()
# print(data2)

# x={'a','b','c'}
# y={'b','d','f'}
# x.update(y)
# print(x)
# union set ma same data xa vanye aak choti matra linxa 
# data1={1,2,3,4}
# data2={3,4,5,6}
# union_set=data1 | data2
# print(union_set)

# intersection set common value lai matra linxa 
# data1={1,2,3,4}
# data2={3,4,5,6}
# intersection_set=data1 & data2
# print(intersection_set)

# data1={1,2,3,4}
# data2={3,4,5,6}
# x=data1.isdisjoint(data2)
# print(x)

# data1={5,6,3,4}
# data2={3,4,5,6}
# c=data1.issubset(data2)
# print(c)

# creating a dictionary vanye paxi yo bata jun ne use garna milxa

# my_dict={}
# my_dict={1:'apple',2:'ball'}
# my_dict={'name':'john',1:[2,4,3]}
# my_dict=dict({1:'apple',2:'ball'})
# my_dict=dict([(1:'apple'),(2:'ball')])

# data={'name':'sunil rawat','age':17}
# print(data)
# for i in data:
#     print(i)
# for i in data.values():
#     print(i)
# for i in data.item():
#     print(i)

# data={'name':'sunil rawat','age':17}
# print(data['name'])
# print(data['age'])

# data={}
# print(data)
# data['name']="sunil rawat"
# data["age"]=18
# print(data)
# data={'name':'sunil rawat','age':17}
# if 'name' in data:
#     print('present')
# else:
#     print("not present")
# if "sunil rawAT"

# data={'name':'sunil rawat','age':17}
# data2={'fev movie':}
# data.update(data2)
# print(data)

# dict1= {'a':"geeks","B":"for",}
# dict2={"B":"geeks"}
# print("orginal dict:")



# data={'name':'sunil rawat','age':17}
# del data["age"]
# print(data)

# data={'name':'sunil rawat','age':17}
# print(data)
# remove_pop=data.pop('age')
# print(remove_pop)

# data1={'name':'sunil rawat','age':17}
# get_data=data1.get('name')
# print(get_data)

# data={'name':'sunil rawat','age':17}
# print(data)
# data.clear()
# print(data)

# rename garnye tarika dict mA yai ho

# a_dict={'a':1,'B':2,'C':3}
# new_key="A"
# old_key="a"
# a_dict[new_key]=a_dict.pop(old_key)
# print(a_dict)
thisdict={
    "brand":"ford",
    "model":"mustang",
     "year": 1964
}
print(thisdict)
thisdict["year"]=2018
print(thisdict)