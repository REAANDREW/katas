target = [4,1,5,8,2,3,6,9,7,10]
target = target * 10

def selection_sort(array):
    for i in range(0,len(array)):
        k = i
        for j in range(i+1, len(array)):
            if array[j] < array[k]:
                k = j
        swap=array[i]
        array[i]=array[k]
        array[k]=swap
    return array

print(selection_sort(target))
                
