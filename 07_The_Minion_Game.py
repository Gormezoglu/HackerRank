
def minion_game(string):
    s =string

    vowels = 'AEIOU'

    kevin = 0 # kevin's score. Vowels are for Kevin
    stuart = 0 # stuart's score. Consonants are for Stuart

    for i in range(len(s)):
        if s[i] in vowels:
            kevin += (len(s)-i) #this counts the number of the combination that start with vowels to the end of the string
            print("Kevin:",kevin)
        else:
            stuart += (len(s)-i) #this counts the number of consonants to the end of the string
            print ("Stuart", stuart)


    if kevin > stuart:
        print ("Kevin", kevin)
    elif kevin < stuart:
        print ("Stuart", stuart)
    else:
        print ("Draw")
