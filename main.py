from flask import Flask, jsonify

app = Flask(__name__)
#lista com dados dos desenvolvedores
desenvolvedores = [
  {'nome':'Filipe',
  'habilidades':['python','Flask']
  },
	{'nome':'Andre',
  'habilidades':['python','Django']}
]
#rota principal que recebe o id
@app.route('/dev/<int:id>/')
def desenvolvedor(id):
#retorna um desenvolvedor da lista de acordo com o id
    desenvolvedor = desenvolvedores[id]
	#retorna os dados do desenvolvedor
    return jsonify(desenvolvedor)

#local onde a api está rodando		
app.run(host='0.0.0.0', port=81)
