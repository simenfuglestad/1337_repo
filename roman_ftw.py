#Define digit mapping
roman_numeral_map = (('M',  1000),
                     ('CM', 900),
                     ('D',  500),
                     ('CD', 400),
                     ('C',  100),
                     ('XC', 90),
                     ('L',  50),
                     ('XL', 40),
                     ('X',  10),
                     ('IX', 9),
                     ('V',  5),
                     ('IV', 4),
                     ('I',  1))

def to_roman(n):
    """convert integer to Roman numeral"""
    if not isinstance(n, int):
        raise NotIntegerError("decimals can not be converted.")
    if not (0 < n < 5000):
        raise OutOfRangeError("number out of range (must be 1... 5000")
    
    result = ""
    for numeral, integer in roman_numeral_map:
        while n >= integer:
            result += numeral
            n -= integer
    print result
    return result


def from_roman(s):
    """Convert roman numeral to integer """
    result = 0
    s = remove_subtractives(s)
    
    while s is not "":
        if "M" in s:
            result += 1000
            s = s.re1place("M", "", 1)
        elif "D" in s:
            result += 500
            s = s.replace ("D", "", 1)
        elif "C" in s:
            result += 100 
            s = s.replace ("C", "", 1)
        elif "L" in s:
            result += 50
            s = s.replace ("L", "", 1)
        elif "X" in s:
            result += 10
            s = s.replace ("X", "", 1)
        elif "V" in s:
            result += 5
            s = s.replace ("V", "", 1)
        elif "I" in s:
            result += 1
            s = s.replace ("I", "", 1)

    print result
    return result

def subtract_roman(a, b):
    a = remove_subtractives(a)
    b = remove_subtractives(b)
    for c in b:
        if c in a:
            a = a.replace (c, "", 1)
            b = b.replace (c, "", 1)
    if b is not "":
        while "M" in b or "D" in b or "C" in b or "L" in b or "X" in b or "V" in b:
            a = a.replace ("M", "DD", 1)
            a = a.replace ("D", "CCCCC", 1)
            a = a.replace ("C", "LL", 1)
            a = a.replace ("L", "XXXXX", 1)
            a = a.replace ("X", "VV", 1)
            a = a.replace ("V", "IIIII", 1)
            for c in b:
                if c in a:
                    a = a.replace (c, "", 1)
                    b = b.replace (c, "", 1)
    a = shorten(a)
    print a
    return a


def remove_subtractives(s):
    """Removes subtractives from the roman numeral."""
    while "CM" in s:
        s = s.replace ("CM", "DCCCC", 1)
    while "CD" in s:
        s = s.replace ("CD", "CCCC", 1)
    while "XC" in s:
        s = s.replace ("XC", "LXXXX", 1)
    while "XL" in s:
        s = s.replace ("XL", "XXXX", 1)
    while "IX" in s:
        s = s.replace ("IX", "VIIII", 1)
    while "IV" in s:
        s = s.replace ("IV", "IIII", 1)
    return s
    
def shorten (p):
    """Shortens the roman number by replacing smaller numbers with larger ones."""
    p = remove_subtractives(p)
    p = ''.join(sorted(p, key=roman_numberal_map))
    while 5 * "I" in p:
        p = p.replace ("IIIII", "V", 1)
    while 2 * "V" in p:
        p = p.replace ("VV", "X", 1)
    while 5 * "X" in p:
        p = p.replace ("XXXXX", "L", 1)
    while 2 * "L" in p:
        p = p.replace ("LL", "C", 1)
    while 5 * "C" in p:
        p = p.replace ("CCCCC", "D", 1)
    while 2 * "D" in p:
        p = p.replace ("DD", "M", 1)
    return p

t1 = to_roman(3985)
t2 = to_roman(199)
t3 = subtract_roman(t1, t2)
t4 =from_roman(t3)
t4
