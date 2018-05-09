class ShoppingCart():
 
    def __init__(self):
        self.total = 0
        self.items = dict()
 
    def add_item(self,item_name,quantity,price):
        """This method should adds the cost of the added items to the current value of total , and 
        also adds an entry to the items dict such that the key is the item_name and the value is the quantity of the item """
        self.total = self.total + (price*quantity)
        self.items[item_name] = quantity
 
    def remove_item(self,item_name,quantity,price):
        if item_name in self.items:
           if quantity < self.items[item_name] and quantity > 0:
               self.items[item_name] -= quantity
               self.total -= price*quantity


        elif quantity >= self.items[item_name]:
           self.total -= price*self.items[item_name]
           del self.items[item_name]

 
    def checkout(self,cash_paid):
        """ return the customer's balance"""
        #if cash paid is less than total
        if cash_paid < self.total:
            return "Cash paid not enough"
        else:
            return cash_paid - self.total
 
class Shop(ShoppingCart):
 
    def __init__(self):
        ShoppingCart.__init__(self)    
        self.quantity = 100   
 
    def remove_item(self):
        self.quantity = self.quantity - 1
 
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("MacBook",100,450)
    cart.add_item("MacAir",600,650)
    cart.add_item("HP",140,200)
    cart.add_item("Acer",80,320)
 
    #show all items
    print("All items: ",cart.items)
    #show total
    print("current Total:",cart.total)
 
    #remove macbook
    cart.remove_item("MacBook",120,450)
 
    print()
    #show all items
    print("after removing Macbook,120,450:",cart.items)
    print("Total after removing:",cart.total)
 
    print()
    print("after payment of 200")
    print(cart.checkout(200))
 
    print()
    #instance of shop
    shop = Shop()
    shop.remove_item()
    print("Quantity in shop:",shop.quantity)
