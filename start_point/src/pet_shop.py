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
