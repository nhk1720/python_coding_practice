# Fibonacci Number

num=int(input("Enter any number"))
a=0
b=1

for n in range(num):
    print(a)
    c=a+b
    a=b
    b=c
print("=====Done=====")