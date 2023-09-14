"""
Name: Point_of_sale.py
Author: Carson Cottrell
Created: 9/2/2023
Purpose: Sell Water
"""
#Cost of water for the customer
WATERBOTTLE_COST = 1.55
# TODO: Get int input from user how many water bottles sold
class CarsonsWaterbottles:
    def __init__(self):
        pass
    def get_input(self):
        self.number_of_water = int(input("Enter number of water bottles: "))
        
    def calculate(self):
        # TODO: Calculate cost of the water purchased
        self.total_sale = self.number_of_water * WATERBOTTLE_COST
    def display(self):
        # TODO: Display transaction for customer
        print(f"Your Water Bottles were: ${self.total_sale:,.2f}")


carsons_water = CarsonsWaterbottles()
carsons_water.get_input()
carsons_water.calculate()
carsons_water.display()