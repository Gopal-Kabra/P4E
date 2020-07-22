fname = input("Enter file name: ")
fh = open(fname)
lst=[]
for each in fh:
    words=each.split()
    for word in words:
        if word not in lst:
            lst.append(word)
print(sorted(lst))
