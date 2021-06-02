'''
Write a class called Product. The class should have fields called name,
amount, and price, holding the product’s name, the number of items of
that product in stock, and the regular price of the product.
There should be a method get_price that receives the number of
items to be bought and returns a the cost of buying that many items,
where the regular price is charged for orders of less than 10 items,
a 10% discount is applied for orders of between 10 and 99 items, and
a 20% discount is applied for orders of 100 or more items.
There should also be a method called make_purchase that receives the
number of items to be bought and decreases amount by that much.
'''
class product:
    def __init__(self,name,items,price):
        self.name=name;
        self.items=items
        self.price=price
    def getprice(self,n):
        if n<10:
            print("Regular price is charged for you orders")
            cost=n*self.price
            print("If you place above 9 items you get 10% discount")
            print("If you place above 99 items you get 20% discount")
        elif n>=10 and n<100:
            print("10% dicount is applied for you orders")
            cost=n*self.price
            discount=(cost*10)/100
            finalcost=cost-discount
            print("Actual Cost: ",cost)
            print("10% Discount: ",finalcost)
            print("Cost after 10% discount: ",discount)
            print("If you place above 99 items you get 20% discount")
        else:
            print("20% dicount is applied for you orders")
            cost=n*self.price
            discount=(cost*20)/100
            finalcost=cost-discount
            print("Actual Cost: ",cost)
            print("20% Discount: ",discount)
            print("Cost after 20% discount: ",finalcost)
    def my_purchase(self,n):
                if n<10:
                    print("Regular price is charged for you orders")
                    cost=n*self.price
                    print("Final cost:",cost)
                elif (n>=10) and (n<100):
                    print("10% dicount is applied for you orders")
                    cost=n*self.price
                    discount=(cost*10)/100
                    finalcost=cost-discount
                    print("Actual Cost: ",cost)
                    print("10% Discount: ",discount)
                    print("Final Cost after 10% discount: ",finalcost)
                else:
                    print("20% dicount is applied for you orders")
                    cost=n*self.price
                    discount=(cost*20)/100
                    finalcost=cost-discount
                    print("Actual Cost: ",cost)
                    print("20% Discount: ",discount)
                    print("Final Cost after 20% discount: ",finalcost)
p=product("PEN",200,5)
n=int(input("Enter Number of pens you want to buy:"))
p.getprice(n)
n=int(input("Enter Number of pens you want to buy:"))
p.my_purchase(n)
