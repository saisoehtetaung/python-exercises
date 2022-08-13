class Restaurant():
    menu = {
        "pizza" : 20000,
        "noodle" : 3000,
        "drink" : 2000,
        "soup" : 3000,
        "cafe" : 1500
    }
    
    def __init__(self):
        self.total = 0
        self.orders = []

    def orderfoods(self,food):
        self.orders.append(food)
        self.total += self.menu[food]
    
    def billResult(self):
        for orderList in self.orders:
            print(f"{orderList} : {self.menu[orderList]} ")
        


table =Restaurant()
for (key,value) in table.menu.items():
    print(f"{key} = {value}")

while True:
    order= input("What do u want to order\n (if you done \'type e\'): ")
    if order=="e":
        break
    table.orderfoods(order)

table.billResult()
print(f"Total Balance : {table.total}")


