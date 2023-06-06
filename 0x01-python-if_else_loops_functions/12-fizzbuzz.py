#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            res = "FizzBuzz"
        elif num % 3 == 0:
            res = "Fizz"
        elif num % 5 == 0:
            res = "Buzz"
        else:
            res = num
        print("{}".format(res), end=" ")
