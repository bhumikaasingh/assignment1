# x=10
# def outer():
#     x=4
#     def inner():
#         x=8
#         print(x)
#         print("inside the function y",)
#     inner()
#     print("z",)
# outer()

def outer():
    x="local"
    def inner():
        nonlocal x 
        x="nonlocal"
        print("inner",x)
    print(x)
    inner()
    print('outer',x)
outer()