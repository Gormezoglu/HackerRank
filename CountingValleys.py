def countingValleys(steps, path):
    if 1<=steps<=(10**6):
        path_list = list(path)
        level = 0
        result = 0
        for i in range(len(path_list)):
            if (isinstance(path_list[i],str) and path_list[i]=='U' or path_list[i]=='D'):
                if path_list[i]=='U':
                    level +=1                    
                else:
                    level -=1

                if (level > 0 or (level == 0 and path_list[i]=='D')):
                    continue                
                else:
                    print('level is', level)
                    if level == 0:
                        result +=1
                        print('result is:',result)
                    
            else:
                raise ValueError('Just allowed to be U or D')      
    else:
        raise AttributeError('steps are not in range')
    return result

countingValleys (12,'DDUUDDUDUUUD')
