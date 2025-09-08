#Merge sort implemented without recursion
def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

def mergeSort(arr):
    step = 1 #start with sub-arrays of len 1
    length = len(arr)

    while step < length:
        for i in range(0, length, 2 * step):
            left = arr[i:i + step]
            right = arr[i + step:i + 2 * step]

            #W3Schools uses incorrect indentation starting here,
            #so their version doesn't sort properly
            merged = merge(left, right)

            #put merged array back into initial array
            for j, val in enumerate(merged):
                arr[i + j] = val

        step *= 2 #Double sub-array size for next iteration

    return arr

myList = [3, 7, 6, -10, 15, 23.5, 55, -13]
mySortedList = mergeSort(myList)
print("Sorted array:", mySortedList)