rowery = {
    "Bike-001": {
        "Id": 1,
        "Model": "Super Rower",
        "Typ": "Górski",
        "Cena_za_godzine": 250,
        "Dostępny": True
    },
    
    "Bike-002": {
        "Id": 2,
        "Model": "Mega Super Rower",
        "Typ": "Miejski",
        "Cena_za_godzine": 300,
        "Dostępny": False
    },
    
    "Bike-003": {
        "Id": 3,
        "Model": "Ultra Mega Super Rower",
        "Typ": "Terenowy",
        "Cena_za_godzine": 500,
        "Dostępny": True
    }
    
}

wypozyczone = []

def getChoseBikeGui():
    MenuPress = int(input("Wprowadz id roweru od: 1 do 3: "))
    
    if MenuPress > 3:
        getChoseBikeGui()
        
    if MenuPress == 1:
        if 1 in wypozyczone:
            print("Podany rower jest obecnie wypożyczony")
        else:
            print("Wybrano rower Bike-00", MenuPress)
            wypozyczone.append(MenuPress)
            
    if MenuPress == 2:
        if 2 in wypozyczone:
            print("Podany rower jest obecnie wypożyczony")
        else:
            print("Wybrano rower Bike-00", MenuPress)
            wypozyczone.append(MenuPress)
            
    if MenuPress == 3:
        if 3 in wypozyczone:
            print("Podany rower jest obecnie wypożyczony")
        else:
            print("Wybrano rower Bike-00", MenuPress)
            wypozyczone.append(MenuPress)
            
def getAllBikes():
    for nazwa, reszta in rowery.items():
        print(f"{nazwa}, \n")
        for key, value in reszta.items():
            print(f"{key}, {value}")
            
def getBikeReturn():
    x = int(input("Wprowadz id roweru od 1 do 3: "))
    if x > 3:
        getBikeReturn()
    
    for nazwa, reszta in rowery.items(): 
        booleanek = rowery["Bike-00", x]["Dostępny"]
        if booleanek == False:
            print("Oddano rower z id 00", x)

def getBikeReturn():
    x = int(input("Wprowadz id roweru od 1 do 3: "))
    if x > 3:
        getBikeReturn()
    
    for nazwa, reszta in rowery.items(): 
        booleanek = rowery["Bike-00", x]["Dostępny"]
        if booleanek == False:
            print("Oddano rower z id 00", x)
    
def getAllAvalibleBikes():
    for nazwa, reszta in rowery.items():
        booleanek = rowery[nazwa]["Dostępny"]
        if booleanek == True:
            print(f"{nazwa}, \n")
            for key, value in reszta.items():
                print(f"{key}, {value}")
                
def getBikeCost():
    h = int(input("Wprowadz ile godzin: "))
    x = int(input("Wprowadz id roweru od 1 do 3: "))
    
    if x > 3:
        getBikeCost()
    
    if h == 0:
        getBikeCost()
    
    for nazwa, reszta in rowery.items():
        cena = rowery[f"Bike-00{x}"]["Cena_za_godzine"]
        prc = cena * h
    print(f"Cena za {h}godzin z rowerem z id: {x} wynosi {prc}")
    
def getBikesListPrice():
    for nazwa, reszta in rowery.items():
        if reszta == "Cena_za_godzine":
            print("Najtańszy rower: $", min(reszta), "Najdroższy rower: $", max(reszta))
    
        
# def getMenuGui():
#     print("""*-* [ 🚲 ] *-*
          
#           1) Wybierz rower: 
          
#           2) Wyświetlanie wszystkich rowerów
          
#           3) Wyświetlanie dostępnych rowerów
          
#           4) Oddanie roweru po podanym ID
          
#           5) Obliczenie kosztu wypożyczenia roweru
          
#           6) Wyświetlanie najtanszego i najdroższego roweru
          
#           """)
    
#     MenuPress = int(input("Wprowadz opcje: "))
    
#     if MenuPress == 1:
#         getChoseBikeGui()
        
#     elif MenuPress == 2:
#         getAllBikes()
        
#     elif MenuPress == 3:
#         getAllAvalibleBikes()
        
#     elif MenuPress == 4:
#         getBikeReturn()
        
#     elif MenuPress == 5:
#         getBikeCost()
        
#     elif MenuPress == 6:
#         getBikesListPrice()
        
#     elif MenuPress > 6:
#         getMenuGui()        
    
getBikesListPrice()