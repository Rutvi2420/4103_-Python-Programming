"""
3. Function to Calculate Factorial (Using Recursion)
 Implement factorial using:
Normal function
Recursive function
"""
# Normal function to calculate factorial
def factorial_normal(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


num = int(input("Enter a number: "))

if num < 0:
    print("Factorial does not exist for negative numbers")
else:
    print("Factorial (Normal Function) =", factorial_normal(num))

# Factorial Using Recursive Function

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


num = int(input("Enter a number: "))

if num < 0:
    print("Factorial does not exist for negative numbers")
else:
    print("Factorial (Recursive Function) =", factorial_recursive(num))


