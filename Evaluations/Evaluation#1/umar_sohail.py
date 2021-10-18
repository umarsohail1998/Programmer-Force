import re
import random

# Q1
def count_evens(arr):
    try:
        return len([x for x in arr if x%2==0])
    except Exception as e:
        return e

# Q2
def analyze(st):
    try:
        letters = 0
        digits = 0
        for x in st:
            if x.isdigit():
                digits += 1
            elif x.isalpha():
                letters += 1
        return (letters, digits)
    except Exception as e:
        return e


# Q3
def validate_password(st):
    try:
        if len(st) < 6:
            return False
        elif not re.findall("[a-z]", st):
            return False
        elif not re.findall("[A-Z]", st):
            return False
        elif not re.findall("[0-9]", st):
            return False
        elif not re.findall("[@$#]", st):
            return False
        return True
    except Exception as e:
        print(e)

# Q4
# https://www.geeksforgeeks.org/python-sort-list-according-to-other-list-order/
def sort_deck(lt):
    try:
        deck  = ['jack', 'queen', 'king', 'ace']
        digits = [x for x in lt if type(x) is int]
        digits.sort()
        letter = [x for x in lt if type(x) is str]
        letter.sort(key = lambda i: deck.index(i.lower())) 
        digits.extend(letter)
        return digits
    except Exception as e:
        return e

# Q5
def int_to_col(n):
    if n<1:
        return 'Invalid column number'
    st = ""
    q = r = 0
    while n > 0:
        q = (n-1) // 26
        r = (n-1) % 26
        st = chr(65 + r) + st
        n = q
    return st


# Q6

non_ielmts = []

def helper(value):
    global non_ielmts
    if type(value) is dict or type(value) is list:
        q6_main(value)
    else:
        non_ielmts.append(value)

def q6_main(d):
    if type(d) is dict:
        for key, value in d.items():
            helper(value)
    elif type(d) is list:
        for x in d:
            helper(x)

def get_depth(d):
    global non_ielmts
    q6_main(d)
    res = non_ielmts.copy()
    non_ielmts.clear()
    return res

# Q7
def Q7():
    pass

# Q8
def Q8():
    TeamA = ['A1','A2','A3','A4','A5','A6'] 
    TeamB = ['B1','B2','B3','B4','B5','B6'] 
    print(random.choice(TeamA))
    print(random.choice(TeamB))
