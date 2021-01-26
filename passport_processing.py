#!/usr/bin/env python3

''' https://adventofcode.com/2020/day/4 '''

import re


def count_valid(lines: list, validator) -> int:

    # count no. of valid passports in input text (as read from file)

    lines = ''.join(lines).split('\n\n')
    passport_lines = map(lambda l : l.replace('\n', ' '), lines)
    passports = map(line_to_dict, lines)
    return sum(map(validator, passports))
    

def line_to_dict(line: str) -> dict:

    # convert passport string to dictionary

    return dict(map(lambda kvp : kvp.split(':'), line.split()))


def int_is_between(lower: int, upper: int, number: str) -> bool:

    return lower <= int(number) <= upper


def hgt_is_valid(hgt: str) -> bool:

    units = hgt[-2:]
    h = hgt[:-2]

    if units == 'cm':
        return int_is_between(150, 193, h)
    elif units == 'in':
        return int_is_between(59, 76, h)
    else:
        return False

    
def pid_is_valid(pid: str) -> bool:
    return bool(re.search(r'\d{9}', pid)) and len(pid) == 9


def ecl_is_valid(ecl: str) -> bool:
    return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def hcl_is_valid(hcl: str) -> bool:
    return bool(re.search(r'^\#[0-9a-f]{6}$', hcl)) and len(hcl) == 7

    
def validate_fields(passport: dict) -> bool:

    return all([int_is_between(1920, 2002, passport['byr']),
                int_is_between(2010, 2020, passport['iyr']),
                int_is_between(2020, 2030, passport['eyr']),
                hgt_is_valid(passport['hgt']),
                hcl_is_valid(passport['hcl'] ),
                ecl_is_valid(passport['ecl']),
                pid_is_valid(passport['pid'])])

    
def is_valid_part1(passport: dict) -> bool:
                
    if len(passport.keys()) == 8:
        return True
    if (len(passport.keys()) == 7 and 'cid' not in passport.keys()):
        return True
    else:
        return False


def is_valid_part2(passport: dict) -> bool:
                
    if len(passport.keys()) == 8:
        return validate_fields(passport)
    if (len(passport.keys()) == 7 and 'cid' not in passport.keys()):
        return validate_fields(passport)
    else:
        return False
    
    
if __name__ == '__main__':

    with open('passport_processing.txt') as fp: 
        lines = fp.readlines()
    
    print(f'Part 1: {count_valid(lines, is_valid_part1)} passports are valid')
    print(f'Part 2: {count_valid(lines, is_valid_part2)} passports are valid')
        

    
