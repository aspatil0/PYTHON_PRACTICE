n = input("Enter a word: ")
#aditya
rev = ""  # empty string to store reverse

for i in range(len(n) - 1, -1, -1):  # start from last character to first ( first:last:step)(a:a:-1)
    rev = rev + n[i]

print("Reversed:", rev)

if rev == n:
    print("Yes, it's a palindrome.")
else:
    print("No, not a palindrome.")
