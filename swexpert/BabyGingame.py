num = int(input())
cnt = [0]*10

for i in range(6) :
    no = num%10
    cnt[no]+=1
    num //=10

tri=0
for i in range(10):
    if(cnt[i]>=3):
        cnt[i]-=3
        tri+=1

run=0
for i in range(8):
    if(cnt[i]>=1) and (cnt[i+1]>=1) and (cnt[i+2]>=1):
        cnt[i]-=1
        cnt[i+1] -= 1
        cnt[i+2] -= 1
        run+=1

if (run + tri)==2:
    print("Baby Gin")
else:
    print("Lose")