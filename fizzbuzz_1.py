# a=[3,7,9,10,12,15,16,20]
def fizzbuzz(listy):
    for num in listy:
        if num % 3 == 0 and num % 5 == 0:
            print('Fizzbuzz')
        elif num % 3 == 0:
            print('Fizz')
        elif num % 5 == 0:
            print('Buzz')
        else:
            print(num)
# fizzbuzz(a)