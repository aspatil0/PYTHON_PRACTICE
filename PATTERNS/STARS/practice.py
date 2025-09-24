n = 5

for i in range(n):
    print("x",end="")

print("--------------")

for i in range(n):
    for j in range(n):
        print("x",end="")
    print()


print("-----------------")

for i in range(n):
    for j in range(i+1):
        print("x",end="")
    print()

print("--------------------------")

for i in range(n):
    for j in range(i,n):
        print("x",end="")
    print()

print("------------hh------------------")

for i in range(n):
    for j in range(i,n):
        print('-',end='')
    for j in range(i+1):
        print("x",end="")
    print()


print("=====================")

for i in range(n):
    for j in range(i+1):
        print("-",end="")
    for j in range(i,n):
        print("x",end="")
    print()

print("****************hhhh*********")

for i in range(n):
    for j in range(i,n):
            print("-",end="")
    for j in range(i):
            print("*",end="")
    for j in range(i+1):
            print("*",end="")
    print()
