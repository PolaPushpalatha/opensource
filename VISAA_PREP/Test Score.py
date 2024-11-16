x, a, b = map(int,input().split())
for i in range(x+1):
    total=i*a
    if total==b:
        print("YES")
        break
else:
    print("NO")
        
    
