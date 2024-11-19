def c():
    n=int(input().strip())
    a=list(map(int,input().strip().split()))
    
    t=sum(a)
    
    l=0
    b=[]
    
    for i in range(n):
        r=t-l-a[i]
        bv=abs(l-r)
        b.append(bv)
        l+=a[i]
    print(*b)
c()
