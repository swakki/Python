# write a Python program to swap first and last element of the list.

# Swap function
def swapList(newList):
	
	# Swapping 
	temp = newList[0]
	newList[0] = newList[-1]
	newList[-1] = temp

    # newList[0], newList[-1] = newList[-1], newList[0]

	return newList
	
newList = [12, 35, 9, 56, 24]
print(swapList(newList))
