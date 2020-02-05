#2605. 줄세우기

#그냥 index에 insert 해주고 뒤집으면 될듯
#학생번호는 그 배열의 인덱스에 +1

n=int(input())
data_list=list(map(int,input().split()))
rslt=[]
for i in range(n): #i+1번 학생은 data_list[i] 번자리에 드간다.
    rslt.insert(data_list[i],i+1)
print(*rslt[::-1])