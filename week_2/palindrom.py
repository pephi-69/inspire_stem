#This is a program to check if a word is a palindrom
#Date :22/2/2024
#Name:Ephraim

def palindrome(word):
   return word == word[::-1]

word = input("Enter the word : ")
if palindrome(word):
    print('{word} is palindrome')
else:
    print ('{word} is not palindrome')