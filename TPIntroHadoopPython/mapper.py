#!/usr/bin/env python3
import sys

def mapper(entry):
    """mapper"""
    lines = entry.split('\n')
    for line in lines:
        words = line.split()
        for word in words:
            print(f'{word}\t1')

def main():
    """main"""
    while 1:
        try:
            entry = input()
        except EOFError:
            break

        if(entry == ""):
            break
        mapper(entry)
    

if __name__ == "__main__":
    main()
