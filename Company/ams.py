n = int(input("Enter a number: "))
temp = n
sum = 0
digits = len(str(n)) #3

while n > 0:
    r = n % 10
    sum =sum+ r ** digits  #0+2**3
    n //= 10

if sum == temp:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
