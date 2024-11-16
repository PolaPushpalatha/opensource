bill_price=int(input())
max_dis=int(max(0.10*bill_price,100))
print(bill_price-max_dis)
