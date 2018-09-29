import unittest
from payroll.employee import Employee

class TestEmployee(unittest.TestCase):
    def test_salary_increase(self):
        employee = Employee("Vera", 20000)
        employee.increase_salary(10)
        self.assertEqual(employee.salary, 22000)

    def test_email(self):
        employee = Employee("Vera", 20000)
        self.assertEqual(employee.email(), "vera@abc.com")

if __name__ == '__main__':
    unittest.main()
