class Company():
    def __init__(self, name, delivery_time, max_height,min_height, max_width, min_width, weight_const):
        self.name = name
        self.delivery_time = delivery_time
        self.max_height = max_height
        self.min_height = min_height
        self.max_width = max_width
        self.min_width = min_width
        self.weight_const = weight_const

    def calculate_shipping(self, height, width, weight):
        shipping_is_valid = self.validate_shipping(height, width, weight)
        if shipping_is_valid:
            shipping_price = (weight*self.weight_const)/10
            mapping = {
                "nome": self.name,
                "valor_frete": shipping_price,
                "prazo_dias": self.delivery_time
            }
            return mapping
        else:
            return {}
        
    def validate_shipping(self, height, width, weight):
        if self.min_height <= height <= self.max_height and self.min_width <= width <= self.max_width and weight > 0:
            return True
        else:
            return False