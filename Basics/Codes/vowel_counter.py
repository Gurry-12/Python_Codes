def num_vowels(text):
    """Return the number of vowels in string."""
    vowels = "aeiou"
    num = 0
    for v in vowels:
        num += text.lower().count(v)        
    return num

def num_consonants(text):
    num_0 = 0
    vowels = "aeiou"
    for letter in text:
        if letter not in vowels:
            num_0 += 1
    return num_0

def list_vowels(text):
    vowels = "aeiou"
    list_v = []
    for v in vowels:
        if v in text:
            list_v.append(v)
    return list_v

def list_consonants(text):
    vowels = "aeiou"
    list_c = []
    for letter in text:
        if letter not in vowels:
            list_c.append(letter)
    return list_c

text = str(input("Enter a sentence: "))

print("Number of vowels", num_vowels(text))
print("Number of consonants", num_consonants(text))

print("List of vowels in the sentence: ", list_vowels(text))
print("List of consonants in the sentence: ", list_consonants(text))