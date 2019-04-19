from random import randint

"""Classes for melon orders."""
class AbstractMelonOrder():
    """Abstract melon order class for order type subclasses to inheret from."""
    def __init__(self, species, qty, country_code=None):
        self.species = species
        self.qty = qty
        self.shipped = False
        if country_code:
            self.country_code = country_code

    def get_base_price(self):
        return randint(5, 9)

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()
        
        if self.species.lower() == "christmas melon":
            base_price *= 1.5 

        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international":
            if self.qty < 10:
                total += 3

        return total

    def mark_shipped(self):
        """Record the fact that an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"
    tax = 0.17


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """A melon order from the U.S. government."""
    order_type = "government"
    tax = 0.0
    passed_inspection = None

    def mark_inspection(self, passed):
        """Record the fact that an order has passed inspection."""

        self.passed_inspection = passed

