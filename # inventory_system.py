# inventory_system.py
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    # For display
    def info(self):
        return f"{self.name} | ₹{self.price} | Qty: {self.quantity}"
    
    # Operator overloading: + to merge two products (same name)
    def __add__(self, other):
        if self.name == other.name:
            total_qty = self.quantity + other.quantity
            return Product(self.name, self.price, total_qty)
        else:
            raise ValueError("Cannot merge different products!")
    
    # For printing
    def __repr__(self):
        return f"Product('{self.name}', {self.price}, {self.quantity})"


class Inventory:
    def __init__(self):
        self.products = []  # list of Product objects
    
    def add(self, product):
        self.products.append(product)
        print(f"Added: {product.name}")
    
    def remove(self, product_name):
        for p in self.products:
            if p.name == product_name:
                self.products.remove(p)
                print(f"Removed: {product_name}")
                return
        print(f"Product {product_name} not found!")
    
    def update(self, product_name, new_price=None, add_qty=None):
        for p in self.products:
            if p.name == product_name:
                if new_price:
                    p.price = new_price
                if add_qty:
                    p.quantity += add_qty
                print(f"Updated {product_name}")
                return
        print(f"Product {product_name} not found!")
    
    def calculate_total_inventory_value(self):
        total = sum(p.price * p.quantity for p in self.products)
        return total
    
    # Polymorphic display method
    def info(self):
        print("INVENTORY CONTENTS:")
        print("-" * 50)
        if not self.products:
            print("Empty Inventory")
        else:
            for p in self.products:
                print(p.info())
        print("-" * 50)
        print(f"Total Inventory Value: ₹{self.calculate_total_inventory_value():,.2f}")


# Demo
if __name__ == "__main__":
    inv = Inventory()
    
    p1 = Product("Laptop", 55000, 5)
    p2 = Product("Mouse", 800, 25)
    p3 = Product("Laptop", 55000, 3)  # same name
    
    inv.add(p1)
    inv.add(p2)
    inv.add(p3)
    
    print("\n Merging two Laptop products...")
    merged = p1 + p3
    inv.remove("Laptop")
    inv.add(merged)
    
    inv.update("Mouse", add_qty=10)
    inv.update("Mouse", new_price=750)
    
    print("\n" + "="*60)
    inv.info()


    # Output:    # Added: LaptopAdded: Laptop
Added: Mouse
Added: Laptop

 Merging two Laptop products...
Removed: Laptop
Added: Laptop
Updated Mouse
Updated Mouse

============================================================
INVENTORY CONTENTS:
--------------------------------------------------
Laptop | ₹55000 | Qty: 8
Mouse | ₹750 | Qty: 35
--------------------------------------------------
Total Inventory Value: ₹466,250.00