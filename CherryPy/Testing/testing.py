import unittest
from data import Employee,test
from unittest.mock import patch

# class Test_t1(unittest.TestCase):
    
#     @classmethod
#     def setUpClass(cls):
#         print("Setup")
        
#     @classmethod
#     def tearDownClass(cls):
#         print("\nTearDown")
    
#     def test_add(self):
#         self.assertEqual(test.add(10,5),15)
#         self.assertEqual(test.add(-1,-1),-2)
        
#     def test_subtract(self):
#         self.assertEqual(test.subtract(10,5),5)
        
#     def test_multiply(self):
#         self.assertEqual(test.multiply(10,5),50)
        
#     def test_divide(self):
#         self.assertEqual(test.divide(10,5),2)
        
#         with self.assertRaises(ValueError):
#             test.divide(10,0)

            
           
            
class Test_Employee(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("Setup")
        
    @classmethod
    def tearDownClass(cls):
        print("\nTearDown")
    
    def setUp(self):
        self.emp_1 = Employee('Kush', 'Rastogi', 50000)
        self.emp_2 = Employee('Sagar', 'Singhal', 60000)
    
    
    def test_email(self):      
        self.assertEqual(self.emp_1.email, 'Kush.Rastogi@email.com')
        self.assertEqual(self.emp_2.email, 'Sagar.Singhal@email.com')

        self.emp_1.first='Shubh'
        self.emp_2.first='Pranshu'
        
        self.assertEqual(self.emp_1.email, 'Shubh.Rastogi@email.com')
        self.assertEqual(self.emp_2.email, 'Pranshu.Singhal@email.com')
        
        
    def test_fullname(self):
       
        self.assertEqual(self.emp_1.fullname, 'Kush Rastogi')
        self.assertEqual(self.emp_2.fullname, 'Sagar Singhal')
        
        self.emp_1.first='Shubh'
        self.emp_2.first='Pranshu'
        
        self.assertEqual(self.emp_1.fullname, 'Shubh Rastogi')
        self.assertEqual(self.emp_2.fullname, 'Pranshu Singhal')
        
        
    def test_apply_raise(self):
        
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()
        
        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)
        
    def test_monthly_schedule(self):
        with patch('data.requests.get') as mocked_get:
            mocked_get.return_value.ok=True
            mocked_get.return_value.text='Success'
            
            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Rastogi/May')
            self.assertEqual(schedule,'Success')
            

if __name__ == '__main__':
    unittest.main()