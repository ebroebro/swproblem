#2050 알파벳을 숫자로 변환
word=input()
num_list=[]
for i in word:
    num = ord(i) - ord('A')+1
    num_list.append(num)
result = list(map(str, num_list))
print(' '.join(result))