#2667 단지번호 붙이기
from pprint import pprint

n=int(input())
map_list =[]
for _ in range(n):
    data = int(input())
    data_list=[]
    for _ in range(n) :
        data_list.insert(0,data%10)
        data//=10
    map_list.append(data_list)

dy = [0,0,1,-1]
dx = [1,-1,0,0]

def finding(x,y):
