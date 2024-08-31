#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])
    elif length == 1:
        print([0])
    else:
        #starts the list with 0 , 1 as first number in sequence
        fib_list = [0, 1]
        #starts the loop when list index is less than length parameter
        while len(fib_list) < length:
        #adds the last 2 index in and append it to the list
            fib_list.append(fib_list[-1] + fib_list[-2])
        print(fib_list)
