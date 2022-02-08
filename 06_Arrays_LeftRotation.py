def rotLeft(a, d):

    f =[]
    l =[]
    for i in range(d,(len(a))):
        f.append(a[i])

    for m in range(d):
        l.append(a[m])

    return(f+l)