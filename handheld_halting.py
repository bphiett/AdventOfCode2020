#!/usr/bin/env python3

''' https://adventofcode.com/2020/day/8 '''

import unittest


def part1(ops: list[str], args: list[int]) -> (int, int):

    idx = 0
    acc = 0
    hist = []

    while idx not in hist and idx < len(ops):

        op = ops[idx]
        arg = args[idx]
        hist.append(idx)
        
        if op == 'nop':
            idx += 1
            acc += 0
        elif op == 'acc':
            idx += 1
            acc += arg
        else: # 'jmp'
            idx += arg
    return idx, acc

        
def part2(ops: list[str], args: list[int]) -> int:

    for idx, op in enumerate(ops):

        if op == 'nop':
            ops[idx] = 'jmp'
            i, acc = part1(ops, args)
            ops[idx] = 'nop'
            if i == len(ops):
                return acc
        elif op == 'jmp':
            ops[idx] = 'nop'
            i, acc = part1(ops, args)
            ops[idx] = 'jmp'
            if i == len(ops):
                return acc

            
class Test(unittest.TestCase):

    def test(self):

        prog = ['nop +0',
                'acc +1',
                'jmp +4',
                'acc +3',
                'jmp -3',
                'acc -99',
                'acc +1',
                'jmp -4',
                'acc +6']

        ops = [line.split()[0] for line in prog]
        args = [int(line.split()[1]) for line in prog]
    
        self.assertEqual(part1(ops, args), (1, 5))
        self.assertEqual(part2(ops, args), 8)


if __name__ == '__main__':

    with open("handheld_halting.txt") as fp: 
        prog = fp.readlines()
    prog = [line.strip() for line in prog]

    ops = [line.split()[0] for line in prog]
    args = [int(line.split()[1]) for line in prog]
    
    print(f'Part 1 = {part1(ops, args)[1]}')
    print(f'Part 2 = {part2(ops, args)}')    
 
    unittest.main()

