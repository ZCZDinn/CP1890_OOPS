from dataclasses import dataclass

@dataclass
class Product:
    name:str = ""
    price:float = 0.0
    discountPercent:int = 0.0

    def getDiscountAmount(self) -> float:
        return self.price * (self.discountPercent / 100)
    def getDiscountPrice(self) -> float:
        return self.price - self.getDiscountAmount()