"""
4. Function with Default Arguments
 Write a function to calculate simple interest.
 Keep rate default as 5%.
"""

def simple_interest(principal, time, rate=5):
    si = (principal * time * rate) / 100
    return si

p = float(input("Enter Principal Amount: "))
t = float(input("Enter Time (in years): "))

print("Simple Interest (Default Rate 5%) =", simple_interest(p, t))

r = float(input("Enter Rate of Interest (or 0 to skip): "))

if r != 0:
    print("Simple Interest (Custom Rate) =", simple_interest(p, t, r))
