import random

def fizzbuzz(num):
    for i in range(1, num+1):
        if (i % 15) == 0:
            print("FizzBuzz!!!")
        elif (i % 10) == 0:
            print("Buzz")
        elif (i % 5) == 0:
            print("Fizz")
        else:
            print(i)

spare_number = random.randint(1,100)

while True:
    try:
        number = int(input("Give me a positive number: "))
        fizzbuzz(number)
        break
    except ValueError:
        print(f"This is not a valid number, please try again.")

