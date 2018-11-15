class Car:
    def __init__(self, price):
        self.price = price

    def raised_fee(self):
        self.price *= self.raise_rate

    @classmethod
    def include_fee(cls, price):
        return cls(1.1 * price)

    @classmethod
    def raise_rate(cls, raise_rate):
        cls.raise_rate = 1 + raise_rate


if __name__ == '__main__':
    car1 = Car(100)
    car2 = Car.include_fee(100)
    print(car1.price)
    print(car2.price)

    Car.raise_rate(0.3)
    car1.raised_fee()
    car2.raised_fee()

    print(car1.price)
    print(car2.price)