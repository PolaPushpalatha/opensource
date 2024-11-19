def s():
    t=int(input().strip())
    results=[]
    for _ in range(t):
        n,m=map(int,input().strip().split())
        results.append(max(0,n-m))
    for result in results:
        print(result)
s()        
