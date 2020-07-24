fname = input("mbox-short.txt ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
data=[]
for line in fh :
   line = line.rstrip()
   if line.startswith('From ') :
        words = line.split()
        for w in words :
            if '@' in w:
                new1 = w
                print(new1)
                count+=1
            
print("There were", count, "lines in the file with From as the first word")

