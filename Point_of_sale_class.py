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
        pass
        
    def get_number_water(self):
        if self._number_of_water > 0:
            return self._number_of_water
        else:
            return "You must order at least one water bottle"


    def get_total_sale(self):
        return self._total_sale


    def calculate(self, number_of_water):
        # TODO: Calculate cost of the water purchased
        self._number_of_water = number_of_water
        self._total_sale = self._number_of_water * WATERBOTTLE_COST

