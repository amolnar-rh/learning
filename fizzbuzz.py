def fizzbuzz(num):
    num = int(num)
    for i in range(1, num+1):
        if (i % 15) == 0:
            print("FizzBuzz!!!")
        elif (i % 10) == 0:
            print("Buzz")
        elif (i % 5) == 0:
            print("Fizz")
        else:
            print(i)

number = input("Give me a positive number: ")

while str.isdecimal(number) == False:
    number = input("Give me any number: ")

fizzbuzz(number)