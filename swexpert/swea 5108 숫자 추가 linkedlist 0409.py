#5108 숫자 추가 0409
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.dummy = Node('dummy')
        self.current = self.dummy

    def insert(self, idx, num):
        self.current = self.dummy
        for i in range(idx):
            self.current = self.current.next
        new = Node(num)
        new.next = self.current.next
        self.current.next = new

    def find(self, idx):
        self.current = self.dummy
        for i in range(idx+1):
            self.current = self.current.next
        return self.current.data




T=int(input())
for z in range(T):
    n,m,l=list(map(int,input().split()))
    data_list=LinkedList()
    tmp_list=list(map(int,input().split()))

    for i in range(len(tmp_list)):
        data_list.insert(i,tmp_list[i])

    for i in range(m):
        idx,value=list(map(int,input().split()))
        data_list.insert(idx,value)

    print("#{} {}".format(z+1,data_list.find(l)))



