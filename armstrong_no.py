num=int(input())
sum=0
l=len(str(num))
temp = num
while temp > 0:
   digit=temp%10
   sum+=digit**l
   temp//=10
if num==sum:
   print("yes")
else:
   print("no")
