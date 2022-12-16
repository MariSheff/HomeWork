#категория продукта
class CategoryProduct:

    def __init__(self, category_name):
        self.category_name = category_name

    def __str__(self):
        return f'{self.category_name}'

# ТОВАР
class Product(CategoryProduct):

    def __init__(self, name_product, category, description=None, value=0, price=0, count_product=0):
        self.name_product = name_product
        self.category = category
        self.description = description
        self.value = value
        self.price = price
        self.count_product = count_product #доступное количество на складе

    def __str__(self):
        return f'{self.description} \n   цена: {self.price}:, в наличии {self.count_product} меш.'

    # в наличии
    def available_product(self):
        if self.count_product>0:
            print(f'{self.name_product} в наличии {self.count_product} меш.')
            return True
        else:
            print(f'{self.name_product} нет в наличии')
            return False

#корзина клиента
class ClientCart(Product):

    def __init__(self):
        self.count = 0
        self.total_value = 0
        self.total_count = 0
        self.total_price = 0
        self.lst_cart = []

    def __str__(self):
        return f'{self.lst_cart} на сумму {self.total_price}, объем {self.total_value} кг'

    #добавление товара в корзину, пересчет остатка товара
    def add_product(self, product, count):
        if product.count_product >= count:
            self.count += count
            self.lst_cart.append(product.name_product)
            self.total_price += self.count * product.price
            self.total_count += count
            self.total_value += count * product.value
            print(self.total_value, product.value)
        else:
            print(f'{product.name_product} нет в наличии')

    #удаление из корзины, пересчет остатка товара
    def dell_product(self, product, count):
        print(self.count)
        self.count -= count
        print(self.count)
        if self.count == 0:
            self.lst_cart.remove(product.name_product)
        product.count_product += count
        self.total_count -= count
        self.total_price -= count * product.price
        self.total_value -= count * product.value
        print(self.total_value, product.value)
    #очистка корзины клиентом
    def clearCart(self):
        self.lst_cart.clear()
        self.total_count = 0
        self.total_price = 0
        self.total_value = 0
        print("Ваша корзина очищена")



class Client(ClientCart, Product):

    def __init__(self, name):
        self.name = name
        self.lst_cart = []
        self.total_value = 0
        self.total_count = 0
        self.total_price = 0
        self.count = 0
    def __str__(self):
        return f'{self.lst_cart} на сумму {self.total_price}, объем {self.total_value} кг'

    def add_product(self, product, count):
         super().add_product(product, count)

    def dell_product_from_cart(self, product, count):
        super().dell_product(product, count)

    def get_products(self):
        return self.lst_cart

    def get_total(self):
        return f'{self.total_count} меш. на общую сумму {self.total_price}'

    def clearCart(self):
        super().clearCart()

class HistorySales:
    pass

dry_food = CategoryProduct('Dry food')
natural_food = CategoryProduct('Natural food')

print(dry_food.__str__())
print(natural_food.__str__())

savita = Product("SAVITA", dry_food.category_name, 'Корм SAVITA беззерновой корм для взрослых собак с мясом дикого кабана',12, 5000, 10)
go = Product("GO!", dry_food.category_name, 'Корм GO! для щенков со свежим ягненком', 12, 6000, 15)
wolfsblut = Product("Wolfsblut Wild Pacific", dry_food.category_name, 'Дикий океан для взрослых собак с лососем и сельдью',12, 9000, 20)

print(wolfsblut.__str__()) #описание товара

print(Product.available_product(go)) # проверка наличия товара
print(Product.available_product(wolfsblut))

client1 = Client('Mari')
client2 = Client('Inga')

client1.add_product(wolfsblut, 6)
print(client1.__str__())
client1.dell_product_from_cart(wolfsblut, 2)

client2.add_product(go, 6)
client2.add_product(savita, 5)
print(client2.get_products())

print(client1.__str__())
print(client2.__str__())

print(f'Client {client2.name}: {client2.get_total()}')
print(f'Client {client1.name}: {client1.get_total()}')

client1.clearCart()


