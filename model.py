import random
import json

STEVILO_DOVOLJENIH_NAPAK = 9
PRAVILNA_CRKA, PONOVLJENA_CRKA, NAPACNA_CRKA = '+', 'O', '-'
ZMAGA, PORAZ = 'W', 'L'
ZACETEK = 'Z'

DATOTEKA_S_STANJEM = 'stanje.json'
DATOTEKA_Z_BESEDAMI = 'besede.txt'


class Igra:
    def __init__(self, geslo, crke):
        self.geslo = geslo
        self.crke = crke[:]
        # paziti moramo, saj so crke seznam in je to referenca, morda bolje kopija

    def napacne_crke(self):
        return [crka for crka in self.crke if crka not in self.geslo]
        # izpeljan seznam, tisti znaki iz seznama crke, ki niso v geslu

    def pravilne_crke(self):
        return [crka for crka in self.crke if crka in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        #vse_crke = True
        # for crka in self.geslo:
        #    if crka in self.pravilne_crke():
        #        pass
        #    else:
        #        vse_crke = False
        #        break
        return self.stevilo_napak() <= STEVILO_DOVOLJENIH_NAPAK and all(crka in self.crke for crka in self.geslo)
        # all mora biti true za vse člene v (), ta del naredi enako kot for zanka zgoraj

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


with open(DATOTEKA_Z_BESEDAMI, 'r', encoding='utf-8') as f:
    bazen_besed = [beseda.strip().upper() for beseda in f.readlines()]


def nova_igra():
    geslo = random.choice(bazen_besed)
    return Igra(geslo, [])


# testno_geslo = 'DEŽUJE'
# testne_crke = ['A', 'I', 'D', 'K', 'J', 'U']
# igra = Igra(testno_geslo, testne_crke)
# print(testno_geslo)

class Vislice:
    def __init__(self, datoteka_s_stanjem, datoteka_z_besedami):
        self.igre = {}
        self.datoteka_s_stanjem = datoteka_s_stanjem
        self.datoteka_z_besedami = datoteka_z_besedami
        # v tem slovarju hranimo vse igre, ki smo jih začeli

    def prost_id_igre(self):
        if len(self.igre) == 0:
            return 0
            # ker bi prišlo do napake
        else:
            return max(self.igre.keys()) + 1
            # ID številski, največjemu prištejemo 1 za naslednjega

    def nova_igra(self):
        self.nalozi_igre_iz_datoteke()
        id_igre = self.prost_id_igre()
        # ker je v istem classu, uporabimo self
        igra = nova_igra()
        self.igre[id_igre] = (igra, ZACETEK)
        self.zapisi_igre_v_datoteko()
        return id_igre

    def ugibaj(self, id_igre, crka):
        self.nalozi_igre_iz_datoteke()
        igra, _ = self.igre[id_igre]
        stanje = igra.ugibaj(crka)
        self.igre[id_igre] = (igra, stanje)
        self.zapisi_igre_v_datoteko()

    def nalozi_igre_iz_datoteke(self):
        with open(self.datoteka_s_stanjem, 'r', encoding='utf-8') as f:
            igre = json.load(f)
            self.igre = {int(id_igre): (Igra(geslo, crke), stanje)
                         for id_igre, (geslo, crke, stanje) in igre.items()}

    def zapisi_igre_v_datoteko(self):
        with open(self.datoteka_s_stanjem, 'w', encoding='utf-8') as f:
            igre = {id_igre: (igra.geslo, igra.crke, stanje)
                     for id_igre, (igra, stanje) in self.igre.items()}
            json.dump(igre, f)
