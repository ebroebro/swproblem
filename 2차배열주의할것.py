##배열에 대해서

from pprint import pprint  #이쁘게 인쇄해줌...

# N= int(input())
field = [[0]*10]*10  #이거는 묶음 단위로 10번을 반복하겠다는 의미 이고
field2= [[0]*10 for i in range(10)] #이거는 2차배열을 만드는거임.
#요거 위에 두개 다름...

field[2][1]=1
# field[2][2]=1
# field2[2][2]=1
pprint(field)
print()
pprint(field2)

#이걸로 보면 좀 더 이해 될수도
a= ['abc' for i in range(3)]
b= ['abc'*3]
print(a)
print(b)