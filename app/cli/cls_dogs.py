from services.dog_services import DogService
from cli.cls_facility import list_facilities
from cli.cls_adopters import list_all_adopters
from validaters import validate_choice
from .utils import print_dogs


def check_if_dog_present(dogs, id):
    dogs_ids = [dog.id for dog in dogs]
    return id in dogs_ids


def list_all_dogs():
    try:
        dogs = DogService.get_all_dogs()
        print_dogs(dogs)
    except:
        print("Error printing dogs")


def creating_new_dog():
    print("*" * 80)
    print("\n Registering new dog")
    name = input("Dog name: ")
    list_all_adopters()
    print("Pick adopter")
    adopter_id = input("Adopter ID: ")
    list_facilities()
    print("Pick Facility")
    facility_id = input("Facility ID: ")

    try:
        if not (name.isnumeric() or name.strip() == ""):
            if adopter_id.isnumeric() and facility_id.isnumeric():
                adopter_id = int(adopter_id)
                facility_id = int(facility_id)
                DogService.create_dog(name, facility_id, adopter_id)
                print("Done!")
            else:
                print("Wrong choice on facility or adopter!")
        else:
            print("Not created!")
    except:
        print("Error creating dog")


def update_dog_details():
    list_all_dogs()
    print("-" * 50)
    id = input("Select dog by id: ")
    name = input("Dog new name: ")

    try:
        dogs = DogService.get_all_dogs()
        if (id.isnumeric()) and (not name.isnumeric()):
            id = int(id)
            is_present = check_if_dog_present(dogs, id)
            if is_present:
                DogService.update_dog(id, name)
                print("Dog Updated")
            else:
                print("No Dog with that Id")
        else:
            print("Invalid input!")

    except:
        print("Error occured while updating dog!")


def delete_dog():
    list_all_dogs()
    print("-" * 50)
    id = input("Delete Dog by id: ")
    try:
        dogs = DogService.get_all_dogs()
        if id.isnumeric():
            id = int(id)
            is_present = check_if_dog_present(dogs, id)
            if is_present:
                DogService.delete_dog(id)
                print("Dog Deleted!")
            else:
                print("No Dog with that Id")
        else:
            print("Invalid input!")

    except:
        print("Error occured while deleting dog!")


def interacting_with_dogs():
    choice = 1

    while choice != 5:
        print("*" * 100)
        print("*" * 10 + " Now interacting with Dogs  " + "*" * 10)
        print("1) Print all dogs")
        print("2) Register new dog")
        print("3) Update Dog details")
        print("4) Delete Dog from the system")
        print("5) Quit interacting with facilities!")

        choice = int(validate_choice(input(">>>> "), 5))

        if choice == 1:
            list_all_dogs()
        elif choice == 2:
            creating_new_dog()
        elif choice == 3:
            update_dog_details()
        elif choice == 4:
            delete_dog()