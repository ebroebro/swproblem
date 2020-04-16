#트리

arr=list(map(int,input().split())) #부모,자식 노드 쌍
L=[0]*(V+1)
R=[0]*(V+1)
P=[0]*(V+1)

for i in range(0, len(arr),2):
    parent, child =arr[i], arr[i+1]
    if L[parent]: #왼쪽 있으면 오른쪽에 넣기
        R[parent]=child
    else:
        L[parent]=child
    P[child]= parent

def inorder(v):
    if v==0:
        return
    #전위순회
    # print(v, end=' ')
    inorder(L(v))
    #중위순회
    print(v,end=' ')
    inorder(R[v])
    #후위순회
    # print(v, end=' ')
inorder(1)