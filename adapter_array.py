#!/usr/bin/env python3

''' https://adventofcode.com/2020/day/10 '''

import numpy as np
import unittest
from collections import Counter
import pdb

def part1(input: list[int]) -> int:

    a = np.array(input)
    s = np.sort(a)
    s = np.insert(s, 0, 0)
    s = np.append(s, s[-1]+3)
    ds = np.diff(s)
    return sum(ds == 1) * sum(ds == 3)


def part2(input: list[int]) -> int:
    xs = sorted(input)
    xs.append(xs[-1] + 3)

    c = Counter()
    c[0] = 1

    for x in xs:
        c[x] = c[x - 1] + c[x - 2] + c[x - 3]

    return c[xs[-1]]


def route(x: list[int]) -> int:

    if len(input) == 1:
        return 1

    idx = 1
    diff = x[idx]-x[0]

    while diff < 4:
        sum += route(x[idx:])
        idx += 1
        if idx > len(x)-2:
            break
        else:
            diff = x[idx]-x[0]
    
    return sum
        
class Test(unittest.TestCase):

    def test(self):

        input1 = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
        input2 = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]
        
        self.assertEqual(part1(input1), 35)
        self.assertEqual(part1(input2), 220)
        self.assertEqual(part2(input1), 8)
        self.assertEqual(part2(input2), 19208)


if __name__ == '__main__':

    with open("adapter_array.txt") as fp: 
        input = fp.readlines()
    input = [int(line.strip()) for line in input]
    
    print(f'Part 1 = {part1(input)}')
    print(f'Part 2 = {part2(input)}')    
 
    unittest.main()


