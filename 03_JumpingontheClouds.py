

def jumpingOnClouds(c):

    l_clouds = (c)

    #if not (2<=n<=100) : raise ValueError ('Cloud count must be in the range between 2 and 100') 

    for i in l_clouds:
        if not (i == 1 or i == 0):
            raise ValueError ('Clouds must be either 1 or 0')


    if int(len(l_clouds)) != int(n):
        raise ValueError('Cloud number and array not matched')
        

    if l_clouds[0] !=0 and l_clouds[n-1] !=0:
        raise ValueError ('Clouds assignment is invalid') 

    for i in range(len(l_clouds)-1):
        if l_clouds[i] == 1 and l_clouds[i+1] ==1:
            raise ValueError ('Clouds assignment is invalid') 


    steps=[]

    i=0
    while i<(len(l_clouds)-1):
        try:
            if(l_clouds[i+1]==1):
                i+=2
                steps.append(i)
            elif(l_clouds[i+1]==0 and l_clouds[i+2]==0 and i!=len(l_clouds)-2):
                i+=2
                steps.append(i)
            elif(l_clouds[i+1]==0 and l_clouds[i+2]==0 and i==len(l_clouds)-2):
                i+=1
                steps.append(i)
                steps.append(i+1)
            else:
                i+=1
                steps.append(i)          
        except:
            i+=1
            steps.append(i)

    print(steps)
    s=(len(set(steps)))
   
    return s

n = 6
c=[0,0,0,1,0,0]


#n = 7
#c=[0,0,1,0,0,1,0]

#n = 10
#c=[0,0,1,0,0,0,0,1,0,0]

print(jumpingOnClouds(c))



