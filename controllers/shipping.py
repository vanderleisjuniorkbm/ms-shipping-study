from flask import Flask
from flask_restx import Api, Resource
from server.instance import server
from models.company import Company
from services.shipping_service import ShippingService
from models.shipping import *

app = server.app
api = server.api

@api.route("/shipping")
class Shipping(Resource):

    @api.expect(shipping_calculate_request, validade=True)
    @api.marshal_with(shipping_result)
    def post(self, ):
        payload = api.payload
        #Aqui é validado o payload
        if "dimensao" not in payload:
            return {"status": "dimensao is missing"}

        if "altura" not in payload['dimensao']:
            return {"status": "altura is missing"}

        if "largura" not in payload['dimensao']:
            return {"status": "largura is missing"}

        if "peso" not in payload:
            return {"status": "peso is missing"}

        shipping_service = ShippingService()
        response = shipping_service.shipping_calculate(payload)

        return response