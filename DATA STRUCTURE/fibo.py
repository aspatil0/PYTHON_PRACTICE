n = int(input("enter a number"))
#0 1 1 2 3 5
a,b=0,1
step=0
for i in range(n):
    print(f"fibonnaci: {a}, Step ={step}")
    a,b =b,a+b
    step=step+1