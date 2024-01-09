from services.adopter_services import AdopterService
from validaters import validate_choice
from .utils import print_adopters, is_valid_name


def check_if_adopters_present(adopters, id):
    adopters_ids = [adopter.id for adopter in adopters]
    return id in adopters_ids


def fetch_adopter_from_list(adopters, id):
    return [adopter for adopter in adopters if adopter.id == id][0]


def list_all_adopters():
    try:
        adopters = AdopterService.get_all_adopters()
        print_adopters(adopters)
    except:
        print("Error printing adopters")


def registering_new_adopter():
    print("*" * 80)
    print("\n Registering new adopter")
    first_name = input("Adopter first_name: ")
    last_name = input("Adopter last_name: ")
    try:
        if is_valid_name(first_name) and is_valid_name(last_name):
            AdopterService.register_adopter(first_name, last_name)
            print("Done!")
        else:
            print("Not created! Invalid names")
    except:
        print("Error registering Adopter")


def update_adopter_details():
    list_all_adopters()
    print("-" * 50)
    id = input("Select adopter by id: ")
    first_name = input("Adopter first_name: ")
    last_name = input("Adopter last_name: ")

    try:
        adopters = AdopterService.get_all_adopters()
        if (id.isnumeric()) and (
            is_valid_name(first_name) and is_valid_name(last_name)
        ):
            id = int(id)
            is_present = check_if_adopters_present(adopters, id)
            if is_present:
                AdopterService.update_adopter(id, first_name, last_name)
                print("Adopter Details Updated")
            else:
                print("No adopter with that Id")
        else:
            print("Invalid input!")

    except:
        print("Error occured while updating adopter details!")


def print_adopter_dogs(dogs, adopter):
    print("\n-" * 3 + f" Listing Adopter - {adopter.get_full_name()} Dogs" + "-" * 50)
    print()
    print("-" * 5 + " Id " + "-" * 10 + " Name " + "-" * 5)
    print("\n")
    for dog in dogs:
        print(" " * 5 + f" {dog.id}" + " " * 5 + f"{dog.name}" + " " * 5)


def print_adopter_associated_facilities(facilities, adopter):
    print(
        "\n-" * 3
        + f" Listing Adopter - {adopter.get_full_name()} Facilities"
        + "-" * 50
    )
    print()
    print("-" * 5 + " Id " + "-" * 10 + " Name " + "-" * 5)
    print("\n")
    for facility in facilities:
        print(" " * 5 + f" {facility.id}" + " " * 5 + f"{facility.name}" + " " * 5)


def list_adopter_dogs():
    list_all_adopters()
    print("-" * 50)
    try:
        id = input("Select adopter by id: ")
        id = int(id)
        adopters = AdopterService.get_all_adopters()
        adopter = fetch_adopter_from_list(adopters, id)
        dogs = AdopterService.get_adopted_dogs(adopter.id)
        print_adopter_dogs(dogs, adopter)
    except:
        print("Wrong choice!")


def list_adopter_associated_facilities():
    list_all_adopters()
    print("-" * 50)
    try:
        id = input("Select adopter by id: ")
        id = int(id)
        adopters = AdopterService.get_all_adopters()
        adopter = fetch_adopter_from_list(adopters, id)
        facilities = AdopterService.get_facilities(adopter.id)
        print_adopter_associated_facilities(facilities, adopter)
    except:
        print("Wrong choice!")


def interacting_with_adopters():
    choice = 1

    while choice != 6:
        print("*" * 100)
        print("*" * 10 + " Now interacting with Adopters  " + "*" * 10)
        print("1) Print all adopters")
        print("2) Register new adopter")
        print("3) Update Adopter details")
        print("4) List all dogs adopted")
        print("5) List facility associated with adopter")
        print("6) Quit interacting with facilities!")

        choice = int(validate_choice(input(">>>> "), 6))

        if choice == 1:
            list_all_adopters()
        elif choice == 2:
            registering_new_adopter()
        elif choice == 3:
            update_adopter_details()
        elif choice == 4:
            list_adopter_dogs()
        elif choice == 5:
            list_adopter_associated_facilities()