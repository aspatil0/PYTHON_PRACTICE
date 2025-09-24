n=5

#for left  angle number pattern
print("-------------------------")
for i in range(1,n+1):
    print(" "*(n-i),str(i)*i)


    #using i and j
print("-------------------------")
for i in range(1,n+1):
    for j in range(i):
        print(i,end="")
    print()