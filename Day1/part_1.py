#!/usr/bin/env python3

''' https://adventofcode.com/2020/day/1#part1 '''

import pandas as pd
import numpy as np


# function 1 using 'in' 
def fn1(nums: np.ndarray, target: int) -> int:
    for num in nums:
        if target - num in nums:
            return num * (target - num)

# function 2 using nested for loops
def fn2(nums: np.ndarray, target: int) -> int:
    for i in nums:
        for j in nums:
            if i + j == target:
                return i * j

# function 3 optimised while
def fn3(sorted_nums: np.ndarray, target: int) -> int:

    # sorted_nums must be sorted in ascending order

    # step through sorted_nums from smallest to largest values
    while len(sorted_nums) > 1:

        num = sorted_nums[0]
        
        if target - num in sorted_nums:
            return num * (target - num)
        else:
            # reduce size of sorted_nums on each iteration by removing values
            # that cannot be part of the solution - this will reduce work
            # required by 'in' in if statement above

            sorted_nums = sorted_nums[1:] # discard value that is too small
            sorted_nums = sorted_nums[sorted_nums <= (target - num)] # discard values that are too large


# pass in one of the 3 possible functions as 2nd arg
def answer(nums: np.ndarray, fn) -> int:

    target = 2020

    # pre computation data optimisation

    # remove any duplicate elements and sort ascending
    nums = np.unique(nums)
    
    # optimisation 1 - discard all large values > target - min(d). These values are
    # too big to sum to target given the smallest number in the dataset
    nums = nums[nums <= (target - min(nums))] 

    # optimisation 2 - discard all values that are < target - max(d). These values are
    # too small to sum to target given the largest number in the dataset
    nums = nums[nums >= (target - max(nums))]

    return fn(nums, target)

if __name__ == '__main__':

    dataframe = pd.read_csv("expenses.csv", header=None)
    data = dataframe[0].to_numpy() # numpy int64 array
    
    a1 = answer(data, fn1)
    a2 = answer(data, fn2)
    a3 = answer(data, fn3)

    print(f'Answer1 = {a1}'
    print(f'Answer2 = {a2}'
    print(f'Answer3 = {a3}'

    
