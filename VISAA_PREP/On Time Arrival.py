def w():
    t=int(input())
    result=[]
    
    for _ in range(t):
        x=int(input())
        if x>=30:
            result.append("YES")
        else:
            result.append("NO")
    for results in result:
        print(results)
w()        
