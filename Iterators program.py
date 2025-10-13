#1
import random
secret_number = int(random.random() * 100) + 1  
print("Guess the number between 1 and 100")
while True:
    guess = int(input("Enter your guess: "))
    if guess < secret_number:
        print("Higher")
    elif guess > secret_number:
        print("Lower")
    else:
        print("Congratulations! You guessed it!")
        break
#2
l = [2, 4, 6, 7, 8]

for num in l:
    print("Number:", num, "Square:", num**2) 

#3  

for i in range(1, 101):
    if(i%3 == 0 and i%5 == 0):
        print(i, "FizzBuzz")
    if(i%3 == 0):
        print(i, "Fizz")
    if(i%5 == 0):
        print(i, "Buzz")
    else:
        print(i)







    
    