#swea 4676 늘어지는 소리 만들기
T=int(input())
for z in range(T):
    word=list(input())
    h=int(input())
    position=list(map(int,input().split()))
    position.sort(reverse=True)
    for i in range(h):
        word.insert(position[i],'-')
    print("#{} {}".format(z+1,''.join(word)))