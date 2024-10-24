class Bill:
    def __init__(self, description, cost, payment_date, payment_type, payment_recurring: bool = False):
        self._description = description
        self._cost = cost
        self._payment_date = payment_date
        self._payment_type = payment_type
        self._payment_recurring = payment_recurring

    def show_info_bill(self):
        print(f"{self._description}\n"
              f"Total coast: {self._cost}\n"
              f"Payment date: {self._payment_date}\n"
              f"{"Recurring Payment" if self._payment_recurring else "Not recurring Payment"}")

    def get_cost(self):
        return self._cost

    def get_payment_date(self):
        return self._payment_date

    def get_payment_recurring(self):
        return self._payment_recurring

    def set_cost(self, new_cost):
        self._cost = new_cost

    def set_payment_date(self, new_date):
        self._payment_date = new_date

    def set_payment_recurring(self, new_recurring: bool):
        self._payment_recurring = new_recurring

    def json_bill(self):
        return {
            "description": self._description,
            "cost": self._cost,
            "payment_date": self._payment_date,
            "payment_type": self._payment_type,
            "payment_recurring": self._payment_recurring
        }

pucpr = Bill("College Payment", 400, "30/10/2024", "credit card", )

pucpr.show_info_bill()
