#1974 스도쿠 검증
def check(data):
    nums = [i for i in range(1,10)]
    #가로
    for i in range(9):
        data_check=[]
        for j in range(9):
            data_check.append(data[i][j])
        if nums != sorted(data_check):
            return 0
    #세로
    for i in range(9):
        data_check=[]
        for j in range(9):
            data_check.append(data[j][i])
        if nums != sorted(data_check):
            return 0

    #네모칸
    for k in range(3):
        for l in range(3):
            data_check=[]
            for i in range(3):
                for j in range(3):
                    data_check.append(data[i+3*k][j+3*l])
            if nums != sorted(data_check):
                return 0
    return 1

T=int(input())
for z in range(T):
    in_data = []
    for i in range(9):
        in_data.append(list(map(int, input().split())))
    print("#{} {}".format(z+1,check(in_data)))
