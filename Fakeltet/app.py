

def fak(n):  
    k = 1
    for i in range(1,n+1): 
        k = k * i 
    return k    
print(fak(4))


nytest = 0
for j in range(0, 101):
    nytest += (1/fak(j))
    print(nytest)