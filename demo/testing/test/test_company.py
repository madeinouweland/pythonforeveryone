import unittest
from payroll.company import Company
from payroll.employee import Employee

class TestCompany(unittest.TestCase):
    def test_calculate_average_salary(self):
        average_salary = Company().calculate_average_salary([
            Employee("Vera", 100),
            Employee("Chuck", 200),
            Employee("Dave", 300),
        ])
        self.assertEqual(average_salary, 200)
