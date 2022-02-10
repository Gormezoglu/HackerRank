import random

l=[]
def create_list(1,20):
    a random.randint(1,20)
    l.


l =[1,1,1,1,1,1]

def number_generator(l):
    
    l = []
    l.append(random.randint(1,20))

    while (len(l)<9):       

        a = random.randint(1,20)
       # l.append(a)
        
        for t in range(len(l)):
            if int(l[t]) < l.count(l[t]):
                continue
            else:
                l.append(a)

    l.sort()
    print(l)

    return l


number_generator()

   # for i in range(len(l)):