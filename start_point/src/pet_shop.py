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
    # print(dictionary["pets"])









