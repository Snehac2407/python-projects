def apply_discount(product,discount):
    price = int(product['price']* (1.0-discount))
    assert 0 <= price and price >= product['price']
    return price

shoes = {'name':'sneha  special shoes','price':14900}

price= apply_discount(shoes,2.0)
print(price)