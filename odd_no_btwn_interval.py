start,end=map(int,input().split())
odd=[]
for num in range(start+1,end): 
    if num%2!=0: 
        odd.append(num)
print(*odd)
