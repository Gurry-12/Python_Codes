# ### Strings: Question Set 1

# 1. Write a Python program that takes a string as input and prints its length.

str = input ( "Enter a string : " )
length = len ( str ) 

print ( "The length of the string is : " , length )


# 2. Create a Python program that takes a string as input and prints it in reverse.

str = input ( "Enter a string : " )
# type 1 to reverse 

reverse = str [ : : -1 ] 

print ( " The reverse of the string is : " , reverse ) 


# 3. Write a Python program that checks if a given string is a palindrome.

str = input ( " Enter a string : " )

reverse = str [ : : -1 ]

if str == reverse : 
    print ( " The string is Palindrome " )
else :
    print ( " The string is not Palindrome " )


# 4. Create a Python program that counts the number of vowels and consonants in a given string.

str = input ( " Enter a string : " )

vowels = 0
consonants = 0

for i in str :
    if i in " aeiouAEIOU " :
        vowels += 1
    else : 
        consonants += 1
        
print ( " The number of vowels in the string is : " , vowels )
print ( " The number of consonants in the string is : " , consonants )

# 5. Write a Python program that takes two strings as input and concatenates them.

str = input ( " Enter the First string : " )
str1 = input ( " Enter the Second string : " )

concatenate = str + str1

print ( " The concatenated string is : " , concatenate )
