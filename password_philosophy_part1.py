#!/usr/bin/env python3

''' https://adventofcode.com/2020/day/2 '''

import unittest

def valid_pwds(fn: str) -> int:

    with open("input.txt") as fp: 
        lines = fp.readlines()

    return sum(map(valid_pwd, lines))    


def valid_pwd(l: str) -> bool:

    a, b, pwd = l.split()
    min_n, max_n = a.split('-')

    min_n = int(min_n)
    max_n = int(max_n)

    char = b[0]

    n = pwd.count(char)
    
    return True if n >= min_n and n <= max_n else False


class Test(unittest.TestCase):

    def test(self):

        self.assertTrue(valid_pwd('1-3 a: abcde'))
        self.assertFalse(valid_pwd('1-3 b: cdefg'))
        self.assertTrue(valid_pwd('2-9 c: ccccccccc'))


if __name__ == '__main__':

   n = valid_pwds('input.txt')
   print(f'{n} passwords are valid')

   unittest.main()
    
