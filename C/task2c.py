text = str(input("Enter text: "))
a = 0

for i in text:
    if i.isalpha():
        i = i.lower()
        if i in "a":
            a += 1

print ("Number of times 'A' appeared", a)

