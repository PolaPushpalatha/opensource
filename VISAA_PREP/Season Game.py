N=int(input())
spring=[3, 4, 5]
summer=[6, 7, 8]
atumn=[9, 10, 11]
winter=[12, 1, 2]
if(N>12):
    print("Invalid")
elif(N in spring):
    print("Spring")
elif(N in summer):
    print("Summer")
elif(N in atumn):
    print("Autumn")
else:
    print("Winter")
    
