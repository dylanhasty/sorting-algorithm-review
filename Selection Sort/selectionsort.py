myList = [64, 34, 25, 5, 22, 11, 90, 12]

n = len(myList)

for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if myList[j] < myList[min_index]:
            min_index =j 
    # swap values
    myList[i], myList[min_index] = myList[min_index], myList[i]

    #swap values by popping lowest value and moving it to the start
    #slower than above swap method due to element shifting
    
    # min_value = mylist.pop(min_index)
    #mylist.insert(i, min_value)
    

print(myList)