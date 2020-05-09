def getProduct(name, price, color):
    return dict(
        name=name,
        price=price,
        color=color,
    )

def getCollectionDescriptionString(collection):
    result = ''
    
    for element in collection:
        result += f'We\'ve got a {element["color"]} {element["name"]} here that is worth ${element["price"]}. \n'
        
    return result
    
products = list()

products.append(getProduct('Apple', 999, 'red'))
products.append(getProduct('Block', 10, 'grey'))
products.append(getProduct('Pillow', 39.9, 'white'))

print(getCollectionDescriptionString(products))


