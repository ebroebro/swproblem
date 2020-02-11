#2116 주사위 쌓기
num= int(input())
original = []
for i in range(num):
    dice= list(map(int,input().split()))
    no6 = dice.pop()
    dice.insert(3,no6)
    original.append(dice)
# dices = original[:]   #이건 얕은복사라 안됨...
#     dices = copy.deepcopy(original) #깊은 복사 import copy 해줘야해

max_sum=0
for i in range(1,7):
    no=i
    tmp = [1,2,3,4,5,6]
    tmp.remove(no)
    if original[0].index(no) >=3 :
        no = original[0][original[0].index(no)-3]
    else:
        no = original[0][original[0].index(no) + 3]
    tmp.remove(no)
    sum=max(tmp)
    for j in range(1,num):
        tmp = [1, 2, 3, 4, 5, 6]
        tmp.remove(no)
        if original[j].index(no) >=3:
            no = original[j][original[j].index(no) - 3]
        else:
            no = original[j][original[j].index(no) + 3]
        tmp.remove(no)
        sum += max(tmp)
    if max_sum <sum:
        max_sum =sum

print(max_sum)
