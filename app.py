from flask import Flask
from flask_restful import Resource, Api
from resource.carro import Carros, Carro

app = Flask(__name__)
api = Api(app)

api.add_resource(Carros, '/carros')
api.add_resource(Carro, '/carros/<string:carro_id>')

if __name__ == '__main__':
    app.run(debug=True)

#http://127.0.0.1:5000