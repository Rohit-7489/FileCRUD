# s = "Hello How Are You"
# print(f"String in upper format-> {s[::-1]}")
# print(f"Reverse String -> {s[::-1]}")
# print(f"length of string -> {len(s)}")
# print(f"String in lower format _> {s.lower()}")

# Arrange string character such that lowercase letter should come first

# s = "ShEry"
# lower = ""
# upper = ""
# for i in s:
#     if i.islower():
#         lower = lower + i
#     elif i.isupper():
#         upper = upper + i 
# print(lower + upper)



# count all letter , digit , special characters 

# str1 = "P@#n26at^&i5ve"
# alpha = 0
# digit = 0 
# special = 0
# for i in str1:
#     if i.isalpha():
#         alpha = alpha + 1
#     elif i.isdigit():
#         digit = digit + 1
#     else:
#         special = special + 1 
        
# print(f"alphabet count: {alpha}")
# print(f"Digit count: {digit}")
# print(f"Special count: {special}")


# compare two string without using inbuilt function

# str1 = "hello"
# str2 = "Hello"
# if len(str1) == len(str2):
#     for i in range(len(str1)):
#         if str1[i] != str2[i]:
#             print("Strigs are not same")
#             break
#     else:
#         print("Strings are same")
# else:
#      print("both string are of the same length")


#  Count vowels from given string

# str1 = "Hello"
# vowels = "eiouAEIOU"
# count = 0 

# for i in str1:
#     if i in vowels:
#         count += 1
# print(f"Total count of vowels are: {count}")


# def CountVowels():
#     str1 = "Hello"
#     vowels = "aeiouAEIOU"
#     count = 0 
#     for i in str1:
#         if i in vowels:
#             count += 1 
#     print(f"Total count of vowels are: {count}")
# print(CountVowels())
            

#  Reverse a string

# s = "Hello are you"
# print(f"reverse string -> {s[::-1]}")

# 
# s = "Hello"
# for i in s[::-1]:
#     print(i)

# s = "Hello"
# rev = ""
# for i in s[::-1]:
#     rev = rev + i
# print(rev)


# Check string is Pallindrome or not

# s = "Hello"
# rev = s[::-1]
# if s == rev:
#         print(f"{s} is a palindrome")
# else:
#         print(f"{s} is not a palindrome")
    

# def palindrome(s):
#     rev = s[::-1]
#     if s == rev:
#         print(f"{s} is an Palindrome")
#     else:
#         print(f"{s} is not a palindrome")
# palindrome("madam")

# Count number of vowels and consonants from a string

# n = "Hello"
# vowel = 0
# consonant = 0
# for i in n:
#     if i in "aeiouAEIOU":
#         vowel += 1 
#     else:
#         consonant += 1 
# print(f"Total Vowels are: {vowel}")
# print(f"Total consonants are: {consonant}")
        
    
    
while loop 
function me return not print