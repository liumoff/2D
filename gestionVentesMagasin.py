# DECLARATIONS

rayonFruitsJ1 = [120, 150, 90]
rayonBoissonsJ1 = [200, 250, 300]
rayonLegumesJ1 = [80, 60, 110]

rayonLegumesJ2 = [70, 80, 90]
rayonFruitsJ2 = [100, 140, 130]
rayonBoissonsJ2 = [220, 230, 240]


Jour1 = [rayonFruitsJ1,
         rayonLegumesJ1,
         rayonBoissonsJ1]

Jour2 = [rayonFruitsJ2,
         rayonLegumesJ2,
         rayonBoissonsJ2]

ventes = [Jour1,
          Jour2]

rayonsNom = [f"Fruits {chr(127823)}",
             f"Legumes {chr(129365)}", 
             f"Boissons {chr(129380)}"]

caTotal = []

# INSTRUCTIONS

print("=== Ventes Journalières ===")

for i, jour in enumerate(ventes) :
    
    
    caTotalJour = 0
    print(f"{chr(128197)} Jour {i + 1} :")
    
    
    for j, rayons in enumerate(jour) :
        caChaineRayons = ""
        
        
        for k, ca in enumerate(rayons) :
            caTotalJour += ca
            
            if len(rayons) != rayons.index(ca) + 1 :
                caChaineRayons += f"{str(ca)}€, "
            else :
                caChaineRayons += f"{str(ca)}€"
            
            
        print(f"{rayonsNom[j]} : {caChaineRayons}")
        
        
    caTotal.append(caTotalJour)
        
    
print("=== Ventes totales par jour ===")

for i, ca in enumerate(caTotal) :
    print(f"{chr(128197)} Jour {i + 1} : {ca}€ {chr(128176)}")