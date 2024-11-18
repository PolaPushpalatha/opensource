n=int(input())
m=[]
for _ in range(n):
    m.append(list(map(int,input().split())))
for j in range(n):
    for i in range(n):
        print(m[i][j], end=" ")
    print()    
