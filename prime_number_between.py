lower,upper=input().split()
lower,upper=int(lower),int(upper)
prime=[]
for num in range(lower,upper - 1):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           #print(num)
           prime.append(num)
print(*prime)
