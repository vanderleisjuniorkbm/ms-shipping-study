from models.company import Company

class ShippingService:
    def shipping_calculate(self, product):
        ninja_shipment = Company(name="Entrega Ninja", delivery_time=6, max_height=200, min_height=10, max_width=140, min_width=6, weight_const=0.3)
        kabum_shipment = Company(name="Entrega KaBuM", delivery_time=4, max_height=140, min_height=5, max_width=125, min_width=13, weight_const=0.2)
        shipment_companies = []
        shipment_companies.append(ninja_shipment)
        shipment_companies.append(kabum_shipment)

        height = product['dimensao']['altura']
        width = product['dimensao']['largura']
        weight = product['peso']
        response = []
        #Aqui é calculado o frete e adicionado ao retorno
        for company in shipment_companies:
            shipment_value = company.calculate_shipping(height, width, weight)
            if shipment_value:
                response.append(shipment_value)
        
        return response