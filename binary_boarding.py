#!/usr/bin/env python3

''' https://adventofcode.com/2020/day/5 '''

import unittest

def get_id(code: str) -> int:

    r = get_row(code[:7])
    c = get_col(code[7:])
    return (r * 8) + c

def get_row(code: str) -> int:

    code = code.replace('F', '0')
    code = code.replace('B', '1')
    return int(code, 2)

def get_col(code: str) -> int:

    code = code.replace('L', '0')
    code = code.replace('R', '1')
    return int(code, 2)


class Test(unittest.TestCase):

    def test(self):

        self.assertEqual(get_row('FBFBBFF'), 44)
        self.assertEqual(get_col('RLR'), 5)
        self.assertEqual(get_id('FBFBBFFRLR'), 357)

        self.assertEqual(get_row('BFFFBBFRRR'[:7]), 70)
        self.assertEqual(get_col('BFFFBBFRRR'[7:]), 7)
        self.assertEqual(get_id('BFFFBBFRRR'), 567)

        self.assertEqual(get_row('FFFBBBFRRR'[:7]), 14)
        self.assertEqual(get_col('FFFBBBFRRR'[7:]), 7)
        self.assertEqual(get_id('FFFBBBFRRR'), 119)

        self.assertEqual(get_row('BBFFBBFRLL'[:7]), 102)
        self.assertEqual(get_col('BBFFBBFRLL'[7:]), 4)
        self.assertEqual(get_id('BBFFBBFRLL'), 820)
                         
        
if __name__ == '__main__':

    with open("binary_boarding.txt") as fp: 
        lines = fp.readlines()
    lines = [line.strip() for line in lines]
    
    ids = [get_id(line) for line in lines]
    print(f'Part 1: Highest Seat ID = {max(ids)}')

    seat_id = set(range(min(ids), max(ids)+1)) - set(ids)
    print(f'Part 2: My Seat ID = {seat_id}')
    
    unittest.main()
