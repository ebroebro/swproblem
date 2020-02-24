#진기's 붕어빵
import sys
sys.stdin = open('input.txt','r')


result=[]
T=int(input())
for z in range(T):
    n,m,k=list(map(int,input().split()))
    people = list(map(int,input().split()))
    data_list = [0 for _ in range(max(people)+1)]
    tmp=0
    isPossible ='Possible'
    for i in range(1,len(data_list)):
        data_list[i] = tmp
        if i%m ==0:
            tmp+=k
            data_list[i]=tmp
    # print(data_list)
    people= sorted(people)
    # print(people)

    for i in range(len(people)):
        if data_list[people[i]] < i+1:
            isPossible='Impossible'
            break
    # if z+1 ==131:
    #     print(n,m,k)
    #     print(people)
    #     print(data_list[67])
    #     print(isPossible)
    print("#{} {}".format(z+1,isPossible))
#     result.append(isPossible)
#
# test=[]
# for i in range(T):
#     case1,case2= input().split()
#     if result[i]!=case2:
#         print(i+1)
