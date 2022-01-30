#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    s= str(s)
    l_s = [*s]
    
    if not 1<=n<=10**12:
        raise ValueError('n must be in range')

    if len(l_s)>100:
        raise ValueError('s must be equal or less than 100 character')

    repetition = int(n/len(l_s))
    remainder = int(n%len(l_s))

    repeated=l_s.count('a') * repetition
    

    l_s_rem=[]
    for i in range(remainder):
        l_s_rem.append(l_s[i])

    return (int(repeated) + int(l_s_rem.count('a')))


s='a'
n=10**12

print(repeatedString(s,n))