#4873 반복문자 지우기
T=int(input())
for z in range(T):
    words=list(input())
    length=len(words)
    while True :
        length-=1
        for i in range(len(words)-1):
            if words[i]==words[i+1]:
                del words[i+1]
                del words[i]
                break
        if length ==0:
            break
    print("#{} {}".format(z+1,len(words)))
