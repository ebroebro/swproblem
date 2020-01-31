#1961.

from pprint import pprint
T=int(input())
for z in range(T):
    n=int(input())
    matrix=[]
    for i in range(n):
        nums = list(map(int,input().split()))
        matrix.append(nums)
    result =[]
    # result=[[] for i in range(n)]
    for i in range(n):
        d90=list()
        d180=list()
        d270=list()
        new_list=[]
        for j in range(n):
            d90.append(matrix[n-j-1][i])
            d180.append(matrix[n-i-1][n-j-1])
            d270.append(matrix[j][n-i-1])
        new_list.append(''.join(list(map(str,d90))))
        new_list.append(''.join(list(map(str, d180))))
        new_list.append(''.join(list(map(str, d270))))
        result.append(new_list)

    rslt =''
    for i in range(n):
        if i !=n-1:
            rslt += ' '.join(result[i])+'\n'
        else:
            rslt += ' '.join(result[i])
    print("#{}".format(z+1))
    print("{}".format(rslt))
