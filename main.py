# Check if words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("door", "rood") --> True

# true anagram
def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = "listen"
    anagram = "silent"
    str1_anagram = sorted(word)
    str2_anagram = sorted(anagram)

    if str1_anagram == str2_anagram:
        return True
    else:
        return False
print(find_anagram("listen", "silent"))

# false anagram
def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = "cup"
    anagram = "cap"
    str1_anagram = sorted(word)
    str2_anagram = sorted(anagram)

    if str1_anagram == str2_anagram:
        return True
    else:
        return False
print(find_anagram("cup", "cap"))
