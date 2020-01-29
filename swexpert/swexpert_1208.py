#1208_ Flattern

def max_dump(case):  # max , min 써도 되는데 일단 안쓰는거 연습
    max =1
    for i in range(len(case)):
        if max < case[i]:
            max=case[i]
    return max

def min_dump(case):
    min= 100 #상자높이 최대가 100임
    for i in range(len(case)):
        if min > case[i]:
            min = case[i]
    return min

for z in range(10):
    dump_num =int(input())
    case = list(map(int, input().split())) #가로 길이는 100으로 고정
    max_num=max_dump(case)
    min_num=min_dump(case)
    diff= max_num - min_num

    for i in range(dump_num):
        if max_num - min_num<=1 :  #평탄화가 완료 되었으면 1을 반환하고 종료
            diff = 1
            break
        case[case.index(max_num)]-=1
        case[case.index(min_num)]+=1
        max_num=max_dump(case)
        min_num=min_dump(case)
        diff=max_num-min_num

    print("#{} {}".format(z+1,diff))