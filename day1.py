
#Use REPL and print the table of 5 using it

base=int(input("Enter the Number :"))
for i in range(1, 11):
    result = base *i
    print(f"{base} x {i} = {result}")



#Write the program to calculate simple interest.

P=float(input("Enter the principle :"))
T=float(input("Enter the time :"))
R=float(input("Enter the rate :"))


SI=(P*T*R)/100

print("interest is:", SI )

'''
'''

#Write the program to print the sum of 2 number entered by the user........

num1=int(input("Enter the first Number :"))
num2=int(input("Enter the second Number :"))

sum= num1 + num2
print("the  sum of two number:",sum)

#Write a python program to find reminder when A number is  divided by z

a=25
z=4
rem=a%z
print("the reminder is:", rem)
