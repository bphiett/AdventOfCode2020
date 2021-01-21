#!/usr/bin/env python3

''' https://adventofcode.com/2020/day/2 '''

def valid_pwds(fn: str) -> int:

    count = 0
    
    with open("input.txt") as fp: 
        lines = fp.readlines() 
        for line in lines:
            [min_n, max_n, char, pwd] = parse_line(line)
            if valid_pwd(min_n, max_n, char, pwd):
                count+=1

    print(f'{count} passwords are valid')


def parse_line(l: str) -> (int, int, str, str):

    [a, b, pwd] = l.split()

    [min_n, max_n] = a.split('-')

    min_n = int(min_n)
    max_n = int(max_n)

    char = b.split(':')[0]

    return [min_n, max_n, char, pwd]


def valid_pwd(min_n: int, max_n: int, char: str, pwd: str) -> bool:

    n = pwd.count(char)
    
    if n >= min_n and n <= max_n:
        return True
    else:
        return False
        
if __name__ == '__main__':

   valid_pwds('input.txt')
    


    
