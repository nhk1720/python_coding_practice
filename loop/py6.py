# 👉 Count numbers divisible by 3 and 5 between 1 and N
num = int(input("Enter any number: "))

count3 = 0
count5 = 0
count_both = 0

for n in range(1, num + 1):
    if n % 3 == 0 and n % 5 == 0:
        count_both += 1
    elif n % 3 == 0:
        count3 += 1
    elif n % 5 == 0:
        count5 += 1

print("Divisible by 3 only:", count3)
print("Divisible by 5 only:", count5)
print("Divisible by both 3 and 5:", count_both)














