def main(list_input, tax=0.16):
    name_products = list_input
    items = [{'product': name, 'price': (index + 1) * 100} for index, name in enumerate(name_products)]
    items_with_taxes = list(map(lambda item: add_taxes(item, tax), items.copy()))
    for item in items_with_taxes:
        print(f"Producto: {item['product']}, Precio: {item['price']}, Impuestos: {item['taxes']}, A pagar: {item['price'] + item['taxes']}")

def add_taxes(item, tax):
    try:
        item['taxes'] = item['price'] * tax
    except KeyError:
        print(f"Error: El item {item} no tiene un precio.")
    except TypeError:
        print(f"Error: El precio de {item} no es un número válido.")
    return item

if __name__ == "__main__":
    listProducts = ['T-shirt', 'coat', 'jeans', 'skit', 'hoobie','sneakers', 'hat', 'joggers', 'gloves', 'boots','leggings', 'suit', 'ligthweith', 'top', 'cardigan', 'Sweter']
    main(listProducts)
