X,N=map(int,input().split())
num_p=(N+99)//100
if(num_p<=X):
    print("0")
else:
    print(num_p-X)
    
