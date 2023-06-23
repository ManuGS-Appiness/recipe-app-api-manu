from django.test import SimpleTestCase
from app import calc

class calcTestCase(SimpleTestCase):
    def test_cal_add(self):
        res = calc.add(5,10)
        self.assertEqual(res,15)
        
    def test_cal_sub(self):
        result=calc.substract(20,-30)
        self.assertEqual(result,50)
        # print("manu")
    
    def test_mul_case(self):
        resu=calc.multiple(20,30)
        self.assertEqual(resu,600)
        # print("manu")