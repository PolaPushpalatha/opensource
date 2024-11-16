N=input()
count=1
r=[]
for i in range(1,len(N)):
    if N[i]==N[i-1]:
        count+=1
    else:
        r.append (N[i-1] + str(count))
        count=1
r.append(N[-1] +str(count))
print(''.join(r))
        
        
