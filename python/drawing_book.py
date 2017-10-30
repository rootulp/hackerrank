#!/bin/python3

def fewest_turns(pages_in_book, target_page):
    return min(turns_from_front(target_page), turns_from_back(pages_in_book, target_page))

def turns_from_front(target_page):
    return target_page // 2

def turns_from_back(pages_in_book, target_page):
    return pages_in_book // 2 - target_page // 2

pages_in_book = int(input().strip())
target_page = int(input().strip())
print(fewest_turns(pages_in_book, target_page))
