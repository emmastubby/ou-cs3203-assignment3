#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 13:09:25 2023

@author: emmastubby
"""

# method to sum list
def sum_list(my_list):
    my_sum = 0
    for num in my_list:
        my_sum += num
    return my_sum

# aklsjdf
def mult_list(my_list):
    prod = 1
    for num in my_list:
        prod = prod * num
    return prod

def reverse(my_list):
    rev = []
    for i in range(1, (len(my_list) + 1)):
        rev.append(my_list[(-1 * i)])
    return rev

def main():
    print("Type a series of numbers separated by spaces, then hit enter.")
    
    l = [int(x) for x in input().split()]
    
    sum_total = sum_list(l)
    product = mult_list(l)
    
    print("Sum: " + str(sum_total))
    print("Product: " + str(product))

if __name__ == "__main__":
    main()