n = int(input("enter a numnber to get series and count"))
a,b=0,1
step=0
for i in range(n):
    print(f"fibonnanci : {a},StepCount : {step}")
    a,b=b,a+b
    step=step+1