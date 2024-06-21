'''
Problem Statement:

So, in this tutorial, i.e., Python exercise 1 tutorial, we have to create a dictionary similar to the real-world dictionary. There is no limit to the definition you provide to any word, as this exercise is just for your practice.

The details and functionalities that are essential and must be present are:

    The user will give the word as input. Suppose that the word is present in your dictionary along with its definition or meaning.
    The program will print the meaning or definition of that word.


dict1 = {
    'adequate' : 'sufficient for a specific need or requirement',
    'consider' : 'deem to be',
    'convey' : 'make known; pass on, of information',
    'demonstrate' : 'give an exhibition of to an interested audience',
    'establish' : 'set up or found',
    'illustrate' : 'clarify by giving an example of',
    'interpret' : 'make sense of; assign a meaning to',
    'justify' : 'show to be right by providing justification or proof',
    'outline' : 'describe roughly or briefly or give the main points or summary of',
    'summarize' : 'be a summary of'
}

print("=================================================================================")
print("============\t Welcome to the Dictionary world \t============")
print("=================================================================================")

print()
print("Words are : ")
for i in dict1.keys():
    print(i, end=(", "))
    
print()
    
print("Which word's meaning you wanna search frm the dictionary ")
word = input()
print("The meaning of the word is : ", dict1[word])

'''

# 1. Dictionary questions 
# 1. Write a Python script to merge two Python dictionaries.
'''
dict1 = {
    'a': 1 , 'b': 2, 'c': 4 }
dict2 = {
    'd': 5, 'e': 6, 'f': 7 }

dict1.update(dict2)
print(dict1)
'''
# update use to merge two dictionaries 

# 2. Write a Python program to remove a key from a dictionary.
'''
dict1 = {'a': 1, 'b': 2, 'c': 4, 'd': 5, 'e': 6, 'f': 7}
del dict1['e']
print(dict1)
'''

# 3.lower()
# Write a Python program to map two lists into a dictionary.
'''
l1 = ['a', 'b', 'c', 'd', 'e']
l2 = [1, 2, 3, 4, 5]

d = dict(zip(l1, l2))
print(d)
'''

# 4. Write a Python program to sort a dictionary by key.

'''
dict1 = {
    'a': 1, 'd': 5, 'b': 2, 'c': 4, 'e': 6, 'f': 7
}


for i in sorted(dict1.keys()):

    print(i, dict1[i])
'''

# 5. Write a Python program to get the maximum and minimum value in a dictionary.

'''
dict1 = {
    'a': 1, 'd': 5, 'b': 2, 'c': 4, 'e': 6, 'f': 7
}

print(max(dict1.values()))

print(min(dict1.values()))
'''
