target = [4,1,5,8,2,3,6,9,7,10]

def bubble_sort(array):
    for i in range(0, len(array)):
        swapped = False
        for j in range(len(array)-1, i, -1):
            if array[j] < array[j-1]:
                swap = array[j-1]
                array[j-1] = array[j]
                array[j] = swap
                swapped=True
        if swapped == False:
            break
    return array

print(bubble_sort(target))
