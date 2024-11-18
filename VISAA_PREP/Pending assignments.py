X, Y, Z = map(int, input().split())
total_time_needed = X * Y
available_time = Z * 24 * 60
if total_time_needed <= available_time:
    print("YES")
else:
    print("NO")
