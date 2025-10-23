text = str(input("Enter text: "))
vowels = 0
consonants = 0

for i in text:
    if i.isalpha():
        i = i.lower()
        if i in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)