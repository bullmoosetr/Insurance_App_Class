from rate_calculator import CustomerRate


def rate_summary_pretty_print():
    rates = dict(allergies="0.01", sleep_apnea='0.06', heart_disease='0.17')
    kelly = CustomerRate(name="Kelly", age="50", gender="female", health_condition="allergies", base_cost=100,
                         condition_rates=rates)

    return print("Thanks for considering TICKLE for insurance {0}! At this time we can offer you an annual rate of ${1} ! \n" \
                 "Please see more details below. \n" \
                 "Base Cost: ${2}\n" \
                 "Condition Rate: %{3} \n" \
                 "Annual Rate: ${1} \n".format(kelly.name, str(kelly.annual_rate()), str(float(kelly.base_cost_increase())), kelly.condition_cost_increase()))


rate_summary_pretty_print()
