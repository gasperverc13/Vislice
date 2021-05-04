import bottle
import model

vislice = model.Vislice()


@bottle.get('/')
# '/' je osnovna stran
# dekorator
def index():
    return bottle.template('index.tpl')


@bottle.post('/igra/')
def nova_igra():
    id_igre = vislice.nova_igra()
    bottle.redirect('/igra/{}/'.format(id_igre))
    # da ne kopiramo kode gremo kar na spodnjo funkcijo


@bottle.get('/igra/<id_igre:int>/')
def pokazi_igro(id_igre):
    igra, stanje = vislice.igre[id_igre]
    return bottle.template('igra.tpl', igra=igra)


@bottle.get('/img/<picture>')
# v <> je parameter
def serve_picture(picture):
    return bottle.static_file(picture, root='img')
    # picture je katera datoteka, root je lokacija


bottle.run(reloader=True, debug=True)