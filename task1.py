#1. Create a program to take a string input from the user and print its length.
string=input("Enter your name:")
print(string)
length=len(string)
print(f"The length is:{length}")

#2.Write a program to convert a list of strings into a list of integers.
string=["12","32","10","90"]
print(string)
integer=[int(i) for i in string]
print(integer)

#3.Write a program to check if a given number is even or odd.
number=int(input("Enter a number:"))
if number % 2 ==0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

#4.Write a program to find the largest of three numbers entered by the user.
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))
if num1>=num2 and num1>=num3:
    print(f"{num1} is the largest")
elif num2>=num1 and num2>=num3:
    print(f"{num2} is the largest")
else:
    print(f"{num3} is the largest")

#5.Write a program to print the multiplication table of a given number.
number=int(input("Enter a number:"))
print(f"The multiplication table of {number} is:")
for m in range(1,11):
    print(f"{number}*{m}={number*m}")

#6.Write a program to print all numbers from 1 to 50 that are divisible by 5.
print(f"The numbers that are divisible by 5 are:")
for a in range(1,51):
    if a%5==0:
        print(a)

#7.Write a program to count how many vowels are present in a given string.
string=input("Enter your name:")
vowels="aeiouAEIOU"
count=0
for v in string:
    if v in vowels:
        count=count+1
print(f"There are {count} vowels present in {string}.")

#8.Write a program to print the factorial of a number using a while loop.
number=int(input("Enter a number:"))
factorial=1
f=1
while f<=number:
    factorial=factorial*f
    f=f+1
print(f"The factorial of {number} is {factorial}")

#9.Write a function to check whether a given number is prime or not.
def prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
number=int(input("Enter a number:"))
if prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")

#10.Write a function to reverse a string without using built-in functions like [::-1] or reversed().
def reverse_string(s):
    reversed_str = ""         
    for c in s:
        reversed_str = c + reversed_str 
    return reversed_str
string = input("Enter a string: ")
print(f"Reversed string: {reverse_string(string)}")