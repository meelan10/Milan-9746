# #string data types
# #lists and tuples
# #conditionals

# # slicing
# name="milan"
# print(name[0:3]) #output mil
# print(name[0:2]) #output mi
# remove= name[3:len(name)-2]
# print(remove)



# #length
# print(len(name))




# #find and replace 
# print(name.find("m"))
# replaced = name.replace("m","N")
# print(replaced)


# #escape sequences character
# text = "My name is Anoj \n\'here\'and \nI'm 21 years old"
# print(text)

#Write a program to detect double spaces in a string
#9.Write a program  to detect double space in a string


text = input("Enter a string: ")

if "  " in text:
    print("Double space detected!")
else:
    print("No double space found.")




#Write the double spaces from the Problem 3 with single spaces

text = input("Enter a string: ")


fixed_text = text.replace("  ", " ")

print("Fixed string:", fixed_text)



#write a program to format the following letter  using escape sequences character
# letter="Dear students , This python  course is going well.Thanks!"

letter = "Dear Marry,\n\tThis Python course is nice.\nThanks!"
print(letter)


