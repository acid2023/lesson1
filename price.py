def format_price(price):
    price = int(price)
    return('Цена: '+str(price).upper() + ' руб.')
price = format_price(56.24)
print(price)