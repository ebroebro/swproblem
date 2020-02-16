data = int(input())
data_list = []
while True:
    data_list.insert(0, data%10)
    data//=10
    print(data_list)
    if data==0:
        break