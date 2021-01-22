#!/usr/bin/env python3

''' https://adventofcode.com/2020/day/2 Part 2 '''

import unittest

def valid_pwds(fn: str) -> int:

    with open("input.txt") as fp: 
        lines = fp.readlines()

    return sum(map(valid_pwd, lines))    


def valid_pwd(l: str) -> bool:

    [a, b, pwd] = l.split()

    [pos_1, pos_2] = a.split('-')

    pos_1 = int(pos_1)
    pos_2 = int(pos_2)

    char = b[0]

    pos_1_valid = pwd[pos_1-1] == char
    pos_2_valid = pwd[pos_2-1] == char
    
    return True if pos_1_valid ^ pos_2_valid else False

class Test(unittest.TestCase):

    def test(self):

        self.assertTrue(valid_pwd('1-3 a: abcde')) # is valid: position 1 contains a and position 3 does not.
        self.assertFalse(valid_pwd('1-3 b: cdefg')) # is invalid: neither position 1 nor position 3 contains b.
        self.assertFalse(valid_pwd('2-9 c: ccccccccc')) # is invalid: both position 2 and position 9 contain c.

if __name__ == '__main__':

   n = valid_pwds('input.txt')
   print(f'{n} passwords are valid')

   unittest.main()

   


    
