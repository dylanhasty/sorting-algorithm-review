myList = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(myList)
for i in range(1,n):
    insert_index = i
    current_value = myList[i]

    for j in range(i-1, -1, -1):
        if myList[j] > current_value:
            myList[j+1] = myList[j]
            insert_index = j
        else:
            break
    myList[insert_index] = current_value

print(myList)