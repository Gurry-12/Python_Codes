'''
# 1. write a python program to print n natural no. 

n = int(input())
for i in range(1,n+1):
    print(i, end = (", "))

print()
# 2. write a python program to print n natural no. in reverse order

n = int(input())
for i in range(n,0,-1):
    print(i, end = (", "))
    
print()
# 3. Write a  program to print all alphabets from a to z. - using while loop

ch = 'a'
while ch <= 'z':
    print(ch, end = " ")
    ch = chr(ord(ch) + 1)

print()
#4. Write a  program to print all even numbers between 1 to 100. 
for i in range(101):
    if i % 2 == 0:
        print(i, end = " ")

print()        
# 5. Write a  program to print all odd number between 1 to 100.

for i in range(101):
    if i % 2 != 0:
        print(i, end = " ")
        
print()
# 6. Write a  program to find sum of all natural numbers between 1 to n. 
n = int(input())
sum = 0
for i in range(n):
    sum = sum + i
print(sum)

print()
# 7. Write a  program to find sum of all even numbers between 1 to n. 

n = int(input())
for i in range(n):
    if i % 2 == 0:
        sum = sum + i
print(sum)

print()
# 8. Write a program to find sum of all odd numbers between 1 to n. 
n = int(input())
for i in range(n):
    if i % 2 != 0:
        sum = sum + i
print(sum)

print()
# 9. Write a  program to print multiplication table of any number.

n = int(input())

for i in range(1,11):
    print(f"{n} x {i} = {n*i}")

print()
# 10. Write a program to count number of digits in any number. 

n = int(input())

print(len(str(abs(n))))

print()

'''
'''
You have to build a "Number Guessing Game,"
in which a winning number is set to some integer value.
The Program should take input from the user, and if the entered number is less than the winning number, 
a message should display that the number is smaller and vice versa.

Instructions:

1. You are free to use anything we've studied till now.
2. The number of guesses should be limited, i.e (5 or 9).
3. Print the number of guesses left.
4. Print the number of guesses he took to win the game.
5. “Game Over” message should display if the number of guesses becomes equal to 0.
You are advised to participate in solving this problem. This task helps you to become
a good problem solver and helps you accepting the challenge and acquiring new skills.
'''
import random
print("==============================================================================")
print("==================== \t Welcome To Numbers World \t =====================")
print("==============================================================================")

print()

sel_no = random.randint(1,10)
guess_count = 9 
input_num = int(input("Enter a no. between 1 to 10:  "))

while input_num != sel_no:
    if input_num < sel_no:
        print("The number is smaller")
    else:
        print("The number is greater")
    guess_count -= 1
    print(f"Guesses left: {guess_count}")
    input_num = int(input("Enter a no. between 1 to 10:  "))
    if guess_count == 0:
        print("Game Over")
        break
print("Congratulations! You have guessed the correct number")
