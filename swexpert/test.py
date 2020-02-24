n, m, k = list(map(int, input().split()))
people = list(map(int, input().split()))
data_list = [0 for _ in range(max(people) + 1)]
tmp = 0
isPossible = 'Possible'
for i in range(1,len(data_list)):
    data_list[i] = tmp
    if i % m == 0:
        tmp += k
        print(i)
        break
# print(data_list)
people = sorted(people)
# print(people)
print(people)
for i in range(len(people)):
    if data_list[people[i]] < i + 1:
        isPossible = 'Impossible'
        break
print("#{} {}".format(1, isPossible))