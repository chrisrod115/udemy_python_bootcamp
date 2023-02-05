fizzbuzz = ["Buzz", "Fizz", "FizzBuzz"]

for i in range(1, 100):
    if (i % 3 == 0) and (i % 5 == 0):
        print(fizzbuzz[2])
    elif i % 3 == 0:
        print(fizzbuzz[1])
    elif i % 5 == 0:
        print(fizzbuzz[0])
    else:
        print(i)
