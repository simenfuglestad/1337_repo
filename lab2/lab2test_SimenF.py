
#-*- coding: utf-8 -*-

#Dette er et utgangspunkt for lab 2 jeg eksperimenterte med.
#Ideen er at istede for å bruke en dictionary kan man bruke
# 2 separate lister som peker på hverandre for å finne verdi.
#Så langt kan programmet kun peke på hvert enkelt romertall
#og si hvilket tall det er basert på en liste med decimaler.

#NB! DETTE PROGRAMMET ER UFULSTENDIG. KODE SKREVET MED #
#FORAN ER IKKE I BRUK OG ER BEHOLDT KUN SOM NOTATER.


#Erklærer to lister.
roman = ["I", "V", "X", "L", "C", "D", "M"]
number = [1, 5, 10, 50, 100, 500, 1000]

#Metode som starter oversetting.     
def roman_to_decimal():
    
    #Bruker skriver inn et romertall
    user_input = raw_input("Choose a roman number >")
    
    #Deler opp brukers input i list og lagrer det i ny variabel.
    user_input_list = list(user_input)
    
    #Erklærer ny tom liste.
    li = []
    
    #Starter en loop som sjekker hvert element i user_input mot
    #romertallene. For hvert treff legges det til i den tomme
    #listen. Hvert ugylide symbol blir ignorert.
    for c in user_input_list: 
        if c in roman:
            li.append(c)
            print "Adding %s to the list" % c
        else:
            print "%s is not a roman number and will be skipped" % c
            
    
    #Her identifiserer vi tallene ved å iterere over li og sjekke
    # indexene mot roman og number.    
    for c in li:
        r_index = roman.index(c)
        li_index = li.index(c)
        
        print "The roman numeral %s is %s in decimal" % (li[li_index], number[r_index])
        
        #length = len(li)
        
        #left_index = li[li_index - 1]
        
        #print left_index
        
    #Denne biten er et utkast. Tanken er å identifisere pluss eller
    #minus basert på tallet til venstre for seg selv i rekken.
    for c in li[1:]:
        li_index = li.index(c)
        left_index = li[li_index - 1]
        print "test"
        print left_index    
        
#Kaller metode for å starte oversetting.    
roman_to_decimal()
