# WRITE YOUR FUNCTIONS HERE
import pdb

def get_pet_shop_name(dictionary):
    pet_shop_name = dictionary["name"]
    return pet_shop_name

def get_total_cash(dictionary):
    total_cash = dictionary["admin"]["total_cash"]
    return total_cash

def add_or_remove_cash(dictionary, amount):
    dictionary["admin"]["total_cash"] += amount

def add_or_remove_cash(dictionary, amount):
    dictionary["admin"]["total_cash"] += amount

def get_pets_sold(dictionary):
    pets_sold = dictionary["admin"]["pets_sold"]
    return pets_sold

def increase_pets_sold(dictionary, num_sold):
    dictionary["admin"]["pets_sold"] += num_sold

def get_stock_count(dictionary):
    stock_count = len(dictionary["pets"])
    return stock_count

def get_pets_by_breed(dictionary, breed):
    breed_list = []
    for pet in dictionary["pets"]:
        if pet["breed"] == breed:
            breed_list.append(pet)
    return breed_list

def find_pet_by_name(dictionary, name):
    for pet in dictionary["pets"]:
        if pet["name"] == name:
            return pet
            
def remove_pet_by_name(dictionary, name):
    index = 0
    for pet in dictionary["pets"]:
        if pet["name"] == name:
            # pet_remove = index  -  superfluous
            del dictionary["pets"][index]
        index += 1

def add_pet_to_stock(dictionary, new_pet):
    dictionary["pets"].append(new_pet)

def get_customer_cash(dictionary):
    return dictionary["cash"]

def remove_customer_cash(dictionary, amount):
    dictionary["cash"] -= amount

def get_customer_pet_count(dictionary):
    return len(dictionary["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

def customer_can_afford_pet(customer, pet):
    customer_cash = customer["cash"]
    pet_price = pet["price"]
    if customer_cash >= pet_price:
        return True
    else:
        return False

def sell_pet_to_customer(dictionary, name, customer):

    # def find_pet_index(dictionary, name):
    #     index = 0
    #     for pet in dictionary["pets"]:
    #         if pet["name"] == name:
    #             return index
    #         index += 1

    # # find the cost of the pet being sold
    # pet_index = find_pet_index(dictionary, name) - this worked in a separate file but when running here it returned an error saying the index couldn't be a string
    pet_price = dictionary["pets"][3]["price"]  #only got this to work with manually entering the index number
    # print(pet_price)

    # deduct the cost from the customer's cash
    remove_customer_cash(customer, pet_price)
    # print(customer)

    # add the cost to the shop's total cash
    add_or_remove_cash(dictionary, pet_price)
    # print(dictionary["admin"])

    # find the named pet and add it to the customer's pets
    add_pet_to_customer(customer, name)

    # remove the pet, by name, from the shop's inventory
    remove_pet_by_name(dictionary, name)
    # print(dictionary["pets"])

    # increase total number of pets sold
    increase_pets_sold(dictionary, 1)
    # print(dictionary["admin"]["pets_sold"])


#WORKINGS FOR IF PET NOT FOUND - won't set to true when pet found, but worked (or seemed to work) when I was piecing it together in a separate file

# def sell_pet_to_customer(dictionary, name, customer):

#     pet_search_result = find_pet_by_name(dictionary, name)
#     # print(pet_search_result)

#     if pet_search_result != None:
#         pet_found = True
#     else:
#         pet_found = False

#     if pet_found == True:
#         # def find_pet_index(dictionary, name):
#         #     index = 0
#         #     for pet in dictionary["pets"]:
#         #         if pet["name"] == name:
#         #             return index
#         #         index += 1

#         # # find the cost of the pet being sold
#         # pet_index = find_pet_index(dictionary, name)
#         pet_price = dictionary["pets"][3]["price"]
#         # print(pet_price)

#         # deduct the cost from the customer's cash
#         remove_customer_cash(customer, pet_price)
#         print(customer)

#         # add the cost to the shop's total cash
#         add_or_remove_cash(dictionary, pet_price)
#         print(dictionary["admin"])

#         add_pet_to_customer(customer, name)
#         print(customer)

#         # remove the pet, by name, from the shop's inventory
#         remove_pet_by_name(dictionary, name)
#         # print(dictionary["pets"])

#         # increase total number of pets sold
#         increase_pets_sold(dictionary, 1)
#         print(dictionary["admin"]["pets_sold"])
#     else:
#         print("Sorry, pet not found.")

# # sell_pet_to_customer(pet_shop, "Arthur", customers[0])
# # print(pet_shop["admin"]["pets_sold"])












