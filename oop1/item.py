class Item:
    def __init__(self,name:str,price:float,quantity=0) -> None:
        assert price >=1 , f"Price should more than or equal to 1"  #เขียนเงื่อนไข
        assert quantity >=1 , f"Quantity should more than or equal to 1"
        
        #รู้ ชื่อสินค้า ราสินค้า จำนวนสินค้า
        self.name = name
        self.price = price
        self.quantity = quantity


    def calculate_total_price(self):
        #ราคาสุทธิ ช ราคาสินค้า * จำนวนสินค้า
        return self.price * self.quantity

    def __del__(self):
        print(f"Object Destroyed")

if __name__ == "__main__":
    #create item
    item1 = Item("cup",0.5,0) #50
    item2 = Item("cone",10,3) #30
    print(f"***Total Price***")
    print(f"{item1.name} {item1.calculate_total_price()}")
    print(f"{item2.name} {item2.calculate_total_price()}")