myList = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(myList)

for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
        if myList[j] > myList[j + 1]:
            myList[j], myList[j + 1] = myList[j + 1], myList[j]
            swapped = True
    
    # use swapped bool to check if array is fully sorted after each iteration
    # not swapped means no swaps were performed, so array is sorted
    if not swapped:
        break

print(myList)