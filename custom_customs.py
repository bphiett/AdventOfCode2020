#!/usr/bin/env python3

''' https://adventofcode.com/2020/day/6 '''

import unittest


def part1(lines: list) -> int:
    
    return sum([len(set(g.replace('\n', ''))) for g in ''.join(lines).split('\n\n')])


def part2(lines: list) -> int:

    group_strings = [g.split('\n') for g in ''.join(lines).split('\n\n')]
    group_sets = [strings_to_sets(g) for g in group_strings]
    questions = [set.intersection(*g) for g in group_sets]
    return sum([len(q) for q in questions])


def strings_to_sets(strings: list) -> list:

    return [set(string) for string in strings]


if __name__ == '__main__':

    with open("custom_customs.txt") as fp: 
        lines = fp.readlines()
    
    print(f'Part 1 = {part1(lines)}')
    print(f'Part 2 = {part2(lines)}')
