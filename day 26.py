class Product:
    def __init__(self, code, name, price, stock):
        self.code = code
        self.name = name
        self.price = price
        self.stock = stock

    def display_info(self):
        print(f"Product Code: {self.code}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Stock: {self.stock} units")
        print()

class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Product '{product.name}' added to the store.")

    def display_products(self):
        if not self.products:
            print("No products in the store yet.")
        else:
            print(f"Products in '{self.name}':")
            for product in self.products:
                product.display_info()

    def find_product_by_code(self, code):
        for product in self.products:
            if product.code == code:
                print(f"Product with code '{code}' found:")
                product.display_info()
                return
        print(f"Product with code '{code}' not found in '{self.name}'.")

# Contoh penggunaan
if __name__ == "__main__":
    # Membuat toko
    my_store = Store("My Super Store")

    # Menambahkan beberapa produk ke toko
    p1 = Product("P001", "Keyboard", 49.99, 100)
    p2 = Product("P002", "Mouse", 19.99, 150)
    p3 = Product("P003", "Monitor", 199.99, 50)

    my_store.add_product(p1)
    my_store.add_product(p2)
    my_store.add_product(p3)

    # Menampilkan semua produk dalam toko
    my_store.display_products()

    # Mencari produk berdasarkan kode
    my_store.find_product_by_code("P002")
    my_store.find_product_by_code("P004")  # Kode produk yang tidak ada dalam toko
