n = int(input("enter num"))
a,b=0,1
step=0
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b
    step=step+1
print("here is step count",step)
    