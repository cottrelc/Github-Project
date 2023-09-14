"""
Name: Point_of_sale.py
Author: Carson Cottrell
Created: 9/2/2023
Purpose: Sell Water
"""
import Point_of_sale_class as bottle


#Cost of water for the customer
def get_input():
        number_of_water = int(input("Enter number of water bottles: "))
        return number_of_water
def display():
        # TODO: Display transaction for customer
        number_of_water = carsons_water.get_number_water()
        total_sale = carsons_water.get_total_sale()
        print(f"Number of Water Bottles: {number_of_water}")
        print(f"Your Water Bottles were: ${total_sale:,.2f}")
carsons_water = bottle.CarsonsWaterbottles()
number_of_water = get_input()
carsons_water.calculate(number_of_water)
display()