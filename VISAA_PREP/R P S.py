vignesh,charan=list(map(str,input().split()))
a_list=["R","P","S"]
if(vignesh,charan in a_list):
    if((vignesh=="R" and charan=="P") or (vignesh=="P" and charan=="S") or (vignesh=="S" and charan=="R")):
        print("Charan")
    elif(vignesh==charan):
        print("NULL")
    else:
        print("Vignesh")
else:
    print("NULL")
    
