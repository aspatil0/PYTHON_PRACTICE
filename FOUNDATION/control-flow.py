#if loop

a = 10
b = 20  
if b>a:
    print("b is greater than a")
else:
    print("a is greater than b")




#elif

a = 15
b = 20
if a>b:
    print("a is greater than b")
elif a==b:
    print("a is equal to b")
else:
    print("b is greater than a")



#for loop

for i in range(1,11):
    print(i)


for i in range(1,11,2):
    print(i)

for i in range(10,0,-1):
    print(i)

for i in range(1,11,1):
    print(i)
    
print("---------------------")



#while loop
i=1
while i<=10:
    print(i)
    i=i+2


#break and continue
for i in range(1,11):
    if i==5:
        break
    print(i)

print("---------------")
