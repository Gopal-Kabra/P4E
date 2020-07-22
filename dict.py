name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)
data = {}
lst = []
for line in fh :
    if line.startswith('From '):
        words = line.split()
        #new1 = words[1]
        for wor in words:
        	#lst.append(wor)
            data[wor] = data.get(wor,0)+1
            #print(w,data[w])  
large = -1 
thew = None
for k,v in data.items():
    if '@' in k:
        
        if v>large :
            large = v
            thew = k
        #print(k,v)
print(thew,large)
    
   
