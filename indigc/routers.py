from flask import render_template, request, jsonify

from indigc import app
from indigc.indicativos import GCI

ig = GCI()


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/sobre/', methods=['GET'])
def sobre():
    return render_template('sobre.html')


@app.route('/pais/<string:_pais>/', methods=['GET'])
def pais(_pais):
    return jsonify(pais=_pais.upper(), indicativo=ig.indicativo_especifico(_pais.upper()))


@app.route('/indicativos/', methods=['GET'])
def indicativos():
    _json = []
    for p in sorted(ig.paises()):
        _json.append({'pais': p, 'indicativo': ig.indicativo_especifico(p)})
    return jsonify(_json)


@app.route('/paises/', methods=['GET'])
def paises():
    p = [_ for _ in ig.paises()]
    return render_template('paises.html', p=p)
