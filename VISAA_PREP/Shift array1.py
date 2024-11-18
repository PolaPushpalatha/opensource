def r():
    n=int(input())
    arr=list(map(int,input().split()))
    
    rotated=arr[1:]+[arr[0]]
    print(" ".join(map(str,rotated)))
r()    
