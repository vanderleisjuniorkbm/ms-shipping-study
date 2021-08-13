import unittest

from models.company import Company

class TestCompany(unittest.TestCase):
    test_company = Company(name="Entrega Teste", delivery_time=6, max_height=200, min_height=10, max_width=140, min_width=6, weight_const=0.3)
    #testes unitários de valor limite
    def test_validate_shipping_true(self):
        self.assertEqual(self.test_company.validate_shipping(200, 140, 1), True)
        self.assertEqual(self.test_company.validate_shipping(201, 140, 1), False)
        self.assertEqual(self.test_company.validate_shipping(200, 141, 1), False)
        self.assertEqual(self.test_company.validate_shipping(200, 140, 0), False)
        
    def test_calculate_shipping(self):
        self.assertEqual(self.test_company.calculate_shipping(200,140,100), {'nome': 'Entrega Teste', 'valor_frete': 3.0, 'prazo_dias': 6})
