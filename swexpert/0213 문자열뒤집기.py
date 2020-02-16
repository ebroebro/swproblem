#문자열 뒤집기
words= list('manner maketh man')

for i in range(len(words)//2):
    words[i],words[len(words)-i-1]=words[len(words)-i-1],words[i]

# start=0
# end = len(words)-1
#
# while start<=end :
#     words[start], words[end]=words[end],words[start]
#     start+=1
#     end-=1

print(*words)