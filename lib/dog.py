#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name, breed):
        self._name = name
        self._breed = breed

    def get_name(self):
        print('Retrieving name')
        return self._name

    def get_breed(self):
        print("Retrieving Breed")
        return  self._breed

    def set_name(self, value):
        if not isinstance(value, str):
            print("Name must be a string.")
        elif not (1 <= len(value) <= 25):
            print("Name must be between 1 and 25 characters.")
        else:
            print(f"Setting name to: {value}")
            self._name = value
    name = property(get_name, set_name)

    def set_breed(self, breed_name):
        if breed_name not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        else:
            print(f"Setting breed to: {breed_name}")
            self._breed = breed_name
    breed = property(get_breed, set_breed)

# Testing the Dog class
guido = Dog("", 1)
print(guido._name)
guido.name = "Guido"
print(guido._breed)
guido.name = "Guido"
guido.breed = "qwwqewew"
print(guido.name)

guido.name = 212
guido.breed = "Pointer"




