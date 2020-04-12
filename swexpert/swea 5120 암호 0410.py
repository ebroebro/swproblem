#5120 암호
#길이 넘어가면 앞으로 바꾸기
def f(num,l):
    if num >=l:
        return num-l
    else:
        return num

T=int(input())
for z in range(T):
    n,m,k=list(map(int,input().split()))
    data_list=list(map(int,input().split()))
    post=0
    for i in range(k):
        length = len(data_list)
        a= f(post+m-1,length) #이전 숫자
        b= post+m
        if b >length:
            b-=length
        c= f(post+m,length) # 이후 숫자
        tmp_value = data_list[a]+data_list[c]
        data_list.insert(b,tmp_value)
        post=b
    rslt_list=data_list[::-1]
    print("#{}".format(z+1), end=' ')
    print(*rslt_list[:10])
