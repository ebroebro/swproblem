#4522 세상의 모든 팰린드롬

T=int(input())
for z in range(T):
    word=input()
    flag='Not exist'
    char_set=[0 for _ in range(ord('z')-ord('a')+1)]
    for i in range(len(char_set)):
        char_set[i]=chr(i+ord('a'))
    new_word=[]
    def f(post):
        global flag
        if flag=='Exist':
            return
        elif len(new_word) == len(word):
            if new_word == new_word[::-1]:
                flag="Exist"
            return
        elif word[post] in char_set:
            new_word.append(word[post])
            f(post+1)
            new_word.pop()
        elif word[post]=='?':
            for i in range(len(char_set)):
                new_word.append(char_set[i])
                f(post+1)
                new_word.pop()
    f(0)
print("#{} {}".format(z+1,flag))