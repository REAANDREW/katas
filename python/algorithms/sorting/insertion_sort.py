target = [4,1,5,8,2,3,6,9,7,10]

def insertion_sort(array):
    for i in range(0,len(array)):
        for j in range(len(array)-1,i,-1):
            if array[j] < array[j-1]:
                swap = array[j-1]
                array[j-1] = array[j]
                array[j] = swap
    return array

print(insertion_sort(target))
