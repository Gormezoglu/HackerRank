import urllib

s = urllib.request.urlopen('https://hr-testcases-us-east-1.s3.amazonaws.com/9693/input14.txt?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1651010253&Signature=Mqx%2F4S4Jqa1h5hnVK53OTsWw%2FaE%3D&response-content-type=text%2Fplain')

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


#not completed ... check