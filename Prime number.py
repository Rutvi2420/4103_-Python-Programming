# Program to print prime numbers from 1 to 50

print("Prime numbers between 1 and 50 are:")

for num in range(1, 51):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=" ")
