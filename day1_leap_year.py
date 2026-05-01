# Day 1 - HackerRank
# Problem: Leap Year

def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
