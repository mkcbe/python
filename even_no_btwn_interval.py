start,end=map(int,input().split())
even=[]
for num in range(start+1,end): 
    if num%2==0: 
        even.append(num)
print(*even)
