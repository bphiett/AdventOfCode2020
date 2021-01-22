#!/usr/bin/env python3

''' https://adventofcode.com/2020/day/1#part2 '''

import pandas as pd
import numpy as np


def fn(nums: np.ndarray, target: int) -> int:

    nums = np.unique(nums)
    
    for i in nums:
        for j in nums:
            for k in nums:
                if i + j + k == target:
                    return i * j * k


if __name__ == '__main__':

    dataframe = pd.read_csv("expenses.csv", header=None)
    data = dataframe[0].to_numpy() # numpy int64 array
    
    print(f'Part 2 answer = {fn(data, 2020)}')    
