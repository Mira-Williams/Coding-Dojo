import re

def loops_1(n):
    for i in range(n):
        print(i**2)


# loops_1(10)

def is_leap(year):
    leap = False
    
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        leap = True

    return leap

def print_1(n):
    string_1 = ''
    for i in range(n):
        i += 1
        string_1 += str(i)
    print(string_1)

# print_1(5)

def triangle(n):
    for i in range(1,n):
        print(i*(10**i - 1)//9)

# triangle(5)

def post_code():
    regex_integer_in_range = r'[1-9]\d{5}$'
    regex_alternating_repetitive_digit_pair = r'(\d)(?=\d\1)'

    P = input()

    print (bool(re.match(regex_integer_in_range, P)) 
    and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

    