# Sum of First N Numbers

# Problem:
# Take an integer N. Calculate and print the sum of numbers from 1 to N.

number= int(input("Enter any number: "))
count=0
for i in range(1,number+1):
    count=count+i
print("sum of natural number: ",count)