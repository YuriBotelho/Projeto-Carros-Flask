from flask_restful import Resource, reqparse


carros = [
    {
        'carro_id':'01',
        'marca':'fiat',
        'modelo':'uno',
        'ano':'2012',
        'cor':'preto',
        'vendido':'false'
    },
    {
        'carro_id':'02',
        'marca':'ford',
        'modelo':'ecosport',
        'ano':'2003',
        'cor':'cinza',
        'vendido':'true'
    }
]

#método get -> retorna todos os carros da lista
class Carros(Resource):
    def get(self):
        return {'carros': carros}

#método get by id
class Carro(Resource):
    def get(self, carro_id):
        for carro in carros:
            if carro['carro_id'] == carro_id:
                return carro
        return {'message':'carro não encontrado'}, 404

    def post (self, carro_id):
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('carro_id')
        argumentos.add_argument('marca')
        argumentos.add_argument('modelo')
        argumentos.add_argument('ano')
        argumentos.add_argument('cor')
        argumentos.add_argument('vendido')

        dados = argumentos.parse_args()

        novo_carro = {
            'carro_id': carro_id,
            'marca': dados['marca'],
            'modelo': dados['modelo'],
            'ano': dados['ano'],
            'cor': dados['cor'],
            'vendido': dados['vendido']
        }

        carros.append(novo_carro)
        return novo_carro, 200

    def put(self, carro_id):
        pass

    def delete(self, carro_id):
        pass
