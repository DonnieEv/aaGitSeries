maxnum = int(input("Number please: "))
list1 = []
for i in range(maxnum):
    if i % 2 != 0:
        list1.append(i)
print(list1)
