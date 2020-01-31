#1961 숫자 배열 회전

T=int(input())
for z in range(T):
    n=int(input())
    result=[[0]*3 for i in range(n)]
    nums=[]
    for i in range(n):
        nums.append(list(map(int, input().split())))
    # print(nums)

    #90도
    d90=[]
    for j in range(n):
        new_list=[]
        for i in range(n-1,-1,-1):
            new_list.append(nums[i][j])
        d90.append(''.join(list(map(str,new_list))))
    # print(d90)
    #180도
    d180=[]
    for i in range(n-1,-1,-1):
        new_list=[]
        for j in range(n-1,-1,-1):
            new_list.append(nums[i][j])
        d180.append(''.join(list(map(str,new_list))))
    # print(d180)
    #270도
    d270=[]
    for j in range(n-1,-1,-1):
        new_list=[]
        for i in range(n):
            new_list.append(nums[i][j])
        d270.append(''.join(list(map(str,new_list))))
    # print(d270)

    new=[d90,d180,d270]
    # print(new)

    #transpose
    for j in range(n):
        for i in range(3):
            result[j][i]=new[i][j]

    rslt = ''
    for i in range(n):
        rslt +=' '.join(list(map(str, result[i]))) + '\n'

    print("#{}".format(z + 1))
    print(rslt, end="")