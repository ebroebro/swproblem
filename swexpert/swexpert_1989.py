#1989 초심자의 회문검사
T=int(input())
for z in range(T):
    word=input()
    new_word=word[::-1]
    if word==new_word:
        result=1
    else:
        result=0

    print("#{} {}".format(z+1,result))