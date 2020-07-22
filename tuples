name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst = []
dic = {}
for line in handle:
    if line.startswith('From '):
        words = line.split()
        lst.append(words[5])
        
    
lst = sorted(lst)

for w in lst :
    k = w[0:2]
    #print(k)
   
    if k in dic :
        dic[k]=dic[k]+1
    else :
        dic[k] =1
for (key,value) in dic.items() :
    print(key,value)
    

