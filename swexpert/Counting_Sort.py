def Counting_Sort(A) :
# A [1...n] .. 입력 배열 (0 to k)
# B [1 ..n] .. 정렬된 배열
# C [1 ..k] .. 카운트 배열.
    k=max(A)+1
    C = [0]*k

    for i in range(0, len(A)) :  #카운트하기
        C[A[i]] +=1
    for i in range(1, len(C)): #카운트 누적 시키기
        C[i]+=C[i-1]

    B = [0] * len(A) # 정렬된 배열 초기화

    for i in range(len(A)-1,-1,-1) : #뒤에서 부터 계산해 보겠다.
        B[C[A[i]]-1] = A[i]
        C[A[i]]-=1
    return B
data_list = [0,4,3,2,5,1,3,4,5]
print(Counting_Sort(data_list))