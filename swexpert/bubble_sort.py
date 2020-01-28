def BubbleSort(data):
    for j in range(len(data)-1,0,-1):
        #for i in range(len(data)): #이것도 되는데 굳이 끝까지 해줄필요가 없다는거임
        for i in range(j):
            if i<len(data)-1 and data[i]>data[i+1]:
                data[i],data[i+1]=data[i+1],data[i] #이런식으로 swap이 가능!
    return(data)
data= [18,17 , 12 ,5 ,1]
print(BubbleSort(data))