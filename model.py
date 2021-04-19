STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA, PONOVLJENA_CRKA, NAPACNA_CRKA = '+', 'O', '-'
ZMAGA, PORAZ = 'W', 'L'

class Igra:
    def __init__(self, geslo, crke):
        self.geslo = geslo
        self.crke = crke[:]
        #paziti moramo, saj so crke seznam in je to referenca, morda bolje kopija

    def napacne_crke(self):
        return [crka for crka in self.crke if crka not in self.geslo]
        #izpeljan seznam, tisti znaki iz seznama crke, ki niso v geslu
    
    def pravilne_crke(self):
        return [crka for crka in self.crke if crka in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        #vse_crke = True
        #for crka in self.geslo:
        #    if crka in self.pravilne_crke():
        #        pass
        #    else:
        #        vse_crke = False
        #        break
        return self.stevilo_napak() <= STEVILO_DOVOLJENIH_NAPAK and all(crka in self.crke for crka in self.geslo)
        #all mora biti true za vse člene v (), ta del naredi enako kot for zanka zgoraj

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        nov = ''
        ugibanje = [crka.upper() for crka in self.crke]
        for znak in self.geslo:
            if znak.upper() in ugibanje:
                nov += znak
            else:
                nov += ' _ '
        return nov

    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())

    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        elif crka in self.geslo:
            self.crke.append(crka)
            if self.zmaga():
                return ZMAGA
            else:
                return PRAVILNA_CRKA
        else:
            self.crke.append(crka)
            if self.poraz():
                return PORAZ
            else:
                return NAPACNA_CRKA
            
with open('besede.txt', 'r', encoding='utf-8') as f:
    bazen_besed = [beseda.strip().upper() for beseda in f.readlines()]

import random

def nova_igra():
    geslo = random.choice(bazen_besed)
    return Igra(geslo, [])




# testno_geslo = 'DEŽUJE'
# testne_crke = ['A', 'I', 'D', 'K', 'J', 'U']
# igra = Igra(testno_geslo, testne_crke)
# print(testno_geslo)
