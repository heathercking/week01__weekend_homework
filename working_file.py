import pdb

from start_point.src.pet_shop import add_pet_to_customer

# from start_point.src.pet_shop import remove_pet_by_name



pet_shop = {
    "pets": [
        {
            "name": "Sir Percy",
            "pet_type": "cat",
            "breed": "British Shorthair",
            "price": 500
        },
        {
            "name": "King Bagdemagus",
            "pet_type": "cat",
            "breed": "British Shorthair",
            "price": 500
        },
        {
            "name": "Sir Lancelot",
            "pet_type": "dog",
            "breed": "Pomsky",
            "price": 1000,
        },
        {
            "name": "Arthur",
            "pet_type": "dog",
            "breed": "Husky",
            "price": 900,
        },
        {
            "name": "Tristan",
            "pet_type": "cat",
            "breed": "Basset Hound",
            "price": 800,
        },
        {
            "name": "Merlin",
            "pet_type": "cat",
            "breed": "Egyptian Mau",
            "price": 1500,
        }
    ],
    "admin": {
        "total_cash": 1000,
        "pets_sold": 0,
    },
    "name": "Camelot of Pets"
}

customers = [
            {
                "name": "Alice",
                "pets": [],
                "cash": 1000
            },
            {
                "name": "Bob",
                "pets": [],
                "cash": 50
            },
            {
                "name": "Jack",
                "pets": [],
                "cash": 100
            }
        ]

new_pet = {
            "name": "Bors the Younger",
            "pet_type": "cat",
            "breed": "Cornish Rex",
            "price": 100
        }

def remove_pet_by_name(dictionary, name):
    index = 0
    for pet in dictionary["pets"]:
        if pet["name"] == name:
            # pet_remove = index  -  superfluous
            del dictionary["pets"][index]
        index += 1

def increase_pets_sold(dictionary, num_sold):
    dictionary["admin"]["pets_sold"] += num_sold

def remove_customer_cash(dictionary, amount):
    dictionary["cash"] -= amount

def add_or_remove_cash(dictionary, amount):
    dictionary["admin"]["total_cash"] += amount


# MAIN FUNCTION

def sell_pet_to_customer(dictionary, name, customer):

    # def find_pet_index(dictionary, name):
    #     index = 0
    #     for pet in dictionary["pets"]:
    #         if pet["name"] == name:
    #             return index
    #         index += 1

    # # find the cost of the pet being sold
    # pet_index = find_pet_index(dictionary, name)
    pet_price = dictionary["pets"][3]["price"]
    # print(pet_price)

    # deduct the cost from the customer's cash
    remove_customer_cash(customer, pet_price)
    print(customer)

    # add the cost to the shop's total cash
    add_or_remove_cash(dictionary, pet_price)
    print(dictionary["admin"])

    # find the named pet and add it to the customer's pets
    # for pet in dictionary["pets"]:
    #     if pet["name"] == name:
    #         return customer["pets"].append(pet)
    
    add_pet_to_customer(customer, name)
    print(customer)

    # remove the pet, by name, from the shop's inventory
    remove_pet_by_name(dictionary, name)
    # print(dictionary["pets"])

    # increase total number of pets sold
    increase_pets_sold(dictionary, 1)
    # print(dictionary["admin"]["pets_sold"])

sell_pet_to_customer(pet_shop, "Arthur", customers[0])
# print(customers)
print(customers[0])
# customer_pet_count = len(customers[0]["pets"])
# print(customer_pet_count)












        

    










