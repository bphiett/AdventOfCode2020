#!/usr/bin/env python3

''' https://adventofcode.com/2020/day/3 '''

import pdb
import unittest
import numpy as np
import math


def count_trees(dx: int, dy: int, lines: list) -> int:

    trees = 0
    x = dx
    y = dy
    
    len_y = len(lines)

    while (y < len_y):
        if lines[y][x] == '#':
            trees += 1
        x = (x + dx) % len(lines[y])
        y += dy

    return trees

    
def strip_newline(line: str) -> str:

    return line.strip()


class Test(unittest.TestCase):

    def test(self):

        trees = ['..##.......',
            '#...#...#..',
            '.#....#..#.',
            '..#.#...#.#',
            '.#...##..#.',
            '..#.##.....',
            '.#.#.#....#',
            '.#........#',
            '#.##...#...',
            '#...##....#',
            '.#..#...#.#']

        self.assertEquals(count_trees(3, 1, trees), 7)
        
        
if __name__ == '__main__':

    with open('toboggan_trajectory.txt') as fp: 
        lines = fp.readlines()

    lines = list(map(strip_newline, lines))

    t1 = count_trees(1, 1, lines)
    t2 = count_trees(3, 1, lines)
    t3 = count_trees(5, 1, lines)
    t4 = count_trees(7, 1, lines)
    t5 = count_trees(1, 2, lines)

    print(f'slope right 1, down 1 -> {t1} trees')
    print(f'slope right 3, down 1 -> {t2} trees')
    print(f'slope right 5, down 1 -> {t3} trees')
    print(f'slope right 7, down 1 -> {t4} trees')
    print(f'slope right 1, down 2 -> {t5} trees')

    n = math.prod((t1, t2, t3, t4, t5))
    print(f'product of all trees is {n}')
    
    unittest.main()
        



   


    
