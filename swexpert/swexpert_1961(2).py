#1961. 숫자 배열 회전

from pprint import pprint

#zip 함수
#zip(*iterables)
#복수의 iterable 객체를 모아준다.
#dictionary 느낌이라 같은 index위치에 있는 것 끼리 묶어준다!!
#girls = ['jane', 'iu', 'mary']
# boys = ['justin', 'david', 'kim']
# # list(zip(girls, boys))
# # [('jane', 'justin'), ('iu', 'david'), ('mary', 'kim')]

n=int(input())
matrix=[]
for i in range(n):
    nums = list(map(int,input().split()))
    matrix.append(nums)
result = []


for i in range(3):
    new_matrix = list(zip(*matrix))
    pprint(matrix)


     for j in range(n):
         result.append(''.join(list(map(str, new_matrix[i][::-1]))))


#
# pprint(result)
#
# new_matrix=list(zip(*matrix))
# pprint(new_matrix)
#
# for j in range(n):
#     d90.append(''.join(list(map(str,new_matrix[i][::-1]))))
#     # for j in range(n):
#
# pprint(d90)