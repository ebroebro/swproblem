T=int(input())
for z in range(T):
    nums=int(input())
    year = nums//10000
    month = (nums%10000)//100
    date = nums%100
    #print("{:04d}".format(year)) # 04d 이게 4자리 맞춰주는거임
    #print("{:02d}".format(month())
    #print("{:02d}".format(date())
    check = {1:31, 2:28, 3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    if 1<= month <=12:
        if date <1 or check[month] <date
            result = '-1'
        else:
            result = '{:04d}'.format(year)+'/'+'{:02d}'.format(month)+'/'+'{:02d}'.format(date)
    else :
        result = -1
    print("#{} {}".format(z+1,result))