# 5️⃣ Count Even and Odd Numbers

# Problem:
# Take integer N. Count how many even and odd numbers are between 1 and N.

num=int(input("Enter any number: "))
count1=0
count2=0
for i in range(1,num+1):
    if (i%2==0):
        count1=count1+1
    
    else:
        count2=count2+1
print("Count of even number",count1)
print("Count of odd number",count2)