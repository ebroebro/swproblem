#4878 반복문자 지우기

#방법 1 _ 재귀, 점화식 사용하기
def f(n):
    if n <2:
        return 1
    else:
        return f(n-1)+2*f(n-2)

T = int(input())
for z in range(T):
    n=int(input())//10
    print("#{} {}".format(z+1,f(n)))





# #방법2 미리 만들어 두기 case 는 30까지!
# data_list=[0 for _ in range(31)]
# for i in range(31):
#     if i <2:
#         data_list[i]=1
#     else:
#         data_list[i]=data_list[i-1]+2*data_list[i-2]
# T=int(input())
# for z in range(T):
#     n=int(input())//10
#     print("#{} {}".format(z+1,data_list[n]))



