import bottle
import model

SKRIVNOST = 'moja skrivnost'

vislice = model.Vislice(model.DATOTEKA_S_STANJEM, model.DATOTEKA_Z_BESEDAMI)


@bottle.get('/')
# '/' je osnovna stran
# dekorator
def index():
    return bottle.template('index.tpl')


@bottle.post('/nova-igra/')
def nova_igra():
    id_igre = vislice.nova_igra()
    bottle.response.set_cookie('idigre', 'idigre{}'.format(id_igre), path='/', secret=SKRIVNOST)
    bottle.redirect('/igra/')
    # da ne kopiramo kode gremo kar na spodnjo funkcijo


@bottle.get('/igra/')
def pokazi_igro():
    id_igre = int(bottle.request.get_cookie('idigre', secret=SKRIVNOST).split('e')[1]) #dobili bi idigre in številko, želimo le številko
    igra, stanje = vislice.igre[id_igre]
    return bottle.template('igra.tpl', igra=igra, stanje=stanje)


@bottle.post('/igra/')
def ugibaj():
    id_igre = int(bottle.request.get_cookie('idigre', secret=SKRIVNOST).split('e')[1])
    crka = bottle.request.forms.getunicode('crka')
    # 'crka' je enak kot v form v templatu
    vislice.ugibaj(id_igre, crka)
    bottle.redirect('/igra/')
    # id_igre gre v {}


@bottle.get('/img/<picture>')
# v <> je parameter
def serve_picture(picture):
    return bottle.static_file(picture, root='img')
    # picture je katera datoteka, root je lokacija


bottle.run(reloader=True, debug=True)
