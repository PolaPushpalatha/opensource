def r():
    n=int(input().strip())
    mn=-2**31
    ma=2**31-1
    
    sign=-1 if n<0 else 1
    n=abs(n)
    rn=int(str(n)[::-1])*sign
    if rn <mn or rn>ma:
        print(0)
    else:
        print(rn)
r()        
    
