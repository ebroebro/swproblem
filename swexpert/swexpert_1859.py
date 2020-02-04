<<<<<<< HEAD
#1859. 백만 장자 프로젝트 (용량 줄여보기..)

=======
#1859. 백만 장자 프로젝트
>>>>>>> 926a73b8e9261cf34db790fd02bb1a78b3bdead4
T=int(input())
for z in range(T):
    n=int(input())
    in_data = list(map(int,input().split()))
<<<<<<< HEAD
    sum=0

=======
    sum = 0
>>>>>>> 926a73b8e9261cf34db790fd02bb1a78b3bdead4
    #모든걸 다 하나씩 산다고 가정.
    #그걸 팔때 가장 이득되는 값만큼만 더해주면 된다!
    #단 음수 값은 무시 해버리면 됨..
    for i in range(n):
        max=0
        for j in range(i,n):
            pro = in_data[j]-in_data[i]
            if max < pro:
                max =pro
        sum+=max  #어차피 max기본값을 0으로 정해놔서 이득이 안되는거는 0을 더하는것과 같다.
<<<<<<< HEAD
    print("#{} {}".format(z+1,sum))


=======
    print("#{} {}".format(z+1,sum))
>>>>>>> 926a73b8e9261cf34db790fd02bb1a78b3bdead4
