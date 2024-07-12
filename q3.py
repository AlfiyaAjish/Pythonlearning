''' You will be given a list of integers, arr, and a single ineteger k.
You must create an array of length k from elements of arr such that its unfairness is minimized.
Call that array arr'.
Unfairness of an array is calculated as max(arr')-min(arr')'''


arr=[1,4,8,2,3]
k=2
arr.sort()
unfair=arr[-1]-arr[0]
sol=[]
i=0
j=i+k

while j<=len(arr):
    maxi=max(arr[i:j])
    mini=min(arr[i:j])
    if((maxi-mini)<unfair):
        unfair=maxi-mini
        sol=arr[i:j]
    i+=1
    j+=1
print(sol)
