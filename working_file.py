import pdb

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

def sell_pet_to_customer(dictionary, name, customer):
    
    # finding the named pet and adding it to the customer's pets
    index = 0
    for pet in dictionary["pets"]:
        if pet["name"] == name:
            customer["pets"].append(pet)
        index += 1
    
    print(customers)

    # then we're calling the previous function to remove the pet, by name, from the shop's inventory
    remove_pet_by_name(dictionary, name)
    # print(dictionary["pets"])

    


    # call previous function to increase total number of pets sold
    increase_pets_sold(dictionary, 1)
    # print(dictionary["admin"]["pets_sold"])



sell_pet_to_customer(pet_shop, "Arthur", customers[0])









        

    










