name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)
data = {}


for line in fh :
    if line.startswith('From '):
        words = line.split()
        data[words[1]] = data.get(words[1],0)+1
            
#print(data)            
large = -1 
thew = None
for k,v in data.items():
   
    if '@' in k:
        
        if v>large :
            large = v
            thew = k
        #print(k,v)
print(thew,large)
            
        
    
        
        
    
   
