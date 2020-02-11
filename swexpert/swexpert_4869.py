#4869 종이붙이기
#1과 2 로  n만들기
n=int(input())//10
cnt=0
start=0
memo=[]
memos=[]
def find_3(start):
    global cnt,n,memo,memos

    if start>n:
        return
    print(start)
    if start==n:
        cnt+=1
        # memos.append(memo)
        # memo=[]
        return
    for i in range(1,3):
        next=start+i
        # memo.append(i)
        find_3(next)

find_3(start)

print(cnt)
print(memo)
