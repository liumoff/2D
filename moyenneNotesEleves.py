# DECLARATIONS

eleve1 = [12, 14, 16, 18]
eleve2 = [10, 11, 13, 15]
eleve3 = [17, 19, 20, 18]

notes = [eleve1, 
         eleve2, 
         eleve3]

# INSTRUCTIONS

for i in notes :
    notesEleves = ""
    moyenneEleves = 0
    
    for j in i :
        moyenneEleves += j
        notesEleves += str(j)
        if len(i) > i.index(j) + 1 :

            notesEleves += ", "
        else :
            notesEleves += ""
            
    moyenneEleves /= len(i)    
    print(f"Notes de l'élève {notes.index(i) + 1} : {notesEleves}")
    print(f"Moyenne de l'élève {notes.index(i) + 1} : {moyenneEleves}")
