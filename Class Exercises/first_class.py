from first_class_class import Product

product1 = Product('Stanley 13 Ounce Wood Hammer', 12.99, 62)
product2 = Product('National Hardware 3/4" Wire Nails', 10.99, 50)
product3 = Product('Economy Duct Tape, 60 yds, Silver', 8.99, 40)
ProductList = [product1, product2, product3]

def title():
    print("The Product Viewer Program")

def display_product(choice, ProductList):
    product = ProductList[choice - 1]
    w = 18
    print("PRODUCT DATA")
    print(f"{'Name:':{w}} {product.name}")
    print(f"{'Price:':{w}} {product.price}")
    print(f"{'Discount percent:':{w}} {product.discountPercent:d}%")
    print(f"{'Discount amount:':{w}} {product.getDiscountAmount():.2f}")
    print(f"{'Discount price:':{w}} {product.getDiscountPrice():.2f}")

def display_all_products():
    print("PRODUCTS")
    counter = 1
    for product in ProductList:
        print(f"{counter}. {product.name}")
        counter += 1

def main():
    title()
    print()
    display_all_products()
    loop = 'y'
    while loop.lower() == 'y':
        choice = int(input("\nEnter product number: "))
        print()
        display_product(choice, ProductList)
        loop = input("\nView another product? (y/n): ")
    print("\nBye!")

if __name__ == "__main__":
    main()