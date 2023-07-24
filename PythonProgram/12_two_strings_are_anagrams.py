"""
string1 = "listen"
string2 = "silent"

str1 = string1.replace(" ", "").lower()
str2 = string2.replace(" ", "").lower()

if len(str1) != len(str2):
    print("The two strings are not anagrams.")
else:
    count_str1 = {}
    count_str2 = {}

    for char in str1:
        count_str1[char] = count_str1.get(char, 0) + 1

    for char in str2:
        count_str2[char] = count_str2.get(char, 0) + 1

    if count_str1 == count_str2:
        print("The two strings are anagrams.")
    else:
        print("The two strings are not anagrams.")
"""
# 12. Implement a program to check if two strings are anagrams of each other.
string1 = "listen"
string2 = "silent"

str1 = string1.replace(" ", "").lower()
str2 = string2.replace(" ", "").lower()

if len(str1) != len(str2):
    print("The two strings are not anagrams.")
else:
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    if sorted_str1 == sorted_str2:
        print("The two strings are anagrams.")
    else:
        print("The two strings are not anagrams.")