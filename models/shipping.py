from flask_restx import fields

from server.instance import server

shipping_result = server.api.model('shipping_result',{
    'nome': fields.String(description='O nome do tipo de entrega'),
    'valor_frete': fields.Float(description='O valor de frete cotado'),
    'prazo_dias': fields.Integer(description='Prazo de entrega em dias')
})


shipping_calculate_payload = server.api.model('shipping_calculate_payload', {
    'nomeesd': fields.String(description='O nome do tipo de entrega'),
    'valor_frete': fields.Float(description='O valor de frete cotado'),
    'prazo_dias': fields.Integer(description='Prazo de entrega em dias')
})

# shipping_calculate_payload = server.api.model('shipping_calculate_payload', {
#     'dimensao': {
#         "altura": fields.Integer(),
#         "largura": fields.Integer()
#     },
#     'peso': fields.Integer()
# })