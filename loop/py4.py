# 4️⃣ Multiplication Table

# Problem:
# Take a number N. Print its multiplication table up to 10.

num1=int(input("Enter any 1st number: "))
# num2=int(input("Enter any 2nd number: "))
for j in range(2,num1+1):
    print("table")
    for i in range(1,10+1):
        table=j*i
        print(j," * ",i,"=",table)
    
    
