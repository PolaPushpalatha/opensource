def c(n):
    c3=n//3
    c5=n//5
    c15=n//15
    
    r=c3+c5-c15
    return r
n=int(input())
print(c(n))
