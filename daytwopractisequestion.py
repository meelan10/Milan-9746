'''1. Indexing and Slicing
   Given the string s = "PythonPractice", what are the outputs of:
   - s[1]
   - s[-3:]
   - s[2:7]
   '''
string="PythonPractise"
print(string[1])
print(string[-3:])
print(string[2:7])



#  2. Reverse a String
  # Write a one-liner to reverse the string "developer" using slicing.

text="developer"
reversed_text= "developer"
print(text[::-1])


#3Count Vowels
   #Write a function that counts the number of vowels in a given string

def count_vowels(text):
    count = 0          
    for letter in text:    
        if letter in 'aeiouAEIOU':  
            count = count + 1       
    return count
word="MilanWagle"
print(count_vowels(word))  



# 4.Check for Palindrome
  # Write a function to check if a given string is a palindrome. Ignore spaces and capitalization.

text= input("Enter the String :")
if (text==text[::-1]):
    print("String is palindrome")
  
else:
    print("string is not palindrome")



# 5.Clean and Format String
  #  Given text = "   hello world! welcome to Python.   ", write code to:
  #  - Remove leading/trailing spaces
  #  - Capitalize each word
  #  - Replace the word "Python" with "Programming"

text="  hello word ! Welcome python  "
print(text.replace("python","Programming"))
print(text.capitalize())
print(text.strip()) 


# 6. Find Longest Word
 #  Write a function that takes a sentence and returns the longest word in it.

def longest_word(sentence):
    words = sentence.split()   
    longest = words[0]         
    
    for word in words:
        if len(word) > len(longest):
            longest = word    
    
    return longest


sentence = input("Enter a sentence: ")
print("Longest word is:", longest_word(sentence))



# 7.String Operators
  #  Given s1 = "Py" and s2 = "thon", what are the results of:
  #  - s1 + s2
  #  - s1 * 3
  #  - "y" in s1
  
s1="py"
s2="thon"

print( s1+ s2 )
print( s1 * 3) 
print("y" in s1)



# 8.Remove Duplicate Characters
 #  Write a function that removes all duplicate characters from a string but keeps the first occurrence.

def remove_duplicates(text):
    result = ""
    for char in text:
        if char not in result:
            result += char
    return result
text="sanjit Pokheral"
print(remove_duplicates(text))


# 9.Check for Anagram
 #  Write a function that returns True if two strings are anagrams of each other.
def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

print(is_anagram("listen", "silent"))   # True
print(is_anagram("hello", "world"))     # False


# 10.Word Frequency Counter
   # Write a function that takes a sentence and returns a dictionary of word frequencies.

def word_frequency(sentence):
    words = sentence.split()        # Split sentence into words
    freq = {}                       # Create empty dictionary

    for word in words:
        if word in freq:
            freq[word] += 1         # If word already in dict, add 1
        else:
            freq[word] = 1          # If word not in dict, start at 1

    return freq
sentence="I love Python because I love coding in Python"
print(sentence)



