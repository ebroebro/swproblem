#2309 일곱 난쟁이
height = []
for _ in range(9):
    height.append(int(input()))
seven=[]
#이진수 느낌으로 가보자 1024
for i in range(1<<8,1<<10):
    rslt=[]
    for j in range(9):
        if i & (1<<j): #그 각 자리가 1이 존재하면 그 값을 데려오는거임..
            rslt.append(height[j])
    if len(rslt)==7 and sum(rslt)==100:
        seven=rslt
for i in sorted(seven):
    print(i)