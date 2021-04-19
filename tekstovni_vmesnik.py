import model

PONOVNI_ZAGON = 'p'
IZHOD = 'i'
stopnje = [
'''
 _____ 
 |   | 
 |   o 
 |  /|\\ 
 |  / \\ 
_|______  
''',
'''
 _____ 
 |   | 
 |   o 
 |  /|\\ 
 |  /  
_|______  
''',
'''
 _____ 
 |   | 
 |   o 
 |  /|\\ 
 |    
_|______   
''',
'''
 _____ 
 |   | 
 |   o 
 |  /| 
 |    
_|______  
''',
'''
 _____ 
 |   | 
 |   o 
 |   | 
 |   
_|______  
''',
'''
 _____ 
 |   | 
 |   o 
 |   
 |   
_|______  
''',
'''
 _____ 
 |   | 
 |    
 |   
 |   
_|______  
''',
'''
 _____ 
 |    
 |    
 |   
 |   
_|______  
''',
'''
 
 |    
 |    
 |   
 |   
_|______  
''',
'''
________  
''',
'''
''',
'''
'''
]

def izpis_igre(igra):
    tekst = f'''###############################\n
    {igra.pravilni_del_gesla()}\n
    Število poskusov: {model.STEVILO_DOVOLJENIH_NAPAK + 1 - igra.stevilo_napak()}\n
    {stopnje[model.STEVILO_DOVOLJENIH_NAPAK + 1 - igra.stevilo_napak()]}    
    Nepravilne črke: {igra.nepravilni_ugibi()}\n
###############################\n'''
    return tekst
    #problem: na koncu ne gre čez ta del še enkrat

def izpis_zmage(igra):
    tekst = f'''###############################\n
    Bravo! Zmagali ste\n
    Uganili ste geslo: {igra.pravilni_del_gesla()}\n
###############################\n'''
    return tekst

def izpis_poraza(igra):
    tekst = f'''###############################\n
    Porabili ste vse poskuse.\n
    Pravilno geslo: {igra.geslo}\n
###############################\n'''
    return tekst

def zahtevaj_vnos():
    return input('Vnesite črko: ')

def zahtevaj_moznost():
    return input('Vnesite možnost: ')

def ponudi_moznosti():
    tekst = f''' Vpišite črko za izbor naslednjih možnosti: \n
    {PONOVNI_ZAGON} : ponovni zagon igre\n
    {IZHOD} : izhod
    '''
    return tekst
    
def izberi_ponovitev():
    print(ponudi_moznosti())
    moznost = zahtevaj_moznost().strip().lower()
    if moznost == PONOVNI_ZAGON:
        igra = model.nova_igra()
        print(izpis_igre(igra))
        return igra
    else:
        return IZHOD

def pozeni_vmesnik():
    igra = model.nova_igra()
    print(izpis_igre(igra))
    while True:
        crka = zahtevaj_vnos()
        odziv = igra.ugibaj(crka)
        print(izpis_igre(igra))
        if odziv == model.ZMAGA:
            print(izpis_zmage(igra))
            igra = izberi_ponovitev()
            if igra == IZHOD:
                break
        elif odziv == model.PORAZ:
            print(izpis_poraza(igra))
            igra = izberi_ponovitev()
            if igra == IZHOD:
                break
            



pozeni_vmesnik()





#  _____
#  |   |
#  |   o
#  |  /|\
#  |  / \
# _|______ 