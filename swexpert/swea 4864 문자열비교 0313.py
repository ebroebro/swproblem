T=int(input())
for z in range(T):
    str1 = input()
    str2=input()
    flag=0
    for i in range(len(str2)-len(str1)+1):
        if str1== str2[i:i+len(str1)]:
            flag=1
            break
    print("#{} {}".format(z+1,flag))