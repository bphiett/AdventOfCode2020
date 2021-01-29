#!/usr/bin/env python3

''' https://adventofcode.com/2020/day/9 '''

import unittest


def part1(data: list[int], n: int) -> int:

    for i in range(n, len(data)):

        p = data[i-n:i] # preamble
        combs = [i+j for i in p for j in p if i != j ]
        if data[i] not in combs:
            return data[i]
        
def part2(data: list[int], target: int) -> int:

    for i in range(len(data)):
        for j in range(i, len(data)):
            if sum(data[i:j]) == target:
                return min(data[i:j]) + max(data[i:j])

            
class Test(unittest.TestCase):

    def test(self):


        data = [35,
                20,
                15,
                25,
                47,
                40,
                62,
                55,
                65,
                95,
                102,
                117,
                150,
                182,
                127,
                219,
                299,
                277,
                309,
                576]
        
        self.assertEqual(part1(data, 5), 127)
        self.assertEqual(part2(data, 127), 62)


if __name__ == '__main__':

    with open("encoding_error.txt") as fp: 
        data = fp.readlines()
    data = [int(line.strip()) for line in data]
    
    print(f'Part 1 = {part1(data, 25)}')
    print(f'Part 2 = {part2(data, 1930745883)}')    
 
    unittest.main()

