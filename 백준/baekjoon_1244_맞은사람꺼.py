num_switch=int(input())
s = [0]+ input().split()
for _ in range(int(input())):
    data = list(map(int,input().split()))
    if data[0] == '1':
        i = data[1]
        while(i<num_switch +1):
            s[i]=1-s[i]
            i+=data[1]
    else:
        i = data[1]
        s[i]=1-s[i]
        j=1
        while(i-j >0 and i+j <num_switch+1 and s[i+j] == s[i-j]):
            s[i+j]=1-s[i+j]
            s[i-j]=1-s[i-j]
            j+=1
for i,e in enumerate(s[1:]):
    if i and not(i%20):
        print()
    print(e,end=" ")