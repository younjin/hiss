# CARBONATED NUMBERS

def fizzbuzz(n):
    if isinstance(n, int):
        for i in xrange(1,n):
            if i % 15 == 0:
                print("fizzbuzz")
            elif i % 3 == 0:
                print("fizz")
            elif i % 5 == 0:
                print("buzz")
            else:
                print(i)
    else:
        raise Exception("fizzbuzz only likes to eat ints.")

import sys
fizzbuzz(int(sys.argv[1]))
