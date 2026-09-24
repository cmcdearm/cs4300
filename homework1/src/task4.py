def calculate_discount(price,discount):
    if price < 0 or discount < 0:
        raise ValueError("Price and discount must be non-negative.")
    if discount > 100:
        raise ValueError("Discount cannot be greater than 100%.")
    discounted_price = price - (price * discount / 100)
    return discounted_price