import unittest

from rate_calculator import CustomerRate


class MVPAnnualRateTest(unittest.TestCase):

    def test_kelly_rate(self):
        rates = dict(allergies="0.01", sleep_apnea='0.06', heart_disease='0.17')
        kelly = CustomerRate(name="Kelly", age="50", gender="female", health_condition="allergies", base_cost=100,
                             condition_rates=rates)

        # Test  Age 18 or Older
        self.assertEqual(kelly.check_age, True)
        # Test Rate
        self.assertEqual(kelly.annual_rate(), 210.20)
        # Test Change Health Condition
        kelly.change_condition("sleep_apnea")
        self.assertEqual(kelly.annual_rate(), 221.2)

    def test_brad_rate(self):
        rates = dict(allergies="0.01", sleep_apnea='0.06', heart_disease='0.17')
        brad = CustomerRate(name="Brad", age="20", gender="male", health_condition="heart_disease", base_cost=100,
                            condition_rates=rates)

        self.assertEqual(brad.check_age, True)
        self.assertEqual(brad.annual_rate(), 117.00)

    def test_josh_rate(self):
        rates = dict(allergies="0.01", sleep_apnea='0.06', heart_disease='0.17')
        josh = CustomerRate(name="Josh", age="40", gender="male", health_condition="sleep_apnea", base_cost=100,
                            condition_rates=rates)

        self.assertEqual(josh.check_age, True)
        self.assertEqual(josh.annual_rate(), 190.80)


if __name__ == '__main__':
    unittest.main()
