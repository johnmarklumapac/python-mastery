# count the number of vowels and consonants
import string

vowels = ['a', 'e', 'i', 'o', 'u']

user_input = input("Enter a String :").lower()

vowel_count = 0
constant_count = 0

for i in user_input:
    if i in vowels:
        vowel_count += 1
    elif i !=  ' ' and i not in string.digits and i not in string.punctuation:
        constant_count += 1

print( "The number of vowels :", vowel_count)
print( " The number of consonants :", constant_count)