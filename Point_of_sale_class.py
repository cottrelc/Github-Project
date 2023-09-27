"""
Name: Point_of_sale.py
Author: Carson Cottrell
Created: 9/14/2023
Purpose: Sell Water
"""
#Cost of water for the customer
WATERBOTTLE_COST = 1.55
# TODO: Get int input from user how many water bottles sold
class CarsonsWaterbottles:
    def __init__(self):
        self._qty_waterbottle = 0
        self.menu_items = ["Water Bottle" , "Diet Water" , "Soda", "Diet Soda" ]
        self.menu_prices = [1.55 , 1.00 , 2.00, 5.00 ]
        #Store the quantity of items
        self.cart = [0, 0, 0, 0]

#--------------------------------------Class Properties----------------------------#
    @property
    def name(self):
        return self._qty_waterbottle
    
    @name.setter
    def name(self, qty_waterbottle):
        self._qty_waterbottle = qty_waterbottle



    def get_menu_items(self) -> list:

        return self.menu_items
    
    def get_menu_prices(self) -> list:
        return self.menu_prices
#-----------------------------------------ADD Items to Cart -------------------------#
    def add_to_cart(self, choice: int, quantity: int) -> str:
        """Add items choice (list) and quantity to cart.
        
        Parameters:
        choice (int): Index number of list item
        quantity (int): How many items purchased
        
        Returns:
        cart_itme (str): String representation of cart
        """

        try:
            index = int(choice) -1
            if 0 <= index < len(self.menu_items):
                item = self.menu_items[index]
                price = self.menu_prices[index]
                self.cart[index] = quantity + self.cart[index]
                cart_item = f"{quantity} {item}(s) added to the cart"
                return cart_item
            else:
                print("Invalid choice. Please select a valid item number.")

        except ValueError:
            print("Invalid input. Please enter a valid item number.")
    
    
    
    #--------------------------------Display Menu-----------------------------------#
    
    def  display_menu(self) -> str:
        display = ""
        #for n in range(3): 
        #    print(f"{self.menu_items[n]} {self.menu_prices[n]}")
        for n in range(len(self.menu_items)): 
            i = n + 1
            display += f"({i}){self.menu_items[n]} {self.menu_prices[n]:.2f}\n"
        return display
    
    def calculate_total(self):
        """Calculate cost of items purchased
        
        Returns
        
        total cost of items
        """
        self.total = 0
        for i in range(4):
            self.total += self.cart[i] * self.menu_prices[i]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def get_number_water(self):
        if self._number_of_water > 0:
            return self._number_of_water
        else:
            return "You must order at least one water bottle"


    def get_total_sale(self):
        return self._total_sale


    def get_qty_waterbottle(self, number_of_water: int = 1):
        # TODO: Calculate cost of the water purchased
        self._number_of_water = number_of_water
        self._total_sale = self._number_of_water * WATERBOTTLE_COST

