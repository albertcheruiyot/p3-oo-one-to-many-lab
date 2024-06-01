class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type.")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        if owner:
            owner.add_pet(self)
        self.all.append(self)

    @classmethod
    def get_all_pets(cls):
        return cls.all

    def set_owner(self, owner):
        if not isinstance(owner, Owner):
            raise Exception("Invalid owner type. Only instances of Owner can be assigned as owners.")
        self.owner = owner
    pass
    
class Owner:
    def __init__(self, name):
        self.name = name
        self.pets_list = []

    def pets(self):
        return self.pets_list

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Invalid pet type. Only instances of Pet can be added.")
        self.pets_list.append(pet)
        if pet.owner is not self:
            pet.set_owner(self)

    def get_sorted_pets(self):
        sorted_pets = sorted(self.pets_list, key=lambda x: x.name)
        return sorted_pets
    pass