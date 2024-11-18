def m(matrix,n):
    for row in matrix:
        print(" ".join(map(str,row[::-1])))
n=int(input())
matrix=[list(map(int,input().split())) for _ in range(n)]
m(matrix,n)
