# Define digit mapping
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
    """Converts an integer to a Roman numeral and returns the numeral."""
    if not isinstance(n, int):
        raise NotIntegerError("decimals can not be converted.")
    if not (0 < n < 5000):
        raise OutOfRangeError("number out of range (must be 1... 5000")

    result = ""
    for numeral, integer in roman_numeral_map:
        while n >= integer:
            result += numeral
            n -= integer
#    print result
    return result


def from_roman(s):
    """Convert a roman numeral to an integer and return the integer."""
    if not isinstance(s, str):
        raise NotStringError("You need to input a string.")
    s = s.upper()
    result = 0
    s = remove_subtractives_roman(s)

    while s is not "":
        if "M" in s:
            result += 1000
            s = s.replace("M", "", 1)
        elif "D" in s:
            result += 500
            s = s.replace("D", "", 1)
        elif "C" in s:
            result += 100
            s = s.replace("C", "", 1)
        elif "L" in s:
            result += 50
            s = s.replace("L", "", 1)
        elif "X" in s:
            result += 10
            s = s.replace("X", "", 1)
        elif "V" in s:
            result += 5
            s = s.replace("V", "", 1)
        elif "I" in s:
            result += 1
            s = s.replace("I", "", 1)

#    print result
    return result


def add_roman(a, b):
    """Function for adding a roman numeral
    to another roman numeral without converting to decimal.
    Returns the result of the addition.
    """
    a = a.upper()
    b = b.upper()
    a = remove_subtractives_roman(a)
    b = remove_subtractives_roman(b)
    result = a + b
    result = shorten_roman(result)
    return result


def subtract_roman(a, b):
    """Function for subtracting a roman numeral from another
    roman numeral without converting to decimal.
    Returns the result of the subtraction.
    """
    a = a.upper()
    b = b.upper()
    a = remove_subtractives_roman(a)
    b = remove_subtractives_roman(b)
    while b is not "":
        for c in b:
            if c in a:
                a = a.replace(c, "", 1)
                b = b.replace(c, "", 1)
        if b is not "":
            if "M" in a:
                a = a.replace("M", "DD", 1)
            if "D" in a:
                a = a.replace("D", "CCCCC", 1)
            if "C" in a:
                a = a.replace("C", "LL", 1)
            if "L" in a:
                a = a.replace("L", "XXXXX", 1)
            if "X" in a:
                a = a.replace("X", "VV", 1)
            if "V" in a:
                a = a.replace("V", "IIIII", 1)
    a = shorten_roman(a)
#    print a
    return a


def multiply_roman(a, b):
    """ Function for multiplying a roman numeral with another
    roman numeral without converting to decimal.
    Returns the result of the multiplication.
    """
    a = remove_subtractives_roman(a)
    b = remove_subtractives_roman(b)
    c = []
    d = []
    a = list(a)
    b = list(b)
#    print a
#    print b
    for element in a:
        counter = 0
        while len(b) > counter:
            c.append(element + b[counter])
#            print c
            counter = counter + 1
    for element in c:
        if "II" in element:
            d.append("I")
        if "VI" in element:
            d.append("V")
        if "XI" in element:
            d.append("X")
        if "LI" in element:
            d.append("L")
        if "CI" in element:
            d.append("C")
        if "DI" in element:
            d.append("D")
        if "MI" in element:
            d.append("M")
        if "IV" in element:
            d.append("V")
        if "VV" in element:
            d.append("XXV")
        if "XV" in element:
            d.append("L")
        if "LV" in element:
            d.append("CCL")
        if "CV" in element:
            d.append("D")
        if "DV" in element:
            d.append("MMD")
        if "MV" in element:
            d.append("MMMMM")
        if "IX" in element:
            d.append("X")
        if "VX" in element:
            d.append("L")
        if "XX" in element:
            d.append("C")
        if "LX" in element:
            d.append("X")
        if "CX" in element:
            d.append("M")
        if "DX" in element:
            d.append("MMMMM")
        if "MX" in element:
            d.append("ERROR!")
        if "IL" in element:
            d.append("L")
        if "VL" in element:
            d.append("CCL")
        if "XL" in element:
            d.append("D")
        if "CL" in element:
            d.append("MMMMM")
        if "DL" in element:
            d.append("ERROR!")
        if "ML" in element:
            d.append("ERROR!")
        if "IC" in element:
            d.append("C")
        if "VC" in element:
            d.append("D")
        if "XC" in element:
            d.append("M")
        if "LC" in element:
            d.append("MMMMM")
        if "CC" in element:
            d.append("ERROR!")
        if "DC" in element:
            d.append("ERROR!")
        if "MC" in element:
            d.append("ERROR!")
        if "ID" in element:
            d.append("D")
        if "VD" in element:
            d.append("MMD")
        if "XD" in element:
            d.append("MMMMM")
        if "LD" in element:
            d.append("ERROR!")
        if "CD" in element:
            d.append("ERROR!")
        if "DD" in element:
            d.append("ERROR!")
        if "MD" in element:
            d.append("ERROR!")
        if "IM" in element:
            d.append("M")
        if "VM" in element:
            d.append("MMMMM")
        if "XM" in element:
            d.append("ERROR!")
        if "LM" in element:
            d.append("ERROR!")
        if "CM" in element:
            d.append("ERROR!")
        if "DM" in element:
            d.append("ERROR!")
        if "MM" in element:
            d.append("ERROR!")
    if "ERROR!" in d:
        return "The result is a number which is too large to handle!"
    "".join(d)
    d = sort_roman(d)
    d = shorten_roman(d)
    return d


def divide_roman(a, b):
    a = a.upper()
    b = b.upper()
    a = remove_subtractives_roman(a)
    b = remove_subtractives_roman(b)
    quotient = ""
    remainder = ""
    while is_greater_equal_roman(a, b):
        a = subtract_roman(a, b)
        quotient += "I"
    remainder = a
    quotient = shorten_roman(quotient)
    if remainder is not "":
        return "Quotient: %r, Remainder: %r." % (quotient,
                                                 remainder)
    else:
        return "Quotient: %r, no Remainder." % quotient


def remove_subtractives_roman(s):
    """Removes subtractives from the roman numeral and returns the numeral.
    """
    while "CM" in s:
        s = s.replace("CM", "DCCCC ", 1)
    while "CD" in s:
        s = s.replace("CD", "CCCC ", 1)
    while "XC" in s:
        s = s.replace("XC", "LXXXX ", 1)
    while "XL" in s:
        s = s.replace("XL", "XXXX ", 1)
    while "IX" in s:
        s = s.replace("IX", "VIIII ", 1)
    while "IV" in s:
        s = s.replace("IV", "IIII ", 1)
#    print s
    while " " in s:
        s = s.replace(" ", "", 1)
#    print s
    return s


def sort_roman(p):
    """Sorts the roman numerals from larges to smallest.
    Cannot sort subtractives.  Returns the sorted roman numeral.
    """
    my_alphabet = "MDCLXVI"
    p = "".join(sorted(
        p, key=lambda elem: [my_alphabet.index(c) for c in elem[0]]))
    return p


def shorten_roman(p):
    """Shortens the roman number by replacing smaller numbers
    with larger ones.  Returns the shortened roman numeral.
    """
    p = sort_roman(p)
    while 5 * "I" in p:
        p = p.replace("IIIII", "V", 1)
    while 2 * "V" in p:
        p = p.replace("VV", "X", 1)
    while 5 * "X" in p:
        p = p.replace("XXXXX", "L", 1)
    while 2 * "L" in p:
        p = p.replace("LL", "C", 1)
    while 5 * "C" in p:
        p = p.replace("CCCCC", "D", 1)
    while 2 * "D" in p:
        p = p.replace("DD", "M", 1)
#    print p
    return p


def is_greater_equal_roman(a, b):
    """A function to test whether roman numeral a is greater than b.
    Returns true is a is greater than b and false if it is not.
    """
    a = convert_to_I(a)
    b = convert_to_I(b)
    return len(a) >= len(b)


def convert_to_I(a):
    """Converts the roman numeral to Is.
    Used for comparison purposes.
    """
    while "M" in a:
        a = a.replace("M", "DD", 1)
    while "D" in a:
        a = a.replace("D", "CCCCC", 1)
    while "C" in a:
        a = a.replace("C", "LL", 1)
    while "L" in a:
        a = a.replace("L", "XXXXX", 1)
    while "X" in a:
        a = a.replace("X", "VV", 1)
    while "V" in a:
        a = a.replace("V", "IIIII", 1)
    return a


def tests():
    # Testing whether all functions work:
    # t1 = to_roman(1115)
    # print t1
    assert to_roman(1115) == "MCXV"
    # t2 = to_roman(200)
    # print t2
    assert to_roman(200) == "CC"
    # t3 = subtract_roman(t1, t2)
    # print t3
    assert subtract_roman("MCXV", "CC") == "DCCCCXV"
    # t4 = from_roman(t3)
    # print t4
    assert from_roman("DCCCCXV") == 915
    # t5 = from_roman("x")
    # print t5
    assert from_roman("x") == 10
    # t6 = subtract_roman("xx", "v")
    # print t6
    assert subtract_roman("xx", "v") == "XV"
    # t7 = add_roman("cccc", "d")
    # print t7
    assert add_roman("cccc", "d") == "DCCCC"
    # t8 = divide_roman("cm", "lV")
    # print t8
    assert divide_roman("cm", "lv") == "Quotient: 'XVI', Remainder: 'XX'."
    assert divide_roman("cm", "ix") == "Quotient: 'C', no Remainder."
    # t9 = is_greater_equal_roman("MM", "M")
    # print t9
    assert is_greater_equal_roman("MM", "M") is True
    assert multiply_roman("XX", "CX") == "MMCC"
    assert multiply_roman("I", "I") == "I"
    assert multiply_roman("M", "V") == "MMMMM"
    assert multiply_roman("C", "L") == "MMMMM"
    assert multiply_roman("III", "XXX") == "LXXXX"
    assert multiply_roman("XXX", "III") == "LXXXX"
    return "All tests passed."
print tests()
