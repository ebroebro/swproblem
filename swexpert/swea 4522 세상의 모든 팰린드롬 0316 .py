#4522 세상의 모든 팰린드롬

T=int(input())
for z in range(T):
    word=list(input())
    while True:
        if len(word)==1 or len(word)==0:
            flag="Exist"
            break
        else:
            if word[0]=='?' or word[-1]=='?':
                word.pop()
                del word[0]
            else:
                if word[0]==word[-1]:
                    word.pop()
                    del word[0]
                else:
                    flag='Not exist'
                    break
    print("#{} {}".format(z+1,flag))