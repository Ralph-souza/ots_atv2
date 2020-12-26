from product import Product
from category import Category

categories = []
products = []


def valid_value(value: float) -> float:
    try:
        while float(value) <= 0:
            value = float(input("Insert a value bigger than 0: "))
    except ValueError:
        value = valid_value(float(input("Type another value: ")))
    return value


def input_sku():
    initial_product = input("Enter product's SKU: ")
    return search_product(initial_product)


def create_product() -> None:
    print("\nCreate new product")

    product = Product()
    sku_not_valid = True
    sku = ""
    while sku_not_valid:
        sku = input("Product SKU: ")
        p = search_product(sku)
        if not p:
            sku_not_valid = False
            break
        print("Invalid SKU, please try again.")

    product.set_sku(sku)
    name = input("Insert product's name: ")
    product.set_name(name)
    value = float(input("Insert product's value: "))
    product.set_value(valid_value(value))
    weight = float(input("Insert product's weight: "))
    product.set_weight(valid_value(weight))
    height = float(input("Insert product's height: "))
    product.set_height(valid_value(height))
    length = float(input("Insert product's length: "))
    product.set_length(valid_value(length))
    width = float(input("Insert product's width: "))
    product.set_width(valid_value(width))
    description = input("Insert product's description: ")
    product.set_description(description)

    categories = input("Insert product's category: ")
    product.set_categories(categories)

    products.append(product)


def product_detail():
    p = input_sku()
    if not p:
        print("Product not found.")
    else:
        print(p)


def search_product(sku: str) -> Product:
    for product in products:
        if product.get_sku() == sku:
            return product


def list_product():
    if len(products) > 0:
        print("\nList products")
        for product in products:
            print(product)


def update_product():
    p = input_sku()
    if not p:
        print("Product not found.")
    else:
        print(p)

        name = input("Insert product's name: ")
        p.set_name(name)
        value = float(input("Insert product's value: "))
        p.set_value(valid_value(value))
        weight = float(input("Insert product's weight: "))
        p.set_weight(valid_value(weight))
        height = float(input("Insert product's height: "))
        p.set_height(valid_value(height))
        length = float(input("Insert product's length: "))
        p.set_length(valid_value(length))
        width = float(input("Insert product's width: "))
        p.set_width(valid_value(width))
        description = input("Insert product's description: ")
        p.set_description(description)


def delete_product():
    p = input_sku()
    if not p:
        print("Product not found.")
    else:
        products.remove(p)
        print("Product deleted.")


def create_category():
    print("\nCreate new category")

    category = Category()

    category.set_name(input("Insert category's name: "))
    if not categories:
        category.set_id(1)
        categories.append(category)
    else:
        new_id = categories[-1].get_id() + 1
        category.set_id(new_id)
        categories.append(category)
    print("Success.")


def search_category(name: str) -> Product:
    for category in categories:
        if category.get_name().lower() == name.lower():
            return category


def list_category():
    print("\nCategories: ")

    for c in categories:
        print(c)


def menu():
    options = ['Create new product', 'Create new category', 'List product', 'List category', 'Product detail',
               'Update product', 'Delete product', 'Exit']
    print("\nMenu")

    for i, option in enumerate(options):
        print(f"[{i+1}] - {option}")

    menu_option = int(input("Choose an option: "))
    return menu_option


while True:
    try:
        menu_option = menu()
        if menu_option == 1:
            create_product()
        elif menu_option == 2:
            create_category()
        elif menu_option == 3:
            list_product()
        elif menu_option == 4:
            list_category()
        elif menu_option == 5:
            product_detail()
        elif menu_option == 6:
            update_product()
        elif menu_option == 7:
            delete_product()
        elif menu_option == 8:
            exit(0)
        else:
            print("Choice unavailable. Try another.")
    except ValueError:
        print("Choice unavailable. Try another.")
