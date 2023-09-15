class product:
    def __init__(self, name: str, price: float):
        self.price = price
        self.name = name

class combo:
    def __init__(self, name: str, products:[], is_gift_pack:bool):
        self.name=name
        self.products=products
        if(is_gift_pack):
            self.discount = 25
        else:
            self.discount = 10

    def calculate_price(self) -> float:
        price = 0
        for i in range(0, len(self.products)):
            price+= self.products[i].price
        
        return price - (price * self.discount / 100) 
    
class Part2:
    item_1 = product("Item 1", 200.0)
    item_2 = product("Item 2", 400.0)
    item_3 = product("Item 3", 600.0)

    itens_combo_1 = []
    itens_combo_1.append(item_1)
    itens_combo_1.append(item_2)
    combo_1 = combo(f"Combo 1 ({item_1.name} + {item_2.name})", itens_combo_1, False)

    itens_combo_2 = []
    itens_combo_2.append(item_2)
    itens_combo_2.append(item_3)
    combo_2 = combo(f"Combo 2 ({item_2.name} + {item_3.name})", itens_combo_2, False)

    itens_combo_3 = []
    itens_combo_3.append(item_1)
    itens_combo_3.append(item_3)
    combo_3 = combo(f"Combo 3 ({item_1.name} + {item_3.name})", itens_combo_3, False)

    itens_combo_4 = []
    itens_combo_4.append(item_1)
    itens_combo_4.append(item_2)
    itens_combo_4.append(item_3)
    combo_4 = combo(f"Combo 4 ({item_1.name} + {item_2.name} + {item_3.name})", itens_combo_4, True)

    def print_catalog(self):
        print(f"\nOnline Store \n"+
              f"{self.get_line()}"+
              "Product(S)                            Price \n" +
              f"{self.item_1.name}                                {self.item_1.price} \n" +
              f"{self.item_2.name}                                {self.item_2.price} \n" +
              f"{self.item_3.name}                                {self.item_3.price} \n" +
              f"{self.combo_1.name}             {self.combo_1.calculate_price()} \n"+
              f"{self.combo_2.name}             {self.combo_2.calculate_price()} \n"+
              f"{self.combo_3.name}             {self.combo_3.calculate_price()} \n"+
              f"{self.combo_4.name}    {self.combo_4.calculate_price()} \n"+
              f"{self.get_line()}"+
              "For delivery Contact: 98764678899")
    def get_line(self) -> str:
        return "___________________________________________ \n"

part2 = Part2().print_catalog()
    
