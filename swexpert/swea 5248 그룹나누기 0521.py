#5248 그룹나누기
def find_set(a):
    if a == parent[a]:
        return a
    else:
        return find_set(parent[a])

def Union(a,b):
    parent[find_set(b)] = find_set(a)

t = int(input())
for z in range(t):
    n, m = map(int, input().split())
    parent = [0]*(n+1)

    for i in range(1, n+1):
        parent[i] = i

    Init_Data = list(map(int, input().split()))
    for i in range(m):
        start = Init_Data[2*i]
        end = Init_Data[2*i+1]
        Union(start, end)

    result = []
    for i in range(len(parent)):
        result.append(find_set(i))
    print("#{} {}".format(z+1, len(set(result))-1))