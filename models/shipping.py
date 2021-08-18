from flask_restx import fields

from server.instance import server
#request body
dimention_model = server.api.model('dimention_model', {
    "altura": fields.Integer(),
    "largura": fields.Integer()
})
shipping_calculate_request = server.api.model('shipping_calculate_request',{
    'dimensao': fields.Nested(dimention_model),
    'peso': fields.Integer()
})
#response body
shipping_result = server.api.model('shipping_result',{
    'nome': fields.String(description='O nome do tipo de entrega'),
    'valor_frete': fields.Float(description='O valor de frete cotado'),
    'prazo_dias': fields.Integer(description='Prazo de entrega em dias')
})