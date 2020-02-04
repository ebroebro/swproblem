#12007 패턴 마디의 길이
# words=input()
# word=[]
# for i in range(len(words)):
#     if words[i] not in word:
#         word.append(words[i])
#     else:
#         if str(word)=='KOREA':
#             print(words[i:i+len(word)])
#             break
#         else:
#             word.append(words[i])
# print(len(word))
T=int(input())
for z in range(T):
    words=input()
    for i in range(1,len(words)): # 아무것도 없는것은 제외하고 해야해
        if words[:i]==words[i:2*i]:
            print("#{} {}".format(z+1,i))
            break