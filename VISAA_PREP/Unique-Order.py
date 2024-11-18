def r():
    n=int(input())
    arr=list(map(int,input().split()))
    
    seen=set()
    result=[]
    
    for num in arr:
        if num not in seen:
            result.append(num)
            seen.add(num)
    print(" ".join(map(str,result)))
r()    
