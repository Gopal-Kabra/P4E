fname = input("mbox-short.txt ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
data=[]
for line in fh :
   line = line.rstrip()
   if line.startswith('From ') :
        words = line.split()
        new1 = words[1]
        print(new1)
        count+=1       

print("There were", count, "lines in the file with From as the first word")
