from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        discount_percentage = self.percent / 100
        total_price = product.get_price() * quantity * (1 - discount_percentage)
        return total_price


class SecondHalfPrice(Promotion):
    def apply_promotion(self, product, quantity):
        if quantity >= 2:
            discounted_quantity = quantity - (quantity // 2)
            total_price = discounted_quantity * product.get_price()
            return total_price
        else:
            return product.get_price() * quantity


class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity):
        if quantity >= 3:
            total_price = product.get_price() * (quantity - (quantity // 3))
            return total_price
        else:
            return product.get_price() * quantity
