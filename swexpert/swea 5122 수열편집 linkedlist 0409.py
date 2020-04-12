#5122 수열편집 0409 linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.dummy = Node('dummy')
        self.current = self.dummy
        self.num_of_data = 0

    def insert(self, idx, num):
        self.current = self.dummy
        for i in range(idx):
            self.current = self.current.next
        new = Node(num)
        new.next = self.current.next
        self.current.next = new
        self.num_of_data += 1

    def pop(self, idx):
        self.current = self.dummy
        for i in range(idx):
            self.current = self.current.next
        self.current.next = self.current.next.next
        self.num_of_data -= 1

    def change(self, idx, num):
        self.current = self.dummy
        for i in range(idx+1):
            self.current = self.current.next
        self.current.data = num

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
        tmp = list(input().split())
        if tmp[0]=='I':
            data_list.insert(int(tmp[1]),int(tmp[2]))
        elif tmp[0]=='C':
            data_list.change(int(tmp[1]),int(tmp[2]))
        elif tmp[0]=='D':
            data_list.pop(int(tmp[1]))
    if data_list.num_of_data>l:
        print("#{} {}".format(z+1,data_list.find(l)))
    else:
        print("#{} -1".format(z + 1))
