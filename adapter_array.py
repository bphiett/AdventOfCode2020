#!/usr/bin/env python3

''' https://adventofcode.com/2020/day/10 '''

import numpy as np
import unittest


def part1(input: list[int]) -> int:

    a = np.array(input)
    s = np.sort(a)
    s = np.insert(s, 0, 0)
    s = np.append(s, s[-1]+3)
    ds = np.diff(s)
    return sum(ds == 1) * sum(ds == 3)
    

class Test(unittest.TestCase):

    def test(self):


        input1 = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
        input2 = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]
        
        self.assertEqual(part1(input1), 35)
        self.assertEqual(part1(input2), 220)


if __name__ == '__main__':

    with open("adapter_array.txt") as fp: 
        input = fp.readlines()
    input = [int(line.strip()) for line in input]
    
    print(f'Part 1 = {part1(input)}')
    # print(f'Part 2 = {part2(input)}')    
 
    unittest.main()


