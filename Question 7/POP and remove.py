# Illustrate difference between POP and remove practically

list1 = [10, 20, 30, 40, 50]

removed_element = list1.pop(2) 
print("After pop(2):", list1)
print("Element removed using pop():", removed_element)

list1.remove(40)   
print("After remove(40):", list1)

