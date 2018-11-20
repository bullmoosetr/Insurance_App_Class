class CustomerRate(object):

    def __init__(self, name, base_cost, age, gender, health_condition, condition_rates):

        # Equation adds $20 to the base rate every 5 years
        self.base_cost = (int(age) - 18) // 5 * 20 + int(base_cost)
        self.age = int(age)
        self.health_condition = health_condition
        self.gender = gender
        self.name = name
        self.condition_rates = condition_rates

    @property
    def check_age(self):
        if self.age >= 18:
            return True
        else:
            return False

    def base_cost_increase(self):
        # Equation adds $20 to the base rate every 5 years over 18
        if self.age >= 18:
            return self.base_cost
        else:
            return "Sorry but you must be 18 years or older to purchase insurance."

    def condition_cost_increase(self):

        condition_cost_increase = float(self.condition_rates[self.health_condition])
        return condition_cost_increase * self.base_cost

    def annual_rate(self):
        # Condition Cost Increase due to health condition
        condition_cost_increase = self.base_cost * float(self.condition_rates[self.health_condition])

        # Check the Customer's gender to determine if they qualify for the $12 discount
        if self.gender == "female":
            # Annual Rate
            return condition_cost_increase + self.base_cost - 12
        else:
            return condition_cost_increase + self.base_cost

    # Added this to show how easy it is to change the properties
    def change_condition(self, new_condition):
        self.health_condition = new_condition
