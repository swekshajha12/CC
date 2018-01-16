def rotateonce(arr):
    if arr:
        element=arr.pop()
        arr=[element]+arr
    return arr
def del_at_index(arr,index):
    del arr[-index]
    return arr
def del_first(arr):
    if arr:
        del arr[0]

def compute(arr,n):
    count=0
    while len(arr)>1:
        count+=1
        arr=rotateonce(arr)
        if len(arr)<count:
            del_first(arr)
        else:
            del_at_index(arr,count)
    return arr
        
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a=compute(a,n)
    print(a[0])
