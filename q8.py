'''consider a number of lines of integer.given 2 lists A and B, A represents points on number line and B represents points which are center of circles on the number line.
if all circles represented in B  have the same radius , determine the smallest radius for the circles such that all the points in A resides on or inside the circles'''
a=[2,6,12]
b=[4,8]
d=0
if a[0]>b[0]:
    d=a[0]-b[0]
    print(d)
i=0
j=0
while i<len(b) and j<len(a):
    if b[i]>=a[j] and b[i]<=a[j+1]:
        d1=b[i]-a[j]
        d2=a[j+1]-b[i]
        d=max(d1,d2,d)
    elif b[i]>a[j+1]:
        d=max(b[i]-a[j+1],d)
    i+=1
    j+=1
print('minimum radius is'd)
