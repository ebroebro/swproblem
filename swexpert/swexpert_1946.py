#1946. 간단한 압축 풀기
T=int(input())
for z in range(T):
    n=int(input())
    words=[]
    for i in range(n):
        Ci,Ki = input().split()
        Ki=int(Ki)
        words.append(Ci*Ki)
    all_data=''.join(words)
    rslt=''
    for i in range(len(all_data)) :
        rslt+=all_data[i]
        if (i+1)%10 ==0 :  #0부터니까... i+1이 10의배수일때까지
            rslt+='\n'
    print("#{}".format(z+1))
    print(rslt)

