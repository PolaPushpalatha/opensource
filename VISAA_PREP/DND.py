def s():
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    
    num1=0
    num2=0
    
    for num in arr:
        if num%m==0:
            num1+=num
        else:
            num2+=num
    print(num1-num2) 
s()    
