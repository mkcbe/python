start,end=map(int,input().split())
armstrong_no=[]
for num in range(start+1,end): 
    sum=0
    l=len(str(num))
    temp = num
    while temp > 0:
        digit=temp%10
        sum+=digit**l
        temp//=10
        if num==sum:
            armstrong_no.append(num)
print(*armstrong_no)
