def m(n,a):
    ma=0
    c=0
    
    for day in a:
        if day==0:
            c+=1
        else:
            ma=max(ma,c)
            c=0
    ma=max(ma,c)
    return ma
n=int(input())
a=list(map(int,input().split()))
print(m(n,a))
