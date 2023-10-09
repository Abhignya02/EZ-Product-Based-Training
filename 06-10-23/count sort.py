# Counting sort in Python programming
def countingSort(array):
    size = len(array)
    output = [0] * size
    count = [0] * size

    # Store the count of each elements in count array
    for i in range(0, size):
        count[array[i]] += 1
    print(count)
    # Store the cummulative count
    for i in range(1, size):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]


l=list(map(int,input().split()))
countingSort(l)
print("Sorted Array in Ascending Order: ")
print(l)