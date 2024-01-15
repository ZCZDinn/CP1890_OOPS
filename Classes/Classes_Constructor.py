class Product:
    def __init__(self, name = "", price=0.0, discount_percent=0):
        self.name = name
        self.price = price
        self.discount_percent = discount_percent

    def getDiscountAmount(self):
        return self.price * (self.discount_percent / 100)

    def getDiscountPrice(self):
        return self.price - self.getDiscountAmount()