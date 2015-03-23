target = [4,1,5,8,2,3,6,9,7,10,11,13,12,15,14,17,16,19,18,20]
target = target * 10
def insertion_sort(array):
    for i in range(0,len(array)):
        for j in range(len(array)-1,i,-1):
            if array[j] < array[j-1]:
                swap = array[j-1]
                array[j-1] = array[j]
                array[j] = swap
    return array

def shell_sort(array):
    sub_sorts = 0
    h=1
    n=len(array)
    while h<n:
        h=3*h+1
        _h = h / 3
        while _h > 0:
            for k in range(0,h):
                subtarget = array[k:n]
                sub_sorts = sub_sorts + 1
                subtarget = insertion_sort(subtarget)
                for a in range(0,len(subtarget)):
                    array[k+a] = subtarget[a]
            _h = _h / 3

    print(sub_sorts)
    return array

print(shell_sort(target))
