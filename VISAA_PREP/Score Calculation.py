def cal(t,p):
    final=t//10
    final_score=final*p
    return final_score
t=int(input())
for _ in range(t):
    x,n=map(int,input().split())
    score=cal(x,n)
    print(score)
