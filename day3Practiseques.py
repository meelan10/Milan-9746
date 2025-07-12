# 1. Take a number from the user and print whether it's even or odd.

num = int(input("Enter the number :"))
if (num%2==0):
  print("The number is even")
else:
  print("The number is odd")


# 2. Write a program to count the number of vowels in a given string.

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
text="sangit Pokheral"
print(count_vowels(text))


# 3. Ask the user to input a sentence and print the number of words in it.

sentence=(input("Enter the sentence :"))
word=sentence.split()
word_count=len(word)
print("Number of words", word_count)


# 4. Take a number from the user and print its multiplication table from 1 to 10 using a function.

def print_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

num = int(input("Enter a number: "))
print_table(num)


# 5.Write a program to accept 5 numbers from the user, store them in a list, and print the maximum and minimum values.

numbers = []
for i in range(5):
    num = int(input("Enter number : "))
    numbers.append(num)
print("Maximum value:", max(numbers))
print("Minimum value:", min(numbers))


# 6.Accept a string and check whether it is a palindrome or not (same forward and backward).

text = input("Enter a string: ")
cleaned = text.replace(" ", "").lower()
if cleaned == cleaned[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


# 7.Create a loop that keeps asking the user to guess a secret number between 1 to 10 until they guess it correctly. (Use while loop and break)

secret_number = 7
while True:
    guess = int(input("Guess the secret number (1 to 10): "))
    if guess == secret_number:
        print("🎉 Correct! You guessed it!")
        break
    else:
        print("❌ Wrong guess. Try again.")


# 8. Accept 5 numbers from the user and store only the even numbers in a new list. Print the final list.

even_numbers = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    if num % 2 == 0:
        even_numbers.append(num)
print("Even numbers:", even_numbers)

# 9. Write a program that prints the Fibonacci sequence up to n terms. (Ask user for n)

n = int(input("Enter the number of terms: "))
a, b = 0, 1
print("Fibonacci sequence:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

# 10. Accept a list of numbers and remove all duplicate values

user_input = input("Enter numbers separated by commas: ")
numbers = list(map(int, user_input.split(",")))
unique_numbers = list(dict.fromkeys(numbers))
print("List without duplicates:", unique_numbers)
