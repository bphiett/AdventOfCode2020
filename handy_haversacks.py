#!/usr/bin/env python3

''' https://adventofcode.com/2020/day/7 '''

import unittest


def part1(tree: dict, target: str) -> int:

    return len([key for key in tree.keys() if (key != target) and (contains(tree, key, target))])
    

def part2(tree: dict, target: str) -> int:

    return weighted_sum(tree, target) - 1


def build_tree(lines: list[str]) -> dict:
        
    d = {}
    
    rules = [line.split(' bags contain ') for line in lines]

    for rule in rules:
        d[rule[0]] = parse_contents(rule[1])

    return d


def contains(tree: dict, bag: str, target: str) -> bool:

    if bag == target:
        return True

    ret = False
    for child in tree[bag]:
        ret |= contains(tree, child['bag'], target)

    return ret


def weighted_sum(tree: dict, bag: str) -> int:

    if not len(tree[bag]):
        return 1
    
    n = 1
    for child in tree[bag]:
        n += child['weight'] * weighted_sum(tree, child['bag'])
    return n
    

def parse_contents(contents: str) -> list:

    if contents == 'no other bags.':
        return []
    
    c = contents.replace('bags', 'bag')
    c = c.replace(' bag.', '')
    c = c.replace(' bag, ', ',')
    cs = c.split(',')
    cs = [parse_bag(c) for c in cs]
    return cs


def parse_bag(bag: str) -> list:

    b  = bag.split(' ', 1)
    return {'weight':int(b[0]), 'bag':b[1]}


class Test(unittest.TestCase):

    def test(self):

        lines = ['light red bags contain 1 bright white bag, 2 muted yellow bags.',
                 'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
                 'bright white bags contain 1 shiny gold bag.',
                 'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
                 'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
                 'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
                 'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
                 'faded blue bags contain no other bags.',
                 'dotted black bags contain no other bags.']

        tree = build_tree(lines)
        
        self.assertEqual(part1(tree, 'shiny gold'), 4)
        self.assertEqual(part2(tree, 'shiny gold'), 32)


if __name__ == '__main__':

    with open("handy_haversacks.txt") as fp: 
        lines = fp.readlines()
    lines = [line.strip() for line in lines]

    tree = build_tree(lines)
    
    print(f'Part 1 = {part1(tree, "shiny gold")}')
    print(f'Part 2 = {part2(tree, "shiny gold")}')    
 
    unittest.main()
