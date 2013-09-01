def run():
    arr = [4,3,6,7,2,1,5]

    for i in range(1,len(arr)):
       itemToCheck = arr[i]
       for j in list(reversed(range(0,i))):
            if itemToCheck < arr[j]:
                temp = arr[j]
                arr[j] = itemToCheck
                arr[j+1] = temp
       print(arr)

if __name__ == "__main__":
    run()
