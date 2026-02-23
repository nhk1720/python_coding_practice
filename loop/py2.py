# Print Even Numbers

# Problem:
# Take an integer N. Print all even numbers from 1 to N.

number=int(input("Enter any number: "))

for n in range(1,number+1):
    if n%2==0:
        print("Even number:",n)

    else:
        print("Odd number:",n)

print("Loop ending")
