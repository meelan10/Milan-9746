# Take a secret word as input(without spaces)
#Then encodes the word using a custom cipher:
#Replace all vowels with *
#Reverse the entire string
#Then shift each letter 2 places ahead in the alphabet (wrap around if needed, e.g, --> a, z--> b)

#finally, print the resulting encoded word...

#task for us...
# def encode_secret_word(word):
#     # Step 1: Replace all vowels with '*'
#     vowels = 'aeiouAEIOU'
#     replaced = ''.join(['*' if ch in vowels else ch for ch in word])

#     # Step 2: Reverse the string
#     reversed_str = replaced[::-1]

#     # Step 3: Shift each letter 2 places ahead in the alphabet
#     result = ''
#     for ch in reversed_str:
#         if ch.isalpha():
#             shifted = chr((ord(ch.lower()) - ord('a') + 2) % 26 + ord('a'))
#             result += shifted.upper() if ch.isupper() else shifted
#         else:
#             result += ch

#     # Final encoded word
#     print("Encoded word:", result)


# # Input
# secret_word = input("Enter secret word (no spaces): ")

# # Validation
# if ' ' in secret_word:
#     print("Error: Input should not contain spaces.")
# else:
#     encode_secret_word(secret_word)

 #write a program to store seven fruits in a list enter by the user..
# L1=[]
# for i in range(7):
#     fruits= input("Enter a fruits :")
#     L1.append(fruits)
#     print(L1)



   #write a program to accept marks of six student and diaplay them in a sorted manner...
L2=[]
for i in range(6):
    marks = int(input("Enter the marks of student"))
    L2.append(marks)
    L2.sort()
    print("sorted the marks of student",L2)
    
  
   #Write a program to sum a list of 4 numbers..
# L3=[]
# for i in range(4):
#     num =int(input("Enter the number :"))
#     L3.append(num)
#     print("sum of number", sum(L3))






