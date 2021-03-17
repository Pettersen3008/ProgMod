# Sander Pettersen


range1 = int(input("Hvor mange rekker vil du ha? "))


# a) 

# Funkjson med input n
def funk1(range1):
    n1 = range1 - 1
    return(n1 * range1)



# b) Her skal vi returnere tallene i en liste

def funk2():
    liste = []
    for x in range(1, range1 + 1):
        var = funk1(x)
        liste.append(var)
    return liste

# Svar til oppgave ser du i terminalen
print(" ")
print("Funksjon1", funk1(range1))
print(" ")
print("Funskjon2", funk2())
print(" ")