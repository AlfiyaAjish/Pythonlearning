'''
search a sorted array for first occurence of k in n/2 order
'''
arr=[1,1,1,1,2,3,4]
elem=2
low = 0
high = len(arr) - 1
mid = 0
while low <= high:
    mid = (high + low) // 2
    if arr[mid] < elem:
        low = mid + 1
    elif arr[mid] > elem:
        high = mid - 1
    else:
        if arr[mid-1]==elem:
            high=mid-1
        else:
            print('position is',mid+1)
            break

