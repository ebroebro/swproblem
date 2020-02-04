<<<<<<< HEAD
#7일차 금속막대
n=3
data=[3,4,2,3,4,5]
# data=[1,2,5,1,2,4,4,3]

##나사 세트 받기
data_list1 = []  #수나사
data_list2=[]   #암나사
for i in range(len(data)):
    if i %2:
        data_list2.append(data[i])
    else:
        data_list1.append(data[i])
nasa_all =[]
for i in range(n):
    nasa_all.append([data_list1[i],data_list2[i]])

nasa=[]
for i in range(len(nasa_all)):
    for j in range(2):
        nasa.append(nasa_all[i][j])
print(' '.join(map(str,nasa)))
=======
>>>>>>> 926a73b8e9261cf34db790fd02bb1a78b3bdead4
