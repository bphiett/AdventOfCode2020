#!/usr/bin/env python3

''' https://adventofcode.com/2020/day/6 '''


def part1(lines: list[str]) -> int:
    
    return sum([len(set(g.replace('\n', ''))) for g in ''.join(lines).split('\n\n')])


def part2(lines: listo[str]) -> int:

    group_strings = [g.split('\n') for g in ''.join(lines).split('\n\n')]
    return sum([len(set.intersection(*map(set, g))) for g in group_strings])


if __name__ == '__main__':

    with open("custom_customs.txt") as fp: 
        lines = fp.readlines()
    
    print(f'Part 1 = {part1(lines)}')
    print(f'Part 2 = {part2(lines)}')
