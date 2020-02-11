#2116 주사위 쌓기
import copy # 깊은 복사 하려고..

num= int(input())
original = []
for i in range(num):
    dice= list(map(int,input().split()))
    no6 = dice.pop()
    dice.insert(3,no6)
    original.append(dice)
# dices = original[:]   #이건 얕은복사라 안됨...
#     dices = copy.deepcopy(original) #깊은 복사 import copy 해줘야해
firstdice = original[0]
max_sum=0
for i in range(6):
    no=i
    sum=0
    for j in range(num):
        dices=copy.deepcopy(original)#깊은 복사 import copy 해줘야해
        for k in range(len(dices[j])):
            if no == dices[j][k]:
                if k <3 :
                    no = dices[j][k+3]
                    dices[j].pop(k+3)
                    dices[j].pop(k)
                    sum+=max(dices[j])
                    break
                else :
                    no = dices[j][k-3]
                    dices[j].pop(k)
                    dices[j].pop(k-3)
                    sum+=max(dices[j])
                    break
    if sum > max_sum:
        max_sum=sum

print(max_sum)
