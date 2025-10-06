# Q1
word = input("Enter a word: ").strip()
vowels = "aeiouAEIOU"
count = 0
for ch in word:
    if ch in vowels:
        count += 1
print("Number of vowels:", count)

# Q2
animals = ['tiger', 'elephant', 'monkey', 'zebra', 'panther']
for a in animals:
    print(a.upper())

# Q3
for n in range(1, 21):
    if n % 2 == 0:
        print(n, "even")
    else:
        print(n, "odd")

# Q4
s = input("Enter a string: ")
t = s.replace(" ", "").lower()
if t == t[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
