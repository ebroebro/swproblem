#햄버거 다이어트 5215
def backtrack(a, k, input, s1, s2):
    global max,max_num
    if k == input:
        if s1 <= max_num and max <s2:
            max = s2
            rslt = []
            for i in range(input):
                if a[i] == 1:
                    rslt.append(tasty[i])
            rslt_list.append(rslt)
    else:
        if s1 <= max_num :
            a[k] = 0
            backtrack(a, k + 1, input, s1, s2)
            a[k] = 1
            backtrack(a, k + 1, input, s1 + cal[k], s2 + tasty[k])

T= int(input())
for z in range(T):
    rslt_list=[]
    max = 0
    n, max_num =list(map(int,input().split()))
    tasty = []
    cal=[]
    for _ in range(n):
        a,b = list(map(int,input().split()))
        tasty.append(a)
        cal.append(b)


    a=[0]*len(cal)


    backtrack(a,0,len(cal),0,0)
    # print(rslt_list)

    for i in range(len(rslt_list)):
        if max < sum(rslt_list[i]):
            max=sum(rslt_list[i])

    print("#{} {}".format(z+1,max))
