# Write a function inside another function.
def outer_function(a, b):

    def inner_function(x, y):
        return x + y
    
    result = inner_function(a, b)
    return result

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum =", outer_function(num1, num2))
