T = int(input())
for z in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    result = []

    while len(data):
        data = sorted(data)
        result.append(data.pop())
        data = sorted(data, reverse=True)

        result.append(data.pop())
        k = ' '.join(list(map(str, result[:10])))   # int 있는걸 다 str으로 바꿔주고 join 이용해서 인쇄하면댐!!
    print("#{} {}".format(z + 1, k))