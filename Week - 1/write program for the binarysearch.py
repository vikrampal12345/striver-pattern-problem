def binarysearch(lis, key):
    low = 0
    high = len(lis) - 1
    while low <= high:
        mid = low + (high - low)//2
        if lis[mid] == key:
            return mid
        elif lis[mid] < key:
            low = mid + 1
        elif lis[mid] > key:
            high = mid - 1

        else:
            return "key not found"    

lis = list(map(int, input("Enter the element: ").split()))
key = int(input("Enter the key: "))
print(binarysearch(lis, key))                    