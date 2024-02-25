class Order: 
    def __init__(self):
        self.customerInfo = ""
        self.items = []
        self.shippingAddress = ""

class Checkout:
    def __init__(self, discount, total):
        self.taxRate = 0.07
        self.discount = discount
        self.initialTotal = total

    def price_total(self):
        return self.initialTotal - self.discount * self.initialTotal + self.taxRate * self.initialTotal
    
class Validate:
    def __init__(self, items, address):
        self.availableItems = ["item1", "item2", "item3"]
        self.items = items
        self.address = address

    def validate(self):
        if len(self.items) == 0:
            return False
        if len(self.address) == 0:
            return False
        for item in self.items:
            if item not in self.availableItems:
                return False
        else:
            return True
        
class SendConfirmation:
    def __init__(self, email, items, address):
        self.email = email
        self.items = items
        self.address = address

    def send(self):
        print(f"Email sent to {self.email} confirming items: {self.items}")

class UpdateInventory:
    def __init__(self, size):
        self.size = size

    def update(self):
        size -= 1
        print("Inventory updated")


if __name__ == "__main__":
    order = Order()
    checkout = Checkout(0.1, 100)
    checkout.price_total()
    validate = Validate(["item1", "item2"], "123 Main St")
    validate.validate()
    send = SendConfirmation("email", ["item1", "item2"], "123 Main St")
    send.send()