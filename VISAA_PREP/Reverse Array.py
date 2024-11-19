def r():
    n=int(input().strip())
    arr=list(map(int,input().strip().split()))
    r=arr[::-1]
    print(*r)
r()    
