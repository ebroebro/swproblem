#2005 파스칼의 삼각형

T=int(input())
for z in range(T):
    n=int(input())
    nums=[[0]*(i+1) for i in range(n)] #2차원 배열 제발 중요함...
    result=''
    for i in range(n):
        for j in range(i+1):
            if i==j or j==0:
                nums[i][j]=1
            else:
                if i>0 and j>0:
                    nums[i][j]= nums[i-1][j]+nums[i-1][j-1]
        result+=' '.join(list(map(str,nums[i])))+'\n'
    print("#{}".format(z+1))
    print(result,end='')