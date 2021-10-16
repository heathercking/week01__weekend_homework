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

    def find_pet_index(dictionary, pet_name):
        index = 0
        for pet in dictionary["pets"]:
            if pet["name"] == pet_name:
                return index
            index += 1

    # find the cost of the pet being sold
    pet_index = find_pet_index(dictionary, name)
    pet_price = dictionary["pets"][pet_index]["price"]
    print(pet_price)

    # deduct the cost from the customer's cash
    remove_customer_cash(customer, pet_price)
    print(customer)

    # add the cost to the shop's total cash
    add_or_remove_cash(dictionary, pet_price)
    print(dictionary["admin"])

    # find the named pet and add it to the customer's pets
    for pet in dictionary["pets"]:
        if pet["name"] == name:
            customer["pets"].append(pet)
    
    print(customer)

    # remove the pet, by name, from the shop's inventory
    remove_pet_by_name(dictionary, name)
    print(dictionary["pets"])

    # increase total number of pets sold
    increase_pets_sold(dictionary, 1)
    print(dictionary["admin"]["pets_sold"])















