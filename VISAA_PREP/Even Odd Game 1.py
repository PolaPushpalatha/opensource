def g():
    n=input().strip()
    d=sum(int(digit) for digit in n)
    
    if d%2==0:
        print("Vignesh")
    else:
        print("Charan")
g()        
