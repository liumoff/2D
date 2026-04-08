# DECLARATIONS

thisTuple = (10, 20, 30)

# INSTRUCTIONS

print(tuple[1])

try :
    tuple[1] = 50
except TypeError :
    print(f"Erreur : Impossible de modifier un élément d'un tuple car il est immuable")


tupleInLIst = list(thisTuple)
tupleInLIst[1] = 50
thisTuple = tuple(tupleInLIst)
print(thisTuple)