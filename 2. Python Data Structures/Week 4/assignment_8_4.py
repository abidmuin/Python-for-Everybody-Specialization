#fname = input("Enter file name: ")
fh = open('2. Python Data Structures\Week 4\/romeo.txt')
lst = list()

for line in fh:
    line = line.rstrip().split()
    for word in line:
        if word not in lst:
            lst.append(word)
        else:
            continue

fh.close()
list.sort(lst)
print(lst)
