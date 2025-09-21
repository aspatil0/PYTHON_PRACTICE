

n = int(input("Enter a number: "))

for i in range(1, n):
    print(i)
print("---------------")
for i in range(1, n+1):
    if i % 2 == 0:
        print(i)
print("---------------")
for i in range(1, n+1):
    if i % 2 != 0:
        print(i)


