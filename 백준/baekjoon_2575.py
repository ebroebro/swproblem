#2575 . 직사각형

#짝수는 x좌표 홀수는 y좌표!
data_list =list(map(int,input().split()))

sq1 = [i for i in data_list[:4]]
sq2 = [i for i in data_list[4:]]

rslt = 'a' #기본 값을 a라 두고,,다른 설정이면 바꿔주는걸로 하자
for i in range(2):
    for j in range(2):
        if sq1[2*i+1] == sq2[2*j+1]:
            if (min(sq1[0],sq1[2]) > max(sq2[0],sq2[2])) and (max(sq1[0],sq1[2]) < min(sq2[0],sq2[2])) or (min(sq1[0],sq1[2]) < max(sq2[0],sq2[2])) and (max(sq1[0],sq1[2]) > min(sq2[0],sq2[2])):
                rslt='b'
        if sq1[2 * i] == sq2[2 * j]:
            if (min(sq1[0], sq1[2]) > max(sq2[0], sq2[2])) and (max(sq1[0], sq1[2]) < min(sq2[0], sq2[2])) or (min(sq1[0], sq1[2]) < max(sq2[0], sq2[2])) and (max(sq1[0], sq1[2]) > min(sq2[0], sq2[2])):
                    rslt='b'

print(rslt)