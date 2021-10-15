import numpy as np
def throw_egg(eggNum, floorNum):
    if eggNum<1 or floorNum<1:
        print('you are stupid people')
        return 0;
    cache = np.ndarray(shape=(eggNum+1,floorNum+1),dtype=int)
    path = np.ndarray(shape=(eggNum + 1, floorNum + 1), dtype=int)
    pp = 1
    for i in range(1,(eggNum+1)):
        for j in range(1,floorNum+1):
            cache[i][j]=j
            j+=1
        i+= 1
    cache[0][:]=1

    for n in range(2,(eggNum+1)):
        for m in range(1,floorNum+1):
            for k in range(1,m):
                cache[n][m] = min(cache[n][m],1+max(cache[n-1][k-1],cache[n][m-k]))
                if cache[n][m] == 1+max(cache[n-1][k-1],cache[n][m-k]):
                    pp = k
                k+=1
            path[n][m] = pp
            m+=1
        n+=1
    print(cache[1:,1:])
    print(path[1:,1:])
throw_egg(2,36)