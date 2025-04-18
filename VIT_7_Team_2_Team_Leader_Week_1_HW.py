# Question 1: Write a Python code that prints numbers from 1 to 10 on the screen.
for i in range(1,11):
    print(i)

# Question 2: Take a number input from the user and write a Python program that prints even numbers up to this number on the screen. 
# Do this first with 'for' and then with 'while' loops.

number=int(input('Enter a number: '))

even=[i for i in range(0, number) if i%2==0]

print(*even)
cift=0
while cift<number:
    print(cift)
    cift+=2

# Question 3: Write a Python code that receives a start and end value from the user and
# prints all the numbers between these values ​​(including the end value) on the screen.

start=int(input('Enter a starting number: '))
end=int(input('Enter a ending number: '))
for i in range(start, (end+1)):
    print(i)

# Question 4: Get a number from the user and write a Python code that prints whether this number is odd or even.


odd_even= int(input("please enter a number: "))

if odd_even % 2==0:
    print("given number is even")
else:
    print("given number is odd")

# Question 5: Write a Python program that takes a positive integer input from the user and calculates its factorial. 
# Factorial is the product of all positive integers between a number itself and 1. 
# For example: if the user entered 5, the program should give the following output: Enter a number from the user: 5 Factorial: 120

def factorial(number):
    if number>0:
        for i in range(1, (number)):
            number*=i
    return number
sayi=int(input('Faktoriyeli hesaplanacak bir sayı giriniz: '))
print(f'Factorial: {factorial(sayi)}')

# Question 6: Write a Python code that receives a number from the user and checks whether this number is prime.

        
while True:
    
    sayi=int(input("Bir sayı giriniz: "))

    for i in range(2, sayi):
        if sayi % i == 0:
            print(sayi, "Asal değildir")
            break
    else:
        print(sayi, "Asaldır.")
        
# Question 7: How to create a loop that calculates the Fibonacci sequence and returns the result as a list containing numbers up to a certain limit?

limit=int(input('Fibonacci sayı listesini oluşturacağınız üst limiti giriniz: '))
fibonacci=[0,1]
while True:
    if (fibonacci[-1]+fibonacci[-2])>limit:
        break
    else:
        fibonacci.append(fibonacci[-1]+fibonacci[-2])
print(fibonacci)

# Question 8: Write a Python code that takes a word from the user and prints the reverse of this word on the screen.

word=input('Bir kelime giriniz: ')
print(word[::-1])

# Question 9: How to create a combination of loop and conditional statement that takes a word input from the user and 
# checks whether that word is a palindrome (the same when read backwards)?



palo = input("Enter a word: ")

if palo == palo[::-1]:
    print(palo, "is a palindorome")
else:
    print(palo, "is not a palindorme")


# Question 10: Write the code that calculates the person's weight index and returns the result as underweight, overweight or overweight according to the index value. (You can look on the internet for the weight index calculation) To do this, ask the user for their weight and height measurements. weight index If it is below 25, it is weak, Between 25-30 is normal, If you are over 30-40, you are overweight. If you are over 40, you are overweight.
weight= int(input("please enter your weight: "))
height= int(input("Please enter your height: "))

BMI= weight/((height/100)**2)

if BMI < 25:
    print("your BMI is weak")
elif 25 <= BMI <=30:
    print("your BMI is normal")
elif 30 < BMI <=40:
    print("your BMI is overweight")
else:
    print("your BMI is obese")

#Question 11: How to write a Python program that finds the largest of three numbers entered by a user?
nu1= int(input("Enter number 1: "))
nu2= int(input("Enter number 2: "))
nu3= int(input("Enter number 3: "))

print("the largest of three numbers is",max([nu1,nu2,nu3]))


#Question 12: Get Midterm and Final grades from a student for any course. The sum of 40% of the midterm exam grade and 60% of the final grade will give the year-end average. If the average is below 50, "FAILED" will appear on the screen, and if it is 50 or above, "SUCCESSFUL" will be displayed on the screen. This printing process is 4 lessons. and the lessons will be written one after the other.
midterm= int(input("Enter midterm grade: "))
final= int(input("Enter final grade: "))

avg= (midterm*0,4)+(final*0,6)

if avg < 50:
    print("FAILED")
else:
    print("SUCCESFUL")

