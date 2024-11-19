def is_palindrome(s):
    cleaned=s.strip().upper()
    left=0
    right=len(cleaned)-1
    while left<right:
        if cleaned[left]!= cleaned[right]:
            return "FALSE"
        left+=1
        right-=1
    return "TRUE"
try:
    s=input().strip()
    if 1<len(s)<100:
        print(is_palindrome(s))
    else:
        print("FALSE")
except:
    print("FALSE")
    
