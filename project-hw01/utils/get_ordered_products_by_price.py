from models.product import Product


def get_ordered_products_by_price(products: list[Product]) -> list[Product]:
    products.sort(key=lambda product: product.get_price())
    products.reverse()
    return products
