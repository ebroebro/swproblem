#1940. 가라 알씨카

T=int(input())
for z in range(T):
    dis = 0
    v = 0
    s = int(input())
    for i in range(s):
        input_data = input()  # 인풋 값이 다르니까 ... 이렇게 변수 따로 주고 하면 될듯!
        if input_data == '0':
            dis += v
        else:
            ga, value = list(map(int, input_data.split()))
            if ga == 1:
                v += value
            elif ga == 2:
                v -= value
                if v < 0:
                    v = 0
            dis += v
    print("#{} {}".format(z+1,dis))