# ix. Find maximum element in List1

list1 = ['physics', 'chemistry', 1997, 2000]

numbers = [x for x in list1 if isinstance(x, int)]

maximum = max(numbers)

print("Maximum element in list1:", maximum)
