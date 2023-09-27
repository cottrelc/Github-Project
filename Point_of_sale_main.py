"""
Name: Point_of_sale.py
Author: Carson Cottrell
Created: 9/2/2023
Purpose: Sell Water
"""
import Point_of_sale_class as bottle


#Cost of water for the customer
def start_ordering():
        while True:

                print(carsons_water.display_menu())
                choice = input(
                        "Enter an item to order (q to quit): ").lower()
                
                if choice == 'q':
                        break

                quantity = int(input("Enter the quantity: "))

                cart_item = carsons_water.add_to_cart(choice, quantity)

                print(cart_item)
                
def generate_receipt():
                carsons_water.calculate_total()
                print("\nreceipt: ")

                print(f"Total: ${carsons_water.total:.2f}")
                print("Thank you for hydrating yourself.")
carsons_water = bottle.CarsonsWaterbottles()
start_ordering()
generate_receipt()
