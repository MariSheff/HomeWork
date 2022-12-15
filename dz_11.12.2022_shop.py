#категория продукта
class CategoryProduct:

    def __init__(self, category_name):
        self.category_name = category_name

    def __str__(self):
        return f'{self.category_name}'

# ТОВАР
class Product(CategoryProduct):

    def __init__(self, name_product, category, description=None, price=0, count_product=0):
        self.name_product = name_product
        self.category = category
        self.description = description
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
        self.total_count = 0
        self.total_price = 0
        self.lst_cart = []

    def __str__(self):
        return f'{self.lst_cart} на сумму {self.total_price}'

#добавление товара в корзину, пересчет остатка товара
    def add_product(self, product, count):
        if product.count_product >= count:
            self.count += count
            self.lst_cart.append(product.name_product)
            self.total_price += self.count * product.price
            self.total_count += count
        else:
            print(f'{product.name_product} нет в наличии')

#удаление из корзины, нужен пересчет остатка товара
    def dell_product(self, product, count):
        print(self.count)
        self.count -= count
        print(self.count)
        if self.count == 0:
            self.lst_cart.remove(product.name_product)
        product.count_product += count
        self.total_count -= count
        self.total_price -= count*product.price

#очистка корзины после покупки или клиентом
    def clearCart(self):
        self.lst_cart.clear()
        self.total_count = 0
        self.total_price = 0
        print("Корзина пуста")

    def get_goods(self):
        return self.lst_cart

    def get_total(self):
        return f'{self.total_count} мешков на общую сумму {self.total_price}'


class Client(ClientCart, Product):

    def __init__(self, name):
        self.name = name
        self.count_bought = 0
        self.lst_cart = []
        self.total_count = 0
        self.total_price = 0
        self.count = 0
    def __str__(self):
        return f'{self.lst_cart} на сумму {self.total_price}'

    def add_product(self, product, count):
         super().add_product(product, count)
        #  if product.count_product >= count:
        #     self.count_bought += count
        #     self.lst_cart.append([product.name_product, self.count_bought])
        #     product.count_product -= self.count_bought
        #
        # else:
        #     print('Товара нет в наличии')
    def dell_product_from_cart(self, product, count):
        super().dell_product(product, count)


    def get_goods(self):
        return self.lst_cart

class HistorySales:
    pass

dry_food = CategoryProduct('Dry food')
natural_food = CategoryProduct('Natural food')

print(dry_food.__str__())
print(natural_food.__str__())

savita = Product("SAVITA", dry_food.category_name, 'Корм SAVITA беззерновой корм для взрослых собак с мясом дикого кабана', 5000, 10)
go = Product("GO!", dry_food.category_name, 'Корм GO! для щенков со свежим ягненком', 6000, 15)
wolfsblut = Product("Wolfsblut Wild Pacific", dry_food.category_name, 'Дикий океан для взрослых собак с лососем и сельдью', 9000, 20)

print(wolfsblut.__str__()) #описание товара
print(Product.available_product(go)) # проверка наличия товара

client1 = Client('Mari')
client2 = Client('Inga')
client1.add_product(wolfsblut, 6)
client2.add_product(go, 6)

print(client1.__str__())
print(client2.__str__())

client1.dell_product(wolfsblut, 2)
print(client1.__str__())



