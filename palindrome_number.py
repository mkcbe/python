x=int(input())
num=x
rev=0
while(x>0):
    dig=x%10
    rev=rev*10+dig
    x=x//10
if(num==rev):
    print("yes")
else:
    print("no")
