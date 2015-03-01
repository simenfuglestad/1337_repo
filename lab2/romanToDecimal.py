from sys import exit
import re

roman = ["I", "V", "X", "L", "C", "D", "M"]
number = [1, 5, 10, 50, 100, 500, 1000]

replace_roman = (
                ("IV",  "IIII"),
                ("IX",  "VIII"),
                ("XL",  "XXXX"),
                ("XC", "LXXXX"),
                ("CD",  "CCCC"),
                ("CM", "DCCCC"))

invalid_roman = ["IL", "IC", "IL", "ID", "IM", "VX"] #this needs to be extended

        
def roman_to_decimal():
    
    user_input = raw_input("Choose a roman number >")
    
    li = []
    final_number = 0
    
    for c in invalid_roman:
        if c in user_input:
            print "Invalid roman number, cannot use %s" % c
            exit(1)
    
    for key, value in replace_roman:
        if key in user_input:
            user_input = user_input.replace(key, value)
                

    for c in user_input: 
        if c in roman:
            li.append(c)
            print "Adding %s to the list" % c
        else:
            print "%s is not a roman number and will be skipped" % c
    print user_input


    for c in li:
        r_index = roman.index(c)
        li_index = li.index(c)
                      
        final_number += number[r_index]
        
        print "The roman numeral %s is %s in decimal" % (li[li_index], number[r_index])
        
    print "The final number is %s" % final_number
        
    
roman_to_decimal()
